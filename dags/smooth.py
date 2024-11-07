from airflow.decorators import dag
from airflow.operators.smooth import SmoothOperator
from datetime import datetime

@dag(    
    start_date=datetime.now(),
    schedule=None,
    catchup=False,
    tags=["smooth"],
)
def smooth():
    video = SmoothOperator(
        task_id="youtube_video"
    )


smooth()
