"""
HealthConnect AI - Skripti 00: Gjenerimi i Dataseteve
======================================================
Autor: Erdona Kadriolli

Qellimi: Gjeneron dataset-et e Diabetit dhe Semundjeve te Zemres
         me strukture identike me ato zyrtare (Pima Indians, UCI Heart).

Te dhenat jane te simuluara mbi baze statistikash publike te dataseteve origjinale.
Per produkt final akademik, zevendesoji me dataset-et reale nga:
  - https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database
  - https://www.kaggle.com/datasets/johnsmith88/heart-disease-dataset
"""

import numpy as np
import pandas as pd
from pathlib import Path

# Random seed per reproducibilitet
np.random.seed(42)

OUTPUT_DIR = Path(__file__).parent.parent / "datasets"
OUTPUT_DIR.mkdir(exist_ok=True)


def generate_diabetes_dataset(n_samples: int = 768) -> pd.DataFrame:
    """
    Gjeneron dataset-in e Diabetit me strukture Pima Indians.
    
    Kolonat (8 features + 1 target):
    - Pregnancies, Glucose, BloodPressure, SkinThickness,
      Insulin, BMI, DiabetesPedigreeFunction, Age, Outcome
    
    Balanca origjinale: ~65% jo-diabetik, ~35% diabetik
    """
    n_negative = int(n_samples * 0.651)  # 500 jo-diabetik
    n_positive = n_samples - n_negative   # 268 diabetik
    
    # --- Pacientet pa diabet (Outcome=0) ---
    negative = pd.DataFrame({
        'Pregnancies': np.random.poisson(3.3, n_negative).clip(0, 17),
        'Glucose': np.random.normal(110, 26, n_negative).clip(44, 199).round().astype(int),
        'BloodPressure': np.random.normal(68, 18, n_negative).clip(0, 122).round().astype(int),
        'SkinThickness': np.random.normal(19.7, 14.9, n_negative).clip(0, 99).round().astype(int),
        'Insulin': np.random.gamma(2, 30, n_negative).clip(0, 846).round().astype(int),
        'BMI': np.random.normal(30.3, 7.7, n_negative).clip(0, 67.1).round(1),
        'DiabetesPedigreeFunction': np.random.gamma(2, 0.2, n_negative).clip(0.078, 2.42).round(3),
        'Age': np.random.gamma(2, 8, n_negative).clip(21, 81).round().astype(int),
        'Outcome': 0
    })
    
    # --- Pacientet me diabet (Outcome=1) ---
    positive = pd.DataFrame({
        'Pregnancies': np.random.poisson(4.9, n_positive).clip(0, 17),
        'Glucose': np.random.normal(141, 32, n_positive).clip(44, 199).round().astype(int),
        'BloodPressure': np.random.normal(70, 21, n_positive).clip(0, 122).round().astype(int),
        'SkinThickness': np.random.normal(22.2, 17.7, n_positive).clip(0, 99).round().astype(int),
        'Insulin': np.random.gamma(2.5, 40, n_positive).clip(0, 846).round().astype(int),
        'BMI': np.random.normal(35.1, 7.3, n_positive).clip(0, 67.1).round(1),
        'DiabetesPedigreeFunction': np.random.gamma(2.5, 0.22, n_positive).clip(0.078, 2.42).round(3),
        'Age': np.random.gamma(2.5, 10, n_positive).clip(21, 81).round().astype(int),
        'Outcome': 1
    })
    
    # Bashkoji dhe perziej
    df = pd.concat([negative, positive], ignore_index=True)
    df = df.sample(frac=1, random_state=42).reset_index(drop=True)
    
    # Shto disa "zero" si ne dataset-in origjinal (vlera mungese te koduara si 0)
    # Kjo eshte tipike per Pima Indians dataset
    zero_cols = ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']
    zero_rates = [0.007, 0.046, 0.296, 0.487, 0.014]
    for col, rate in zip(zero_cols, zero_rates):
        n_zeros = int(len(df) * rate)
        idx = np.random.choice(df.index, n_zeros, replace=False)
        df.loc[idx, col] = 0
    
    return df


def generate_heart_dataset(n_samples: int = 303) -> pd.DataFrame:
    """
    Gjeneron dataset-in e Semundjeve te Zemres me strukture UCI.
    
    Kolonat (13 features + 1 target):
    - age, sex, cp (chest pain type), trestbps (resting blood pressure),
      chol (cholesterol), fbs (fasting blood sugar), restecg (resting ECG),
      thalach (max heart rate), exang (exercise angina), oldpeak,
      slope, ca, thal, target
    
    Balanca origjinale: ~54% jane me semundje (target=1), ~46% jo
    """
    n_positive = int(n_samples * 0.544)  # me semundje
    n_negative = n_samples - n_positive  # pa semundje
    
    # --- Pacientet me semundje zemre (target=1) ---
    positive = pd.DataFrame({
        'age': np.random.normal(56, 8, n_positive).clip(29, 77).round().astype(int),
        'sex': np.random.choice([0, 1], n_positive, p=[0.25, 0.75]),
        'cp': np.random.choice([0, 1, 2, 3], n_positive, p=[0.30, 0.18, 0.40, 0.12]),
        'trestbps': np.random.normal(135, 18, n_positive).clip(94, 200).round().astype(int),
        'chol': np.random.normal(251, 49, n_positive).clip(126, 564).round().astype(int),
        'fbs': np.random.choice([0, 1], n_positive, p=[0.85, 0.15]),
        'restecg': np.random.choice([0, 1, 2], n_positive, p=[0.45, 0.53, 0.02]),
        'thalach': np.random.normal(158, 19, n_positive).clip(71, 202).round().astype(int),
        'exang': np.random.choice([0, 1], n_positive, p=[0.86, 0.14]),
        'oldpeak': np.random.gamma(1.5, 0.5, n_positive).clip(0, 6.2).round(1),
        'slope': np.random.choice([0, 1, 2], n_positive, p=[0.05, 0.35, 0.60]),
        'ca': np.random.choice([0, 1, 2, 3, 4], n_positive, p=[0.65, 0.20, 0.10, 0.04, 0.01]),
        'thal': np.random.choice([0, 1, 2, 3], n_positive, p=[0.005, 0.06, 0.79, 0.145]),
        'target': 1
    })
    
    # --- Pacientet pa semundje (target=0) ---
    negative = pd.DataFrame({
        'age': np.random.normal(53, 9, n_negative).clip(29, 77).round().astype(int),
        'sex': np.random.choice([0, 1], n_negative, p=[0.45, 0.55]),
        'cp': np.random.choice([0, 1, 2, 3], n_negative, p=[0.70, 0.10, 0.15, 0.05]),
        'trestbps': np.random.normal(130, 17, n_negative).clip(94, 200).round().astype(int),
        'chol': np.random.normal(243, 53, n_negative).clip(126, 564).round().astype(int),
        'fbs': np.random.choice([0, 1], n_negative, p=[0.85, 0.15]),
        'restecg': np.random.choice([0, 1, 2], n_negative, p=[0.55, 0.43, 0.02]),
        'thalach': np.random.normal(139, 22, n_negative).clip(71, 202).round().astype(int),
        'exang': np.random.choice([0, 1], n_negative, p=[0.45, 0.55]),
        'oldpeak': np.random.gamma(2.5, 0.7, n_negative).clip(0, 6.2).round(1),
        'slope': np.random.choice([0, 1, 2], n_negative, p=[0.10, 0.65, 0.25]),
        'ca': np.random.choice([0, 1, 2, 3, 4], n_negative, p=[0.30, 0.30, 0.22, 0.16, 0.02]),
        'thal': np.random.choice([0, 1, 2, 3], n_negative, p=[0.005, 0.06, 0.40, 0.535]),
        'target': 0
    })
    
    df = pd.concat([positive, negative], ignore_index=True)
    df = df.sample(frac=1, random_state=42).reset_index(drop=True)
    
    return df


def main():
    print("="*60)
    print("  GJENERIMI I DATASETEVE")
    print("="*60)
    
    # Diabet
    print("\n[1/2] Po gjenerohet dataset-i i Diabetit...")
    df_diabetes = generate_diabetes_dataset(768)
    diabetes_path = OUTPUT_DIR / "diabetes.csv"
    df_diabetes.to_csv(diabetes_path, index=False)
    print(f"  [OK] Ruajt ne: {diabetes_path}")
    print(f"  Rreshta: {len(df_diabetes)} | Kolona: {len(df_diabetes.columns)}")
    print(f"  Outcome=0: {(df_diabetes['Outcome']==0).sum()} | Outcome=1: {(df_diabetes['Outcome']==1).sum()}")
    
    # Zemer
    print("\n[2/2] Po gjenerohet dataset-i i Semundjeve te Zemres...")
    df_heart = generate_heart_dataset(303)
    heart_path = OUTPUT_DIR / "heart.csv"
    df_heart.to_csv(heart_path, index=False)
    print(f"  [OK] Ruajt ne: {heart_path}")
    print(f"  Rreshta: {len(df_heart)} | Kolona: {len(df_heart.columns)}")
    print(f"  target=0: {(df_heart['target']==0).sum()} | target=1: {(df_heart['target']==1).sum()}")
    
    print("\n" + "="*60)
    print("  PERFUNDOI")
    print("="*60)


if __name__ == "__main__":
    main()
