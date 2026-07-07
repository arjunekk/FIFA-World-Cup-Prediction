from pathlib import Path
import sys

# Add the project root to Python's import path
PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(PROJECT_ROOT))

from src.data.loader import load_dataset


def main():
    df = load_dataset(
        source="international_results",
        table="results"
    )

    print("Dataset loaded successfully!\n")

    print(f"Rows: {len(df)}")
    print(f"Columns: {len(df.columns)}")

    print("\nColumn Names:")
    print(df.columns.tolist())

    print("\nFirst 5 Rows:")
    print(df.head())


if __name__ == "__main__":
    main()