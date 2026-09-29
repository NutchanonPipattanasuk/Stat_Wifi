import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

df = pd.read_csv("wifi_data.csv")

bands = ["2.4GHz", "5GHz", "6GHz"]

for band in bands:
    band_data = df[df["PrimaryBand"] == band]

    X = band_data[["Distance"]]
    y = band_data["Throughput_Mbps"]

    model = LinearRegression()
    model.fit(X, y)

    # สร้างช่วงระยะทางสำหรับวาดเส้น regression
    x_line = np.linspace(
        X["Distance"].min(),
        X["Distance"].max(),
        100
    )

    # ทำนาย throughput บนเส้น
    y_line = model.predict(
        pd.DataFrame({"Distance": x_line})
    )

    # จุดข้อมูลจริง
    plt.scatter(
        X["Distance"],
        y,
        label=f"{band} data"
    )

    # เส้น regression
    plt.plot(
        x_line,
        y_line,
        label=f"{band} regression"
    )

plt.xlabel("Distance (m)")
plt.ylabel("Throughput (Mbps)")
plt.title("Linear Regression: Distance vs Throughput")
plt.legend()
plt.grid()

plt.show()