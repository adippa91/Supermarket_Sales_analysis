import pandas as pd
import matplotlib.pyplot as plt
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
cities = df.groupby("City")["Sales"].sum().reset_index()
top_10 = cities.nlargest(10, 'Sales').sort_values("Sales", ascending = True).reset_index()
print(top_10)
fig, ax = plt.subplots(figsize = (8,5))
bars = ax.barh(top_10["City"], top_10["Sales"],color=PRIMARY, edgecolor="white")
for bar in bars:
    width = bar.get_width()
    ax.text(
        width * 0.98,
        bar.get_y() + bar.get_height() / 2,
        f"₹{width/1000:.2f}K",
        ha="right", va="center",
        fontsize=9,
        color="white",
        fontweight="bold"
    )
ax.set_xlabel("Sales", fontsize = 11)
ax.set_ylabel("City", fontsize = 11)
ax.xaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: format(f"₹{x/1000:.2f}K")))
ax.set_xlim(600000,750000)
ax.set_title("Top 10 Sales by City", fontsize = 14, family = "Times New Roman", fontweight = "bold", pad = 12)
plt.tight_layout()
fig.savefig("Sales per City.png", dpi = 300, bbox_inches = "tight")
plt.show()
