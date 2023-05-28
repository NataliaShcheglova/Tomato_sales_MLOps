import os
from random import random, randint
from mlflow import log_artifacts, log_param, log_metric
import mlflow

mlflow.set_tracking_uri("http://127.0.0.1:5000")
mlflow.set_experiment('mlflow_test3')

if __name__ == '__main__':
    log_param("param1", randint(0, 100))

    log_metric("foo", random())
    log_metric("foo", random() + 1)
    log_metric("foo", random() + 2)

    if not os.path.exists("outputs"):
        os.makedirs("outputs")
    with open("outputs/test.txt", "w") as f:
        f.write("hello world")
    log_artifacts("outputs")
