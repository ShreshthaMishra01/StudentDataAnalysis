import os
def statistical_analysis(df):

    print("\nMean")
    print(df[["StudyHours", "Attendance", "Marks"]].mean())

    print("\nMedian")
    print(df[["StudyHours", "Attendance", "Marks"]].median())

    print("\nMode")
    print(df[["StudyHours", "Attendance", "Marks"]].mode())

    print("\nStandard Deviation")
    print(df[["StudyHours", "Attendance", "Marks"]].std())

    print("\nVariance")
    print(df[["StudyHours", "Attendance", "Marks"]].var())

    print("\nCorrelation Matrix")
    print(df[["StudyHours", "Attendance", "Marks"]].corr())