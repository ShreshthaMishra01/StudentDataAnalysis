
import os
def sort_data(df):

    print("\nStudents Sorted by Marks")
    print(df.sort_values(by="Marks", ascending=False))

    print("\nStudents Sorted by Attendance")
    print(df.sort_values(by="Attendance", ascending=False))

    print("\nStudents Sorted by Study Hours")
    print(df.sort_values(by="StudyHours", ascending=False))