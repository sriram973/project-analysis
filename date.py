import pandas as pd
data = {
    "Order date": ["2023-01-01", "2023-01-02", "2023-01-03"]
}
df = pd.DataFrame(data)
df["Order date"] = pd.to_datetime(df["Order date"])
print(df)

print(df["Order date"].dt.year)# it will return the year like 2023

print(df["Order date"].dt.month)# it will return the month like 1

print(df["Order date"].dt.day)# it will return the day like 1

# string operations
data = {
    "Product": ["laptop", "mobile", "tablet", "monitor"]
}
df = pd.DataFrame(data)
print(df)
df["Product"] = df["Product"].str.upper() # it can return in captial letters

print(df)

df["Product"] = df["Product"].str.lower() # it can return in small letters

print(df)

df["Product"] = df["Product"].str.replace("mobile", "keyboard") # it can replace the string 
print(df)

# map values
data = {
    "status": [1, 0, 1, 0]
}
df = pd.DataFrame(data)
print(df)
status_map = {1: "Active", 0: "Inactive"}
df["status"] = df["status"].map(status_map) # it can map the values 
print(df)