from pathlib import Path
import pandas as pd

# Project root directory
PROJECT_ROOT = Path(__file__).resolve().parents[2]


def load_dataset(source: str, table: str) -> pd.DataFrame:
    """
    Load a CSV dataset from the datasets directory.

    Parameters
    ----------
    source : str
        Name of the dataset repository.
    table : str
        Name of the CSV file without the .csv extension.

    Returns
    -------
    pandas.DataFrame
        The loaded dataset.

    Raises
    ------
    FileNotFoundError
        If the requested dataset file does not exist.
    """

    dataset_path = (
        PROJECT_ROOT
        / "datasets"
        / source
        / f"{table}.csv"
    )

    if not dataset_path.exists():
        raise FileNotFoundError(
            f"Dataset not found: {dataset_path}"
        )

    return pd.read_csv(dataset_path)