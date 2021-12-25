
# COMMON
REGION_NAME="us-west-2"

# AIRFLOW
AIRFLOW_DAG_ID="mwaa-sm-customer-churn-dag"

# GLUE
GLUE_ROLE_NAME="AmazonMWAA-Glue-Role"
GLUE_JOB_NAME_PREFIX="mwaa-xgboost-preprocess"
GLUE_JOB_SCRIPT_S3_BUCKET="shimingr-scripts"
GLUE_JOB_SCRIPT_S3_KEY="glue_etl.py"
DATA_S3_SOURCE="s3://shimingr-data/customer-churn.csv"
DATA_S3_DEST="s3://shimingr-data/processed/"

# SAGEMAKER
SAGEMAKER_ROLE_NAME="AmazonMWAA-SageMaker-Role"
SAGEMAKER_TRAINING_JOB_NAME_PREFIX="mwaa-sm-training-job"
SAGEMAKER_TRAINING_DATA_S3_SOURCE="s3://shimingr-data/processed/train/"
SAGEMAKER_VALIDATION_DATA_S3_SOURCE="s3://shimingr-data/processed/validation/"
SAGEMAKER_CONTENT_TYPE="text/csv"
SAGEMAKER_MODEL_NAME_PREFIX="mwaa-sm-customer-churn-model"
SAGEMAKER_ENDPOINT_NAME_PREFIX="mwaa-sm-endpoint" # endpoint names have a 63 max char limit
SAGEMAKER_MODEL_S3_DEST="s3://shimingr-data/model/"
