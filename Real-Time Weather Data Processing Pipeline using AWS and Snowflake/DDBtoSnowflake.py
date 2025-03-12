from datetime import datetime
import pandas as pd
import boto3
from io import StringIO
import os

def handle_insert(record):
    result_dict = {}
    for key, value in record['dynamodb']['NewImage'].items():
        for dt, col in value.items():
            if isinstance(col, dict):
                result_dict[key + "_" + dt] = col.get('S') if 'S' in col else col.get('N') if 'N' in col else col.get('BOOL') if 'BOOL' in col else col.get('L') if 'L' in col else col.get('M') if 'M' in col else col.get('NULL') if 'NULL' in col else col.get('B') if 'B' in col else col.get('SS') if 'SS' in col else col.get('NS') if 'NS' in col else col.get('BS') if 'BS' in col else None
            else:
                result_dict[key + "_" + dt] = col
            if isinstance(result_dict[key + "_" + dt], (list, dict)):
                result_dict[key + "_" + dt] = str(result_dict[key + "_" + dt])
    dff = pd.DataFrame([result_dict])
    return dff

def lambda_handler(event, context):
    df = pd.DataFrame()
    try:
        for record in event['Records']:
            table = record['eventSourceARN'].split("/")[1]
            if record['eventName'] == "INSERT":
                dff = handle_insert(record)
                df = pd.concat([df, dff], ignore_index=True)

        if not df.empty:
            all_columns = list(df)
            df[all_columns] = df[all_columns].astype(str)

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            key = f"snowflake/{table}_{timestamp}.csv"
            bucketName = os.environ.get("S3_BUCKET_NAME", "weatherstreamdata")

            csv_buffer = StringIO()
            df.to_csv(csv_buffer, index=False)

            s3 = boto3.client('s3')
            s3.put_object(Bucket=bucketName, Key=key, Body=csv_buffer.getvalue())

        print(f"Successfully processed {len(event['Records'])} records.")
    except Exception as e:
        print(f"Error in lambda_handler: {e}")

    return {
        'statusCode': 200,
        'body': 'Function executed successfully.'
    }
