from airflow.decorators import dag
from airflow.operators.smooth import SmoothOperator
from datetime import datetime


@dag(
    schedule="@daily",
    start_date=datetime(2024, 9, 11),
    catchup=False,
    tags=["smooth"],
)


def smooth():
    video = SmoothOperator(
        task_id="youtube_video"
    )


smooth()