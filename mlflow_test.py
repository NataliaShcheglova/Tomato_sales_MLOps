import mlflow
import os
from mlflow.models.signature import infer_signature

from sklearn.model_selection import train_test_split
from sklearn.datasets import load_diabetes
from sklearn.ensemble import RandomForestRegressor

mlflow.set_tracking_uri('http://127.0.0.1:5000')
mlflow.sklearn.autolog('sklearn2')
with mlflow.start_run():
    db = load_diabetes()
    X_train, X_test, y_train, y_test = train_test_split(db.data, db.target)
    # Create and train models.
    rf = RandomForestRegressor(n_estimators=100, max_depth=6, max_features=3)
    rf.fit(X_train, y_train)

    # Use the model to make predictions on the test dataset.
    predictions = rf.predict(X_test)

    signature = infer_signature(X_train, predictions)
    #mlflow.sklearn.log_model(rf, "diabetes_rf", signature=signature)

    autolog_run = mlflow.last_active_run()
