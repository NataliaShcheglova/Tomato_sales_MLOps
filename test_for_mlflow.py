import mlflow
import mlflow.sklearn
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split


mlflow.set_tracking_uri("http://127.0.0.1:5000")
mlflow.set_experiment('mlflow_air_quality')
with mlflow.start_run(run_name='air_quality_model_training'):
     data = pd.read_csv('AirQualityUCI.csv')
     data = data.drop(['Date', 'Time', 'Unnamed: 15', 'Unnamed: 16'], axis=1)
     data = data.dropna()
     X = data.drop('CO(GT)', axis=1)
     y = data['CO(GT)']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestRegressor(n_estimators=100)

    model.fit(X_train, y_train)
    mlflow.log_param('n_estimators', 100)
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    mlflow.log_metric('mse', mse)

    mlflow.end_run()