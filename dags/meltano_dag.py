from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from datetime import datetime

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2024, 3, 30),
    "retries": 1,
}

with DAG(
    "meltano_etl",
    default_args=default_args,
    schedule_interval="@daily",
    catchup=False,
) as dag:

    run_meltano = DockerOperator(
        task_id="run_meltano",
        image="meltano/meltano",
        api_version="auto",
        auto_remove=True,
        command="meltano run tap-mysql target-postgres",
        docker_url="unix://var/run/docker.sock",
        network_mode="bridge",
        mount_tmp_dir=False,
        volumes=["/path/to/meltano_project:/project"],
    )

    run_meltano
