import os
def group_data(df):

    print("\nAverage Marks by Grade")
    print(df.groupby("Grade")["Marks"].mean())

    print("\nNumber of Students in Each Grade")
    print(df.groupby("Grade").size())

    print("\nAverage Attendance by Grade")
    print(df.groupby("Grade")["Attendance"].mean())
