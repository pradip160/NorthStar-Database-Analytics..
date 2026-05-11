import pandas as pd

def load_data(path):
    """Load NorthStar dataset."""
    return pd.read_csv(path)

def clean_data(df):
    """Clean missing values and create calculated fields."""
    df = df.copy()
    df["delay_minutes"] = df["delay_minutes"].fillna(0)
    df["profit"] = df["revenue"] - df["cost"]
    df["is_failed"] = (df["delivery_status"] == "Failed").astype(int)
    df["is_delayed"] = df["delivery_status"].isin(["Delayed", "Failed"]).astype(int)
    return df

if __name__ == "__main__":
    df = load_data("../Data/sample_northstar_data.csv")
    cleaned = clean_data(df)
    print(cleaned.head())
