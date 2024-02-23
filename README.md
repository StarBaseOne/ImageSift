# ImageSift

Currently in draft mode. Work in Progress
## Overview

ImageSift is a lightweight serverless image recognition application built using Amazon Web Services (AWS). The project enables users to upload images to a web application, where AWS services are leveraged to recognize and classify objects within the images.

## Components

- **Amazon S3**: Used to store uploaded images. When a user uploads an image, the application saves it to an S3 bucket.
- **AWS Lambda**: Lambda functions are triggered whenever a new image is uploaded to the S3 bucket. These functions are responsible for invoking the image recognition service.
- **Amazon Rekognition**: Rekognition analyzes and recognizes objects within the uploaded images, providing information such as labels, confidence scores, and bounding box coordinates.
- **Amazon SageMaker**: Integration with SageMaker enhances the image analysis workflows.
- **API Gateway**: API Gateway exposes endpoints for the application, allowing users to interact with it to upload images and retrieve recognition results.
- **AWS CloudFormation**: or AWS Serverless Application Model (SAM) is used to define the infrastructure as code.
- **Web Application**: A simple web application is developed using a framework like Flask or Node.js. It allows users to upload images through the web interface and displays the recognition results obtained from Rekognition.

## Benefits

- **Scalability**: The serverless architecture scales automatically based on the number of requests, making it cost-effective.
- **Easy Deployment**: AWS CloudFormation or SAM makes it easy to deploy the entire infrastructure.
- **Seamless Services**: AWS services like S3, Lambda, Rekognition, and API Gateway are highly supported and performant.

## Features

### Fine-tuning Rekognition with SageMaker

- **Improved Accuracy**: Fine-tuning a pre-trained model with SageMaker allows for leveraging transfer learning, improving the accuracy of object detection for specific classes.
- **Flexibility**: Customize the model to detect objects that are critical for the application but may not be well-covered by general-purpose models.
- **Scalability**: Both SageMaker and Rekognition are fully managed services that scale automatically, allowing you to handle large volumes of image data efficiently.

## Deployment

To deploy the ImageSift application on your AWS account, follow these steps:

1. **Modify CloudFormation Template**: Update the `infrastructure.yml` CloudFormation template with your desired configuration options, such as instance type, model hyperparameters, etc.
   
2. **Modify Parameters File**: Update the `parameters.json` file with your specific parameter values, such as S3 bucket name, SageMaker instance type, etc.
   
3. **Deploy CloudFormation Stack**: Use the AWS Management Console, AWS CLI, or AWS SDK to deploy the CloudFormation stack. This will create the necessary resources for your application, including S3 buckets, Lambda functions, API Gateway, etc.
   
4. **Access the Application**: Once the stack is deployed successfully, you can access the application through the provided endpoint. You can upload images through the web interface and perform object detection or classification tasks.
