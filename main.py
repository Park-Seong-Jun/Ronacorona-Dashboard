import pandas as pd

daily_df = pd.read_csv("data/daily_report.csv")
daily_count_df = daily_df[["Confirmed","Deaths","Recovered"]].sum().reset_index(name="Count")
daily_count_df = daily_count_df.rename(columns={"index":"Condition"})
daily_count_df