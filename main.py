import pandas as pd

daily_df = pd.read_csv("data/daily_report.csv")

#일 총 전세계 총 현황
totals_df = daily_df[["Confirmed", "Deaths", "Recovered"]
                     ].sum().reset_index(name="Count")

totals_df = totals_df.rename(columns={"index": "Condition"})

# 국가별 현황
countries_df = daily_df[["Country_Region", "Confirmed", "Deaths", "Recovered"]]
countries_df = countries_df.groupby("Country_Region").sum().reset_index()


#전 세계 일별 현황(확진자, 사망자, 완치자)
conditions = ["confirmed","deaths","recovered"] 

def make_global_df(condition):
    df = pd.read_csv(f"data/time_{condition}.csv")
    df = df.drop(['Province/State', 'Country/Region','Lat','Long'], axis=1).sum().reset_index(name=f"{condition}_total")
    df = df.rename(columns={"index": "Date"})
    return df
final_df =None
for condition in conditions:
    condition_df = make_global_df(condition)
    if final_df is None:
        final_df = condition_df
    else:
         final_df = final_df.merge(condition_df)
