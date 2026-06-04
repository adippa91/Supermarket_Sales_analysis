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
data = pd.read_csv("Supermart Grocery Sales - Retail Analytics Dataset.csv", parse_dates = ["Order Date"])
df = pd.DataFrame(data)
df["Order Date"] = pd.to_datetime(df["Order Date"], format = "mixed")
df["Months"] = df["Order Date"].dt.month
df["Years"] = df["Order Date"].dt.year
monthly_sales = df.groupby(["Years","Months"])["Sales"].sum().reset_index()
monthly_sales["Period"] = pd.to_datetime(monthly_sales["Years"].astype(str) + "-" + monthly_sales["Months"].astype(str), format = "mixed")
monthly_sales = monthly_sales.sort_values("Period")
fig, ax = plt.subplots(figsize = (8,5))
ax.plot(monthly_sales["Period"], monthly_sales["Sales"],
        marker="o",
        color="#2C3E7A",
        markerfacecolor="#ffffff",
        markeredgecolor="#2C3E7A",
        markeredgewidth=1.5)
ax.set_xlabel("Period", fontsize = 11)
ax.set_ylabel("Sales", fontsize = 11)
ax.xaxis.set_major_locator(mdates.MonthLocator(interval=3))
ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: format(f"₹{int(x):,}")))
ax.tick_params(axis="x", rotation=45)
ax.set_title("Monthly Sales", fontsize = 14, family = "Times New Roman", fontweight = "bold", pad = 12)
plt.tight_layout()
fig.savefig("Monthly sales.png", dpi = 300, bbox_inches = "tight")
plt.show()
