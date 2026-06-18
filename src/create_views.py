import sqlite3

db_path = "database/mel_reporting.db"

conn = sqlite3.connect(db_path)

with open("sql/create_views.sql", "r") as file:
    sql_script = file.read()

conn.executescript(sql_script)

conn.commit()

conn.close()

print("Views created successfully.")