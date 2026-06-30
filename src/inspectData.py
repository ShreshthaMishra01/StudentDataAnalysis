import os
def inspect_data(df):

    print("Missing Values:")
    print(df.isnull().sum())

    print("\nDuplicate Records:")
    print(df.duplicated().sum())

    print("\nDescriptive Statistics:")
    print(df.describe())

    print("\nMemory Usage:")
    print(df.memory_usage(deep=True))

    print("\nSummary Information:")
    df.info()