import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("cricket_data.csv")
print("====================================")
print("      CRICKET STATISTICS ANALYZER")
print("====================================")
print("\nComplete Player Data:")
print(data)
print("\nFirst 5 Records:")
print(data.head())
print("\nMissing Values:")
print(data.isnull().sum())
print("\n====================================")
print("           BASIC STATISTICS")
print("====================================")
print("\nTotal Players:", len(data))
print("Total Runs:", data["Runs"].sum())
print("Average Runs:",
      round(data["Runs"].mean(), 2))
print("Total Wickets:", data["Wickets"].sum())
print("Average Strike Rate:",
      round(data["Strike_Rate"].mean(), 2))
highest_run_index = data["Runs"].idxmax()
highest_run_player = data.loc[
    highest_run_index, "Player"
]
highest_runs = data.loc[
    highest_run_index, "Runs"
]
print("\nHighest Run Scorer:")
print(highest_run_player, "-", highest_runs, "runs")
highest_average_index = data["Average"].idxmax()
highest_average_player = data.loc[
    highest_average_index, "Player"
]
highest_average = data.loc[
    highest_average_index, "Average"
]
print("\nHighest Batting Average:")
print(
    highest_average_player,
    "-",
    highest_average
)
highest_sr_index = data["Strike_Rate"].idxmax()
highest_sr_player = data.loc[
    highest_sr_index, "Player"
]
highest_sr = data.loc[
    highest_sr_index, "Strike_Rate"
]
print("\nHighest Strike Rate:")
print(highest_sr_player, "-", highest_sr)
highest_wicket_index = data["Wickets"].idxmax()
highest_wicket_player = data.loc[
    highest_wicket_index, "Player"
]
highest_wickets = data.loc[
    highest_wicket_index, "Wickets"
]
print("\nHighest Wicket Taker:")
print(
    highest_wicket_player,
    "-",
    highest_wickets,
    "wickets"
)
top_5_runs = data.sort_values(
    by="Runs",
    ascending=False
).head(5)
print("\n====================================")
print("          TOP 5 RUN SCORERS")
print("====================================")
print(
    top_5_runs[
        ["Player", "Runs"]
    ]
)
top_5_wickets = data.sort_values(
    by="Wickets",
    ascending=False
).head(5)
print("\n====================================")
print("         TOP 5 WICKET TAKERS")
print("====================================")
print(
    top_5_wickets[
        ["Player", "Wickets"]
    ]
)
strike_rate_data = data.sort_values(
    by="Strike_Rate",
    ascending=False
)
print("\n====================================")
print("       PLAYERS BY STRIKE RATE")
print("====================================")
print(
    strike_rate_data[
        ["Player", "Strike_Rate"]
    ]
)
plt.figure(figsize=(10, 6))
plt.bar(
    data["Player"],
    data["Runs"]
)
plt.xlabel("Players")
plt.ylabel("Runs")
plt.title("Runs Scored by Players")
plt.xticks(
    rotation=45,
    ha="right"
)
plt.tight_layout()
plt.show()
plt.figure(figsize=(10, 6))
plt.bar(
    data["Player"],
    data["Wickets"]
)
plt.xlabel("Players")
plt.ylabel("Wickets")
plt.title("Wickets Taken by Players")
plt.xticks(
    rotation=45,
    ha="right"
)
plt.tight_layout()
plt.show()
plt.figure(figsize=(10, 6))
plt.bar(
    data["Player"],
    data["Strike_Rate"]
)
plt.xlabel("Players")
plt.ylabel("Strike Rate")
plt.title("Strike Rate of Players")
plt.xticks(
    rotation=45,
    ha="right"
)
plt.tight_layout()
plt.show()
print("\n====================================")
print("            PLAYER SEARCH")
print("====================================")
player_name = input(
    "\nEnter player name: "
)
player = data[
    data["Player"].str.lower()
    == player_name.lower()
]
if len(player) > 0:
    print("\nPlayer Statistics:")
    print(player.to_string(index=False))
else:
    print("\nPlayer not found.")
print("\n====================================")
print("       PROGRAM COMPLETED")
print("====================================")