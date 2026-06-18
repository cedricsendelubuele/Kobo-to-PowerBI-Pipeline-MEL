import pandas as pd
import random
from datetime import datetime, timedelta
from pathlib import Path

# Parameters
N_RECORDS = 1000

territories = [
    "Goma",
    "Nyiragongo",
    "Rutshuru",
    "Masisi"
]

kit_types = [
    "NFI_KIT_A",
    "NFI_KIT_B"
]

start_date = datetime(2025, 1, 1)

rows = []

# Generate records
for i in range(1, N_RECORDS + 1):

    distribution_date = start_date + timedelta(
        days=random.randint(0, 180)
    )

    rows.append({

        "submission_id": f"SUB{i:04}",
        "submitted_at": distribution_date,
        "enumerator_id": f"EN{random.randint(1,5):03}",

        "site_id": random.choice([
            "SITE_GOM_01",
            "SITE_NYI_01",
            "SITE_RUT_01",
            "SITE_MAS_01"
        ]),

        "province": "North Kivu",

        "territory": random.choice(territories),

        "beneficiary_uid": f"BEN{i:04}",

        "hh_size": random.choice([
            random.randint(1, 10),
            20
        ]),

        "sex_head": random.choice([
            "Male",
            "Female"
        ]),

        "age_head": random.choice([
            random.randint(18, 70),
            150
        ]),

        "item_kit_type": random.choice(kit_types),

        "qty": random.choice([
            1,
            1,
            1,
            2
        ]),

        "distribution_date": distribution_date
    })

# Create dataframe
df = pd.DataFrame(rows)

# Create folder data if needed
data_folder = Path("data")
data_folder.mkdir(exist_ok=True)

# Save CSV
output_file = data_folder / "kobo_sample.csv"

df.to_csv(
    output_file,
    index=False
)

print("=" * 40)
print("Dataset generated successfully")
print("=" * 40)
print(f"Records : {len(df)}")
print(f"File : {output_file}")