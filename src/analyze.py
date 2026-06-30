import os
def analyze_data(df):

    print("\nAverage Marks:", df["Marks"].mean())

    print("Highest Marks:", df["Marks"].max())

    print("Lowest Marks:", df["Marks"].min())

    print("Average Attendance:", df["Attendance"].mean())

    print("Average Study Hours:", df["StudyHours"].mean())

    pass_percentage = (df["Result"] == "Pass").mean() * 100
    fail_percentage = (df["Result"] == "Fail").mean() * 100

    print("Pass Percentage:", round(pass_percentage, 2), "%")
    print("Fail Percentage:", round(fail_percentage, 2), "%")

    print("\nGrade Distribution:")
    print(df["Grade"].value_counts())
