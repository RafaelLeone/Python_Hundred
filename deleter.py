import pandas as pd


df = pd.read_csv("game_data.csv")

df["Genre(s)"] = "No info"
df["Platform(s)"] = "No info"
df["Release Year"] = "No info"
df["Developer(s)"] = "No info"
df["Publisher(s)"] = "No info"
df["Avg. Time"] = "No info"
df["Avg. Rushed Time"] = "No info"
df["Art"] = "No info"
df["Description"] = "No info"

df.to_csv("game_data.csv", index=False)
