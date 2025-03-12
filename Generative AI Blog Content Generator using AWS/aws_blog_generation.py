import boto3
import botocore.config
import json
from datetime import datetime

def blog_generate_using_bedrock(blogtopic: str) -> str:
    prompt = f'''<s>[INST]Human: Write a 200 words blog on the topic {blogtopic}
    Assistant:[/INST]'''
    body = {
        "prompt": prompt,
        "max_gen_len": 512,
        "temperature": 0.5,
        "top_p": 0.9
    }
    try:
        bedrock = boto3.client("bedrock-runtime", region_name="us-east-2", config=botocore.config.Config(read_timeout=300, retries={'max_attempts': 3}))
        response = bedrock.invoke_model(body=json.dumps(body), modelId="meta.llama3-3-70b-instruct-v1:0")
        response_content = response.get('body').read().decode('utf-8')
        response_data = json.loads(response_content)
        blog_details = response_data.get('generation', '')
        if not blog_details:
            raise ValueError("Generated blog content is empty.")
        return blog_details
    except Exception as e:
        print(f"Error generating the blog: {e}")
        return ""

def save_blog_details_s3(s3_key, s3_bucket, generate_blog):
    s3 = boto3.client('s3')
    try:
        s3.put_object(Bucket=s3_bucket, Key=s3_key, Body=generate_blog)
        print(f"Blog successfully saved to S3 with key: {s3_key}")
    except Exception as e:
        print(f"Error when saving the blog to S3: {e}")
        raise

def lambda_handler(event, context):
    try:
        event = json.loads(event['body'])
        blogtopic = event.get('blog_topic', '').strip()
        if not blogtopic:
            raise ValueError("No blog topic provided.")
        generate_blog = blog_generate_using_bedrock(blogtopic=blogtopic)

        if generate_blog:
            current_time = datetime.now().strftime('%Y%m%d%H%M%S')
            s3_key = f"blog-output/{current_time}.txt"
            s3_bucket = 'genblogs3'
            save_blog_details_s3(s3_key, s3_bucket, generate_blog)
            return {
                'statusCode': 200,
                'body': json.dumps({
                    'message': 'Blog generation completed successfully.',
                }, indent=4)
            }
        else:
            return {
                'statusCode': 500,
                'body': json.dumps({
                    'message': 'Failed to generate the blog.'
                }, indent=4)
            }

    except Exception as e:
        print(f"Error in lambda handler: {e}")
        return {
            'statusCode': 400,
            'body': json.dumps({
                'message': f"Error: {str(e)}"
            }, indent=4)
        }
