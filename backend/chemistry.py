"""
Chemistry processing module using RDKit
Handles molecule parsing, validation, and basic chemical operations
"""

from rdkit import Chem
from rdkit.Chem import Descriptors, AllChem
from typing import Optional, Dict, Tuple
import re


def smiles_to_mol(smiles: str) -> Optional[Chem.Mol]:
    """
    Convert SMILES string to RDKit molecule object
    
    Args:
        smiles: SMILES representation of molecule
    
    Returns:
        RDKit Mol object or None if invalid
    """
    try:
        mol = Chem.MolFromSmiles(smiles)
        return mol
    except:
        return None


def formula_to_smiles(formula: str) -> Optional[str]:
    """
    Attempt to convert molecular formula to SMILES
    NOTE: This is limited - formulas don't contain structure info
    For hackathon, we'll handle common cases
    
    Args:
        formula: Molecular formula (e.g., 'H2O', 'CH4')
    
    Returns:
        SMILES string or None
    """
    # Simple lookup for common molecules (hackathon demo)
    common_molecules = {
        'H2O': 'O',
        'CH4': 'C',
        'CO2': 'O=C=O',
        'NH3': 'N',
        'C2H6O': 'CCO',  # Ethanol
        'C6H12O6': 'OC[C@H]1OC(O)[C@H](O)[C@@H](O)[C@@H]1O',  # Glucose
        'NaCl': '[Na+].[Cl-]',
        'C6H6': 'c1ccccc1',  # Benzene
        'CH3OH': 'CO',  # Methanol
        'H2SO4': 'OS(=O)(=O)O'  # Sulfuric acid
    }
    
    # Clean formula
    formula_clean = formula.strip().replace(' ', '')
    
    if formula_clean in common_molecules:
        return common_molecules[formula_clean]
    
    # For unknown formulas, return None
    # In a real system, this would use more sophisticated methods
    return None


def validate_molecule(mol: Chem.Mol) -> Tuple[bool, str]:
    """
    Validate if molecule is chemically reasonable
    
    Args:
        mol: RDKit molecule object
    
    Returns:
        Tuple of (is_valid, message)
    """
    if mol is None:
        return False, "Invalid molecule structure"
    
    # Check for at least one atom
    if mol.GetNumAtoms() == 0:
        return False, "Molecule has no atoms"
    
    # Sanitization check
    try:
        Chem.SanitizeMol(mol)
        return True, "Valid molecule"
    except:
        return False, "Molecule failed sanitization (chemical rules violated)"


def get_molecular_formula(mol: Chem.Mol) -> str:
    """
    Get molecular formula from RDKit molecule
    
    Args:
        mol: RDKit molecule object
    
    Returns:
        Molecular formula string
    """
    if mol is None:
        return "Unknown"
    
    return Chem.rdMolDescriptors.CalcMolFormula(mol)


def calculate_basic_properties(mol: Chem.Mol) -> Dict[str, float]:
    """
    Calculate basic molecular properties
    
    Args:
        mol: RDKit molecule object
    
    Returns:
        Dictionary of property names and values
    """
    if mol is None:
        return {}
    
    properties = {
        'molecular_weight': Descriptors.MolWt(mol),
        'logp': Descriptors.MolLogP(mol),
        'h_donors': Descriptors.NumHDonors(mol),
        'h_acceptors': Descriptors.NumHAcceptors(mol),
        'tpsa': Descriptors.TPSA(mol),
        'rotatable_bonds': Descriptors.NumRotatableBonds(mol),
        'aromatic_rings': Descriptors.NumAromaticRings(mol),
        'heavy_atoms': mol.GetNumHeavyAtoms(),
        'fraction_csp3': Descriptors.FractionCSP3(mol)
    }
    
    return properties


def generate_3d_coordinates(mol: Chem.Mol) -> Chem.Mol:
    """
    Generate 3D coordinates for molecule visualization
    
    Args:
        mol: RDKit molecule object
    
    Returns:
        Molecule with 3D coordinates embedded
    """
    if mol is None:
        return None
    
    try:
        mol_3d = Chem.AddHs(mol)
        AllChem.EmbedMolecule(mol_3d, randomSeed=42)
        AllChem.MMFFOptimizeMolecule(mol_3d)
        return mol_3d
    except:
        # If 3D generation fails, return original
        return mol


def smiles_to_canonical(smiles: str) -> Optional[str]:
    """
    Convert SMILES to canonical form
    
    Args:
        smiles: Input SMILES string
    
    Returns:
        Canonical SMILES or None
    """
    mol = smiles_to_mol(smiles)
    if mol is None:
        return None
    
    return Chem.MolToSmiles(mol, canonical=True)
