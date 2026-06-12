import pandas as pd
import random
from datetime import datetime, timedelta

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

rows = []

start_date = datetime(2025, 1, 1)

for i in range(1, 1001):

    territory = random.choice(territories)

    hh_size = random.randint(1, 10)

    sex_head = random.choice([
        "Male",
        "Female"
    ])

    age_head = random.randint(18, 70)

    distribution_date = (
        start_date +
        timedelta(days=random.randint(0, 180))
    )

    rows.append({
        "submission_id": f"SUB{i:04}",
        "submitted_at": distribution_date,
        "enumerator_id": f"EN{random.randint(1,5):03}",
        "site_id": f"SITE_{territory[:3].upper()}",
        "province": "North Kivu",
        "territory": territory,
        "beneficiary_uid": f"BEN{i:04}",
        "hh_size": hh_size,
        "sex_head": sex_head,
        "age_head": age_head,
        "item_kit_type": random.choice(kit_types),
        "qty": 1,
        "distribution_date": distribution_date
    })

df = pd.DataFrame(rows)

df.to_csv(
    "data/kobo_sample.csv",
    index=False
)

print("Dataset generated successfully!")
print(f"Records: {len(df)}")