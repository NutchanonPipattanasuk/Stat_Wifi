import pandas as pd

df = pd.read_csv("Wifi7Tests.csv")

print(df.columns)
print(df.shape)

#======================================================================
filtered = df[(df["Environment"] == "Home-LOS") & (df["Mode"] == "Standard") & (df["Connection"] == "Wireless") & (df["PrimaryBand"].isin(["2.4GHz", "5GHz", "6GHz"]))
]
#======================================================================

data = filtered[["Distance", "PrimaryBand", "Run", "Throughput_Mbps"]]

print(data.shape)

print("Distances:")
print(sorted(data["Distance"].unique()))

print("Bands:")
print(data["PrimaryBand"].unique())

data.to_csv("wifi_data.csv", index=False)

print(data.groupby(["Distance", "PrimaryBand"]).size())

groups = data.groupby( ["Distance", "PrimaryBand"] )

#=========================================================================
summary = groups["Throughput_Mbps"].agg(["count", "mean", "std"]).reset_index()

summary.columns = ["Distance", "Band", "N", "Mean", "SD"]
summary["Mean"] = summary["Mean"].round(2)
summary["SD"] = summary["SD"].round(2)
print(summary)

summary.to_csv("wifi_summary.csv", index=False)