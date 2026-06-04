import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
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
df["Months"] = df["Order Date"].dt.month
df["Years"] = df["Order Date"].dt.year
bar_2016 = df[df["Years"] == 2016].groupby("Months")["Sales"].sum()
bar_2017= df[df["Years"] == 2017].groupby("Months")["Sales"].sum()
print(bar_2016)
print(bar_2017)
month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

fig, ax = plt.subplots(figsize = (8,5))
ax.plot(bar_2016.index, bar_2016.values, label = "2016",  marker = "o",  markerfacecolor="white", markeredgecolor=PRIMARY, markeredgewidth=1.5 )
ax.plot(bar_2017.index, bar_2017.values, label = "2017", marker = "o", markerfacecolor="white", markeredgecolor=SECONDARY, markeredgewidth=1.5 )
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"₹{x/1000:.2f}K"))
ax.set_xlabel("Months", fontsize = 15)
ax.set_ylabel("Sales", fontsize = 15)
ax.set_title("Sales Comparison \n2016 Vs 2017", fontsize = 25, family = "Times New Roman")
ax.set_xticks(range(1,13))
ax.set_xticklabels(month_names)
plt.tight_layout()
ax.legend()
fig.savefig("Sales Comparison 2016 Vs 2017.png", dpi = 300, bbox_inches = "tight")
plt.show()
