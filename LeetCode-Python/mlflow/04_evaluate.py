
"""
04. evaluate.py

validation 다 끝내고 rmse 값 도출해낸 이후 마지막 셀에서 Staging 으로 이관하는 작업 
"""

if rmse < 3: 
    client = mlflow.tracking.MlflowCLient()
    latest_version = client.get_model_version_by_alias(name="xgboost_model", alias="Develop")

    client.set_registered_model_alias(
        name="xgboost_model",
        version=latest_version.version,
        alias="Staging"
    )