import pandas as pd
import sqlite3
from pathlib import Path

print("Loading dataset...")

# Lire le fichier CSV
df = pd.read_csv("data/kobo_sample.csv")

# Créer le dossier database s'il n'existe pas
db_folder = Path("database")
db_folder.mkdir(exist_ok=True)

# Nom de la base
db_path = "database/mel_reporting.db"

# Connexion à SQLite
conn = sqlite3.connect(db_path)

print("Creating table...")

# Charger les données dans une table
df.to_sql(
    "beneficiaries",
    conn,
    if_exists="replace",
    index=False
)

conn.close()

print("="*40)
print("Database created successfully")
print("Table : beneficiaries")
print("Database :", db_path)
print("Records :", len(df))
print("="*40)
print("="*40)