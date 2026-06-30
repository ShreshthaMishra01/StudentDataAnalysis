import pandas as pd


def assign_grade(marks):

    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    else:
        return "F"


def assign_result(marks):

    if marks >= 40:
        return "Pass"
    else:
        return "Fail"


def calculate_performance_score(row):

    score = (
        0.6 * row["Marks"] +
        0.2 * row["Attendance"] +
        0.2 * row["StudyHours"]
    )

    return round(score, 2)


def transform_data(df):

    df["Grade"] = df["Marks"].apply(assign_grade)

    df["Result"] = df["Marks"].apply(assign_result)

    df["Performance Score"] = df.apply(
        calculate_performance_score,
        axis=1
    )

    return df