import json
import boto3

s3 = boto3.client('s3')

def handler(event, context):
    try:
        # Retrieve image data from API Gateway proxy integration
        body = json.loads(event['body'])
        image_data = body['image']

        # Decode base64-encoded image data
        image_bytes = image_data.encode('utf-8')

        # Upload image to S3 bucket
        bucket_name = os.environ['UPLOAD_BUCKET_NAME']
        s3.put_object(Bucket=bucket_name, Key='uploaded_image.jpg', Body=image_bytes)

        # Return success response
        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Image uploaded successfully'})
        }
    except Exception as e:
        # Return error response
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }

