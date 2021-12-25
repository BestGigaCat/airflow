import boto3
import json
import time
import pandas as pd

endpoint_name = f"mwaa-sm-endpoint-27d3a1452377414b81b8a5fd43763b4d"
bucket = 'shimingr-data'
key="customer-churn.csv"

# read the csv file from S3
results = pd.read_csv("s3://{}/{}".format(bucket, key), header=None, delimiter=",")
df = pd.DataFrame(results, index = None)
df = df.iloc[:,0].str.split(',', expand=True)

# Need to drop the label column
df = df.drop(df.columns[0], axis=1)

# Take a random sample
df = df.sample(120)

sm_client = boto3.client('sagemaker-runtime')

df_to_list = df.to_string(header=False,
                          index=False,
                          index_names=False).split('\n')

df_to_csv = [','.join(v.split()) for v in df_to_list]

for row in df_to_csv:
    payload = row
    response = sm_client.invoke_endpoint(
        EndpointName=endpoint_name,
        ContentType = "text/csv",
        Body= payload)

    output_body = json.loads(response["Body"].read().decode())
    print(output_body)
    time.sleep(0.5)
