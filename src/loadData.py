import pandas as pd

def load_dataset(file_path):
    try:
        df = pd.read_csv(file_path)
        print("\nDataset Loaded Successfully!\n")
        return df
    except Exception as e:
        print("Error:", e)
        return None


def display_data(df):
    print("FIRST 5 RECORDS ")
    print(df.head())

    print("\n LAST 5 RECORDS ")
    print(df.tail())

    print("\n=SHAPE ")
    print(df.shape)

    print("\n COLUMN NAMES ")
    print(df.columns.tolist())

    print("\n=DATA TYPES ")
    print(df.dtypes)