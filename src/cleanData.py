import os

def clean_data(df):

    # Remove duplicate rows
    df = df.drop_duplicates()

    # Fill missing values with mean
    df["StudyHours"] = df["StudyHours"].fillna(df["StudyHours"].mean())
    df["Attendance"] = df["Attendance"].fillna(df["Attendance"].mean())
    df["Marks"] = df["Marks"].fillna(df["Marks"].mean())

    # Validate Attendance (0–100)
    df = df[(df["Attendance"] >= 0) & (df["Attendance"] <= 100)]

    # Validate Study Hours (>=0)
    df = df[df["StudyHours"] >= 0]

    # Validate Marks (0–100)
    df = df[(df["Marks"] >= 0) & (df["Marks"] <= 100)]

    return df


def save_cleaned_data(df):

    os.makedirs("output", exist_ok=True)

    df.to_csv("output/cleaned_data.csv", index=False)

    print("Cleaned dataset saved successfully.")