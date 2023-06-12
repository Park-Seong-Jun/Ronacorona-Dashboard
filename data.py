import pandas as pd

daily_df = pd.read_csv("data/daily_report.csv")

#일 총 전세계 총 현황
totals_df = daily_df[["Confirmed", "Deaths", "Recovered"]
                     ].sum().reset_index(name="Count")

totals_df = totals_df.rename(columns={"index": "Condition"})

# 국가별 현황
countries_df = daily_df[["Country_Region", "Confirmed", "Deaths", "Recovered"]]
countries_df = countries_df.groupby("Country_Region").sum().sort_values(by="Confirmed", ascending=False).reset_index()

#전세계 & 나라별 일일 현황 데이터
def make_daily_df(country = None):
    
    def make_df(condition):
        df = pd.read_csv(f"data/time_{condition}.csv")
        if country != None:
             df = df.loc[df["Country/Region"] == country]
        df = df.drop(['Province/State', 'Country/Region','Lat','Long'], axis=1).sum().reset_index(name=f"{condition}_total")
        df = df.rename(columns={"index": "Date"})
        return df
    
    conditions = ["confirmed","deaths","recovered"] 
    final_df = None
    for condition in conditions:
        condition_df = make_df(condition)
        if final_df is None:
            final_df = condition_df
        else:
             final_df = final_df.merge(condition_df)
    return final_df

df = countries_df.sort_values("Country_Region")
df = df["Country_Region"].reset_index()
dropDown_options = df["Country_Region"]