import subprocess
import sys
from pathlib import Path

# ---------------------------------------------------
# Configuration
# ---------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent

SCRIPTS = [
    "generate_data.py",
    "dqa.py",
    "load_database.py",
    "create_views.py"
]

print("=" * 60)
print("Kobo-to-PowerBI-Pipeline-MEL")
print("Starting automated pipeline...")
print("=" * 60)

# ---------------------------------------------------
# Execute scripts
# ---------------------------------------------------

for script in SCRIPTS:

    print(f"\nRunning {script}...")

    script_path = PROJECT_ROOT / "src" / script

    result = subprocess.run(
        [sys.executable, str(script_path)],
        cwd=PROJECT_ROOT
    )

    if result.returncode != 0:
        print(f"\nERROR while running {script}")
        print("Pipeline stopped.")
        sys.exit(result.returncode)

    print(f"{script} completed successfully.")

print("\n" + "=" * 60)
print("Pipeline completed successfully!")
print("=" * 60)