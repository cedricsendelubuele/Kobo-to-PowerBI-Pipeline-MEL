import pandas as pd

# Charger les données
df = pd.read_csv("data/kobo_sample.csv")

print("========== DATA QUALITY CHECK ==========")

# Nombre total de lignes
print(f"Total records : {len(df)}")

# Valeurs manquantes
print("\nMissing values:")
print(df.isnull().sum())

# Doublons
duplicates = df.duplicated().sum()

print("\nDuplicate records:")
print(duplicates)

# Âges incohérents
invalid_age = df[
    (df["age_head"] < 18) |
    (df["age_head"] > 110)
]

print("\nInvalid age records:")
print(len(invalid_age))

# Taille ménage anormale
large_household = df[
    df["hh_size"] > 15
]

print("\nLarge household records:")
print(len(large_household))

# Quantité anormale
qty_problem = df[
    df["qty"] > 1
]

print("\nQuantity anomalies:")
print(len(qty_problem))

print("\nDQA completed successfully.")