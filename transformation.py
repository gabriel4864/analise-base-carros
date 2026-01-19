import pandas as pd

df = pd.read_csv("car_price_dataset.csv")

df.to_excel("car_base.xlsx", index = False)