import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.ticker as mticker
from numpy.ma.core import size

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
df["Months"] = df["Order Date"].dt.month
df["Years"] = df["Order Date"].dt.year
prod_category = df.groupby("Category")["Sales"].sum().reset_index()
sub_category = df.groupby("Sub Category")["Sales"].sum().reset_index()
top_10 = sub_category.nlargest(10,"Sales").sort_values("Sales", ascending = False)
fig, ax = plt.subplots(1,2,figsize=(14,8))
bar1 = ax[0].barh(prod_category["Category"], prod_category["Sales"], color = PRIMARY)
for bars in bar1:
    width = bars.get_width()
    ax[0].text(
        width * 0.98,
        bars.get_y() + bars.get_height() / 2 ,
        f"₹{width/1000:.2f}K",
        ha="right", va="center", color="white", fontweight="bold"
    )
bar2 = ax[1].barh(top_10["Sub Category"], top_10["Sales"], color = PRIMARY)
for bars in bar2:
    width = bars.get_width()
    ax[1].text(
        width * 0.98,
        bars.get_y() + bars.get_height() / 2 ,
        f"₹{width/1000:.2f}K",
        ha="right", va="center", color="white", fontweight="bold"
    )

ax[0].set_xlabel("Sales", fontsize = 11)
ax[0].set_ylabel("Category", fontsize = 11)
ax[1].set_xlabel("Sales", fontsize = 11)
ax[1].set_ylabel("Sub Category", fontsize = 11)
ax[0].xaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"₹{x/1000:.0f}K"))
ax[0].set_xlim(1800000,2500000)
ax[1].xaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"₹{x/1000:.0f}K"))
ax[1].set_xlim(500000,1200000)
ax[0].tick_params(axis="x", rotation = 15, size = 5)
ax[1].tick_params(axis="x", rotation = 15, size = 5)
ax[0].set_title("Sales per Category", fontsize=14, fontweight="bold", pad=12, family = "Times New Roman")
ax[1].set_title("Sales per Sub Category", fontsize=14, fontweight="bold", pad=12, family = "Times New Roman")
plt.tight_layout()
fig.savefig("Supermart Grocery Sales.png", dpi = 300, bbox_inches = "tight")
plt.show()