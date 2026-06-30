from src.loadData import load_dataset, display_data
from src.inspectData import inspect_data
from src.cleanData import clean_data, save_cleaned_data
from src.transform import transform_data
from src.analyze import analyze_data
from src.sortData import sort_data
from src.filterData import filter_data
from src.group import group_data
from src.statisticalAnalysis import statistical_analysis
from src.report import generate_report

df = load_dataset("data/student_dataset_v2.csv")

display_data(df)

inspect_data(df)

df = clean_data(df)

save_cleaned_data(df)

df = transform_data(df)

filter_data(df)

analyze_data(df)

sort_data(df)

group_data(df)

statistical_analysis(df)

generate_report(df)