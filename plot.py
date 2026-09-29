import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("wifi_summary.csv")

print(df)

for band in ["2.4GHz", "5GHz", "6GHz"]:
    band_data = df[df["Band"] == band]

    plt.errorbar(
        band_data["Distance"],
        band_data["Mean"],
        yerr=band_data["SD"],
        marker="o",
        capsize=5,
        label=band
    )

plt.xlabel("Distance (m)")
plt.ylabel("Mean Throughput (Mbps)")
plt.title("Distance vs Mean Throughput")
plt.legend()
plt.grid()

plt.show()