import pandas as pd
import os


def generate_report(df):

    os.makedirs("output", exist_ok=True)

    total_students = len(df)

    passed_students = len(df[df["Result"] == "Pass"])

    failed_students = len(df[df["Result"] == "Fail"])

    highest_marks = df["Marks"].max()

    lowest_marks = df["Marks"].min()

    average_marks = round(df["Marks"].mean(), 2)

    average_attendance = round(df["Attendance"].mean(), 2)

    grade_distribution = df["Grade"].value_counts()

    report = {
        "Total Students": total_students,
        "Passed Students": passed_students,
        "Failed Students": failed_students,
        "Highest Marks": highest_marks,
        "Lowest Marks": lowest_marks,
        "Average Marks": average_marks,
        "Average Attendance": average_attendance
    }

    report_df = pd.DataFrame(report.items(), columns=["Metric", "Value"])

    grade_df = grade_distribution.reset_index()
    grade_df.columns = ["Grade", "Count"]

    report_df.to_csv("output/report.csv", index=False)

    grade_df.to_csv("output/grade_distribution.csv", index=False)

    print("Report generated successfully.")