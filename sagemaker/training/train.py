import os
import argparse
import boto3
import sagemaker
from sagemaker import get_execution_role
from sagemaker.tensorflow import TensorFlow

def train_model(bucket_name, prefix):
    # Define training data location
    s3_train_data = f's3://{bucket_name}/{prefix}/train'
    s3_validation_data = f's3://{bucket_name}/{prefix}/validation'
    s3_output_location = f's3://{bucket_name}/{prefix}/output'

    # Get SageMaker execution role
    role = get_execution_role()

    # Configure TensorFlow Estimator
    estimator = TensorFlow(entry_point='train_entry.py',
                           role=role,
                           instance_count=1,
                           instance_type='ml.p3.2xlarge',
                           framework_version='2.3.1',
                           py_version='py37',
                           output_path=s3_output_location)

    # Launch training job
    estimator.fit({'train': s3_train_data, 'validation': s3_validation_data})

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--bucket", type=str, help="Name of the S3 bucket")
    parser.add_argument("--prefix", type=str, help="Prefix for data and output locations")
    args = parser.parse_args()

    train_model(args.bucket, args.prefix)
