import pandas as pd

df = pd.read_csv("wifi_data.csv")

bands = ["2.4GHz", "5GHz", "6GHz"]

for band in bands:
    band_data = df[df["PrimaryBand"] == band]

    r = band_data["Distance"].corr(band_data["Throughput_Mbps"])

    print(f"{band}: r = {r:.4f}")