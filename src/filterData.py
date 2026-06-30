import os

def filter_data(df):

    os.makedirs("output", exist_ok=True)

    # Top-performing students (Marks >= 90)
    toppers = df[df["Marks"] >= 90]
    toppers.to_csv("output/toppers.csv", index=False)

    # Failed students (Marks < 40)
    failed = df[df["Marks"] < 40]
    failed.to_csv("output/failed_students.csv", index=False)

    # Attendance below 75%
    low_attendance = df[df["Attendance"] < 75]
    low_attendance.to_csv("output/low_attendance.csv", index=False)

    # Study Hours > 8
    high_study = df[df["StudyHours"] > 8]
    high_study.to_csv("output/study_more_than_8hrs.csv", index=False)

    print("Filtered datasets saved successfully.")