import os
from random import random, randint
from mlflow import log_artifacts, log_param, log_metric
import mlflow

mlflow.set_tracking_uri("http://127.0.0.1:5000")
mlflow.set_experiment('mlflow_time_series')

if __name__ == '__main__':
    log_param("param1", randint(0, 100))

    # Имитация обучения модели и логирование метрик
    for i in range(10):
        # Генерация случайной метрики
        metric_value = random() + i
        log_metric("metric", metric_value)

    # Создание и сохранение артефактов
    if not os.path.exists("outputs"):
        os.makedirs("outputs")
    with open("outputs/test.txt", "w") as f:
        f.write("hello world")
    log_artifacts("outputs")