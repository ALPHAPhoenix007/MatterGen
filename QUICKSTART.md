# 🚀 MatterGen Quick Start Guide

## Installation (2 minutes)

1. **Install dependencies:**
```bash
pip install -r requirements.txt
```

2. **Run the app:**
```bash
streamlit run app.py
```

3. **Open browser:**
```
http://localhost:8501
```

---

## First Time Setup

On first run, the app will automatically:
- Load the dataset (50 compounds)
- Train 4 ML models (Random Forest)
- Initialize similarity engine
- Cache everything for fast subsequent loads

⏱️ **First load**: ~30 seconds  
⏱️ **Subsequent loads**: <5 seconds

---

## How to Use

### Step 1: Select Input Method (Sidebar)
- **SMILES String**: Direct chemical notation (e.g., `c1ccccc1`)
- **Molecular Formula**: Convert formula to SMILES (e.g., `H2O`)
- **Example Molecules**: Pick from pre-loaded samples

### Step 2: Enter Molecule
Examples to try:
- Benzene: `c1ccccc1`
- Ethanol: `CCO`
- Water: `O` or formula `H2O`
- Acetone: `CC(=O)C`

### Step 3: Click "Predict Properties"

### Step 4: Explore Results
- **Predictions Tab**: See all 4 property predictions
- **Similarity Tab**: Find similar known compounds
- **3D Structure Tab**: Rotate and view molecule
- **Model Insights Tab**: Understand how predictions work

---

## Demo Flow for Judges

1. **Introduction** (30 sec)
   - "MatterGen predicts material properties using ML and chemistry"

2. **Input Demo** (30 sec)
   - Enter benzene (`c1ccccc1`)
   - Click predict

3. **Results Walkthrough** (1 min)
   - Show 4 predictions
   - Explain what each property means
   - Show molecular descriptors

4. **Similarity** (30 sec)
   - Show top 5 similar compounds
   - Explain Tanimoto similarity
   - Compare properties

5. **3D Visualization** (30 sec)
   - Show interactive 3D structure
   - Rotate the molecule

6. **Technical Deep Dive** (1 min)
   - Show feature importance graph
   - Explain Random Forest approach
   - Discuss dataset and training

**Total: ~4 minutes**

---

## Common Issues & Fixes

### "Module not found" error
```bash
pip install -r requirements.txt --force-reinstall
```

### RDKit installation issues
```bash
conda install -c conda-forge rdkit
```

### Streamlit not opening
- Check if port 8501 is free
- Try: `streamlit run app.py --server.port 8502`

### 3D visualization not showing
- Make sure Py3Dmol is installed
- Some complex molecules may fail - this is expected

---

## Adding Custom Molecules to Dataset

Edit `data/materials_dataset.csv`:

```csv
smiles,formula,band_gap_ev,formation_energy,stability_score,melting_point_k,name
CCO,C2H6O,7.0,-2.35,0.90,159.0,Ethanol
```

Restart the app to retrain models.

---

## Hackathon Presentation Tips

**DO:**
✅ Emphasize the full-stack nature (ML + chemistry + UI)  
✅ Show live demo with multiple molecules  
✅ Explain the science (fingerprints, similarity)  
✅ Discuss real-world applications  
✅ Mention future improvements  

**DON'T:**
❌ Get stuck in code details  
❌ Apologize for "simple" implementation  
❌ Skip the demo to explain theory  
❌ Forget to show the 3D visualization  
❌ Ignore questions about accuracy  

---

## Key Talking Points

1. **"We built a complete ML pipeline"**
   - Data → Features → Model → Predictions

2. **"We use industry-standard tools"**
   - RDKit (used by pharma companies)
   - Morgan fingerprints (gold standard)

3. **"Models are interpretable"**
   - Random Forest (not black box)
   - Feature importance analysis
   - Similarity matching for validation

4. **"Production-ready architecture"**
   - Modular backend
   - Cached models
   - Scalable design

5. **"Real applications"**
   - Drug discovery
   - Materials science
   - Battery research
   - Solar cells

---

## Advanced: API Usage (Optional)

You can also use the backend directly:

```python
from backend.chemistry import smiles_to_mol
from backend.features import extract_features_from_smiles
from backend.ml_models import PropertyPredictor

# Parse molecule
mol = smiles_to_mol("c1ccccc1")

# Extract features
features = extract_features_from_smiles("c1ccccc1")

# Predict (after training)
predictor = PropertyPredictor("band_gap_ev")
# ... train predictor ...
prediction = predictor.predict_from_smiles("c1ccccc1")
print(f"Band gap: {prediction:.2f} eV")
```

---

## Contact & Support

**Found a bug?** Open an issue  
**Have a question?** Check README.md  
**Want to contribute?** Fork and PR  

---

**Good luck with your hackathon! 🚀**
