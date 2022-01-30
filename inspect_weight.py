# %%
import pandas as pd
import seaborn as sns

from common import save_plot, data


# %%
df = pd.concat(
    map(
        pd.read_json,
        (data / "Personal & Account").glob("weight-*.json"),
    ),
    ignore_index=True,
)


# %%
ax = sns.scatterplot(data=df, x="date", y="bmi")
save_plot(ax.get_figure(), "bmi")

# %%
ax = sns.scatterplot(data=df, x="date", y="weight")
save_plot(ax.get_figure(), "weight")

# %%
df["year"] = df["date"].dt.year
ax = sns.barplot(data=df.groupby("year").mean().reset_index(), x="year", y="bmi")
save_plot(ax.get_figure(), "ave-bmi-per-year")

# %%
ax = sns.barplot(data=df.groupby("year").mean().reset_index(), x="year", y="weight")
save_plot(ax.get_figure(), "ave-weight-per-year")
