import pandas as pd
data = {
    "Product":["laptop","mobile","tablet","monitor"],
    "price":[50000,25000,18000,12000],
    "stock":[10,25,15,8]
}
df = pd.DataFrame(data)
print(df)

print(df["Product"])
print(df[["Product","price"]])
print(df.loc[2])
print(df.iloc[1])

df["total_value"] = df["price"] * df["stock" ]
print(df)