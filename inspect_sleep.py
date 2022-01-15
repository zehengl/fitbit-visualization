# %%
from os import getenv
from pathlib import Path

import pandas as pd
import seaborn as sns
from dotenv import load_dotenv

load_dotenv()

name = getenv("NAME")
output = Path("output")
output.mkdir(exist_ok=True)


# %%
def save_plot(fig, name):
    fig.savefig(output / f"{name}.png", dpi=300, bbox_inches="tight")


# %%
df = pd.concat(
    map(pd.read_json, Path(f"MyFitbitData/{name}/Sleep").glob("sleep-*.json")),
    ignore_index=True,
)

df["dateOfSleep"] = pd.to_datetime(df["dateOfSleep"])
df["startTime"] = pd.to_datetime(df["startTime"])
df["endTime"] = pd.to_datetime(df["endTime"])

df = df.sort_values(by="dateOfSleep")

df["year"] = df["dateOfSleep"].dt.year

# %%
ax = sns.countplot(x="year", data=df)
save_plot(ax.get_figure(), "records-per-year")


# %%
df["hour"] = df["startTime"].dt.hour

ax = sns.countplot(x="hour", data=df)
save_plot(ax.get_figure(), "start-time-overall")


# %%
ax = sns.countplot(x="hour", data=df[df["mainSleep"]])
save_plot(ax.get_figure(), "start-time-main-sleep")


# %%
ax = sns.countplot(x="hour", hue="year", data=df[df["mainSleep"]])
save_plot(ax.get_figure(), "start-time-main-sleep")


# %%
ave_duration_of_sleep_by_year = (
    df[df["mainSleep"]].groupby("year")[["duration"]].mean().reset_index()
)
ave_duration_of_sleep_by_year["duration"] /= 60 * 60 * 1000

ax = sns.barplot(
    x="year",
    y="duration",
    data=ave_duration_of_sleep_by_year,
)
save_plot(ax.get_figure(), "average-duration-of-sleep-by-year")


# %%
df["month"] = df["dateOfSleep"].dt.month
ave_duration_of_sleep_by_month = (
    df[df["mainSleep"]].groupby("month")[["duration"]].mean().reset_index()
)
ave_duration_of_sleep_by_month["duration"] /= 60 * 60 * 1000

ax = sns.barplot(
    x="month",
    y="duration",
    data=ave_duration_of_sleep_by_month,
)
save_plot(ax.get_figure(), "average-duration-of-sleep-by-month")


# %%
ave_duration_of_sleep_by_year_month = (
    df[df["mainSleep"]].groupby(["year", "month"])[["duration"]].mean().reset_index()
)
ave_duration_of_sleep_by_year_month["duration"] /= 60 * 60 * 1000

ax = sns.lineplot(
    x="month",
    y="duration",
    hue="year",
    data=ave_duration_of_sleep_by_year_month,
    palette="husl",
)
save_plot(ax.get_figure(), "average-duration-of-sleep-by-year-month")
