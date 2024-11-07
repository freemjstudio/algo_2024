### 03_train.py 


from mlflow.models.signature import infer_signature 

signature = infer_signature(X_train, y_val_pred)
mlflow.xgboost.log_model(xgb_model, "xgboost_model", signature=signature)

"""
트레이닝 이후, model registry 에 등록한 다음, 
alias 로 Model 을 등록합니다. 

-> 바꾼 이유 : unity catalog 에서 get latest version 함수를 지원하지 않음. 대신 alias 를 사용하는 것을 권장하고 있음. 
"""
from mlflow.tracking.client import MlflowClient 

client = MlflowClient()
model_version_details = client.get_model_version(name="xgboost_model", version=1)

# Develop 으로 해당 버전 등록 
client.set_registered_model_alias(name="xgboost_model", alias="Develop", version=1)
model_version_details.status # READY 