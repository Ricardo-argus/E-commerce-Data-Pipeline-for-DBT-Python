import os
import subprocess
import sys

# Função auxiliar para rodar comandos

def run_cmd(cmd):
    print(f"\n>>> Running: {cmd}")
    result = subprocess.run(cmd, shell=True)
    if result.returncode != 0:
        print(f"Command failed: {cmd}")
        sys.exit(result.returncode)

# Funções equivalentes ao Makefile

def install():
    run_cmd("pip install -r requirements.txt")

def python_ingest():
    run_cmd("python src/ingestion_data.py")

def python_refine():
    run_cmd("python src/refino_data.py")

def python_gold():
    run_cmd("python src/gold_transform.py")

def python_charts():
    run_cmd("python src/charts_gold.py")

def dbt_seed():
    run_cmd("dbt seed --project-dir dbt")

def dbt_run():
    run_cmd("dbt run --project-dir dbt")

def dbt_test():
    run_cmd("dbt test --project-dir dbt")

def dbt_snapshot():
    run_cmd("dbt snapshot --project-dir dbt")

def dbt_docs():
    run_cmd("dbt docs generate --project-dir dbt")
    run_cmd("dbt docs serve --project-dir dbt")

def pipeline():
    install()
    python_ingest()
    python_refine()
    dbt_seed()
    dbt_run()
    dbt_test()
    dbt_snapshot()
    python_gold()
    python_charts()

# Menu simples

if __name__ == "__main__":
    tasks = {
        "install": install,
        "python-ingest": python_ingest,
        "python-refine": python_refine,
        "python-gold": python_gold,
        "python-charts": python_charts,
        "dbt-seed": dbt_seed,
        "dbt-run": dbt_run,
        "dbt-test": dbt_test,
        "dbt-snapshot": dbt_snapshot,
        "dbt-docs": dbt_docs,
        "pipeline": pipeline,
    }

    if len(sys.argv) < 2 or sys.argv[1] not in tasks:
        print("Usage: python run.py [task]")
        print("Available tasks:", ", ".join(tasks.keys()))
        sys.exit(1)

    task = sys.argv[1]
    tasks[task]()
