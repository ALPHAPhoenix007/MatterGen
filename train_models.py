"""
Standalone script to train and save ML models
Run this to pre-train models before deployment
"""

import pandas as pd
import numpy as np
from pathlib import Path
from backend.ml_models import MultiPropertyPredictor
from backend.similarity import SimilarityEngine
from utils.config import PROPERTIES

def main():
    """Train all models and save to disk"""
    print("=" * 60)
    print("MatterGen Model Training Script")
    print("=" * 60)
    
    # Load dataset
    data_path = Path(__file__).parent / 'data' / 'materials_dataset.csv'
    print(f"\n📂 Loading dataset from: {data_path}")
    df = pd.read_csv(data_path)
    print(f"✓ Loaded {len(df)} compounds")
    
    # Initialize predictor
    print(f"\n🤖 Training models for {len(PROPERTIES)} properties...")
    predictor = MultiPropertyPredictor(PROPERTIES)
    
    # Train all models
    results = predictor.train_all(df, smiles_col='smiles')
    
    # Display results
    print("\n📊 Training Results:")
    print("-" * 60)
    for prop, scores in results.items():
        print(f"{prop:25s} | CV R² = {scores['cv_mean']:.3f} ± {scores['cv_std']:.3f}")
    
    # Save models
    print("\n💾 Saving models...")
    models_dir = Path(__file__).parent / 'models'
    models_dir.mkdir(exist_ok=True)
    
    for prop, model in predictor.models.items():
        model_path = models_dir / f'{prop}_model.pkl'
        model.save(str(model_path))
        print(f"✓ Saved: {model_path}")
    
    # Initialize similarity engine
    print("\n🔍 Initializing similarity engine...")
    sim_engine = SimilarityEngine()
    sim_engine.load_database(df, smiles_col='smiles')
    print(f"✓ Loaded {len(sim_engine.database_smiles)} molecules for similarity search")
    
    # Feature importance
    print("\n📈 Top 5 Important Features (Band Gap Model):")
    print("-" * 60)
    importance = predictor.models['band_gap_ev'].get_feature_importance()
    for idx, (feat, imp) in enumerate(list(importance.items())[:5], 1):
        print(f"{idx}. {feat:25s} | Importance: {imp:.4f}")
    
    print("\n" + "=" * 60)
    print("✅ Training complete! Models ready for deployment.")
    print("=" * 60)

if __name__ == "__main__":
    main()
