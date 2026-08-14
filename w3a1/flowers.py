from ucimlrepo import fetch_ucirepo

# Fetch the Iris dataset (UCI id=53) 
iris = fetch_ucirepo(id=53)

# Access data as pandas DataFrames
x = iris.data.features  # measurements (sepal/petal length & width)
y = iris.data.targets   # flower species

print("Iris dataset loaded successfully!")
print("Feature data (x):")
print(x.head())
print("\nTarget data (y):")
print(y.head())

# 1. Total number of records in the file
total_records = len(x)
print("Total number of records:", total_records)

# 2. Total number of different flowers available
total_flowers = y["class"].nunique()
print("Total number of different flowers:", total_flowers)

# 3. Names of all different flowers in the dataset
flower_names = y["class"].unique()
print("Names of all different flowers:")
for name in flower_names:
    print(" -", name)