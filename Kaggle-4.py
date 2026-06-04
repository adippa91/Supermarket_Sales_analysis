import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as mticker
plt.rcParams.update({
    "figure.facecolor": "#FDF6EC",   # warm cream canvas
    "axes.facecolor": "#FFFDF9",     # off-white chart bg
    "grid.color": "#E8D5B7",         # warm grid lines
    "grid.alpha": 0.6,
    "grid.linestyle": "--",
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.labelcolor": "#2D2D2D",
    "xtick.color": "#555555",
    "ytick.color": "#555555",
    "text.color": "#2D2D2D",
})
PRIMARY   = "#2C3E7A"  # all main bars and lines
SECONDARY = "#E07B39"  # accents, second lines, profit bars
data = pd.read_csv("Supermart Grocery Sales - Retail Analytics Dataset.csv", parse_dates = ["Order Date"])
df = pd.DataFrame(data)
df["Order Date"] = pd.to_datetime(df["Order Date"], format = "mixed")
df["Months"] = df["Order Date"].dt.month_name()
df["Years"] = df["Order Date"].dt.year
regions = df.groupby("Region")[["Sales", "Profit"]].sum().reset_index()
regions = regions[regions["Region"] != "North"]
x = np.arange(len(regions["Region"]))
width = 0.35
fig, ax = plt.subplots(figsize=(14,5))
bars1 = ax.bar(x + width/2, regions["Sales"], width = width, label = "Sales", color = PRIMARY)
for bar in bars1:
    height = bar.get_height()
    ax.text(
        bar.get_x() + bar.get_width()/2,
        height * 0.94,
    f"₹{height/1000000:.2f}M",
    ha = "center",va= "bottom", fontsize = 9 , color = "white")
bars2 = ax.bar(x - width/2, regions["Profit"], width = width, label = "Profit", color = SECONDARY)
for bar in bars2:
    height = bar.get_height()
    ax.text(
        bar.get_x() + bar.get_width()/2,
        height * 0.65,
    f"₹{height/1000000:.2f}M",
    ha = "center", va= "bottom", fontsize = 9, color = "white" )
ax.set_xticks(x)
ax.set_xticklabels(regions["Region"])
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"₹{int(x/1000000)}M"))
plt.tight_layout()
ax.legend()
fig.savefig("Profit-Sale bar charts.png", dpi = 300, bbox_inches = "tight")
plt.show()
