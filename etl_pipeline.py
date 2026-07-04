import pandas as pd
import numpy as np

def run_etl():
    print("🚀 Starting ETL Pipeline for Tech Layoffs Dataset...")
    
    # 1. EXTRACT: Load the raw dataset
    # (Assuming your raw data file is named 'layoffs.csv' in your local setup)
    try:
        df = pd.read_csv("layoffs.csv")
    except FileNotFoundError:
        print("❌ Error: 'layoffs.csv' not found. Please place the raw data file in the directory.")
        return

    # 2. TRANSFORM: Clean and Optimize the Data
    print("🧹 Transforming data layers...")
    
    # Convert date columns to standard datetime formats
    if 'date' in df.columns:
        df['date'] = pd.to_datetime(df['date'])
        # Fill missing dates with a placeholder or drop
        df = df.dropna(subset=['date'])

    # Handle missing numeric data using standard industry defaults
    if 'total_laid_off' in df.columns:
        df['total_laid_off'] = df['total_laid_off'].fillna(0).astype(int)
        
    if 'percentage_laid_off' in df.columns:
        df['percentage_laid_off'] = df['percentage_laid_off'].fillna(0.0)

    # Standardize text columns (remove accidental spaces, fix capitalization)
    text_cols = ['company', 'location', 'industry', 'stage', 'country']
    for col in text_cols:
        if col in df.columns:
            df[col] = df[col].astype(str).str.strip().str.title()

    # 3. LOAD: Output a clean, high-performance file for Tableau
    output_file = "cleaned_tech_layoffs.csv"
    df.to_csv(output_file, index=False)
    print(f"✅ Success! Cleaned dataset saved as '{output_file}' with {len(df)} records.")

if __name__ == "__main__":
    run_etl()
