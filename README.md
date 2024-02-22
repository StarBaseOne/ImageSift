# ImageSift
Lightweight serverless image recognition application using Amazon Web Services (AWS). This project will allow users to upload images to a web application, and the application will use AWS services to recognize and classify objects within the images.


## Components:

* **Amazon S3**: S3 to store uploaded images. When a user uploads an image, the application will save it to an S3 bucket.
* **AWS Lambda**: Lambda functions are triggered whenever a new image is uploaded to the S3 bucket. The Lambda functions will be responsible for invoking the image recognition service.
* **Amazon Rekognition**: Amazon Rekognition analyzes and recognizes objects within the uploaded images. Retrieve information such as labels, confidence scores, and bounding box coordinates.
* **API Gateway**: API Gateway to expose endpoints for the application. Users can interact with the application through these endpoints to upload images and retrieve recognition results.
* **AWS CloudFormation**: or AWS Serverless Application Model (SAM) to define the infrastructure as code
* **Web Application**: Develop a simple web application using a framework like Flask or Node.js. Allow users to upload images through the web interface, and display the recognition results obtained from Rekognition.

## Benefits:

* **Scalability**: The serverless architecture scales automatically based on the number of requests, making it cost-effective.
* **Easy Deployment**: AWS CloudFormation or SAM makes it easy to deploy your entire infrastructure.
* **Seamless Services**:  AWS services like S3, Lambda, Rekognition, API Gateway are highly supported and highly performant services


## Features:
To be Added
