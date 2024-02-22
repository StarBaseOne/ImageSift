import json

def update_cloudformation_template(template_file, new_template_file, bucket_name, bucket_prefix, instance_type, num_layers, learning_rate, epochs):
    # Load CloudFormation template
    with open(template_file, 'r') as f:
        template = json.load(f)

    # Update parameters in the template
    template['Resources']['ImageUploadBucket']['Properties']['BucketName'] = bucket_name
    template['Resources']['ImageUploadBucket']['Properties']['BucketName'] = bucket_prefix

    # Update instance type in the template
    template['Resources']['UploadImageFunction']['Properties']['InstanceType'] = instance_type

    # Update hyperparameters in the template
    template['Resources']['UploadImageFunction']['Properties']['Environment']['Variables']['NUM_LAYERS'] = num_layers
    template['Resources']['UploadImageFunction']['Properties']['Environment']['Variables']['LEARNING_RATE'] = learning_rate
    template['Resources']['UploadImageFunction']['Properties']['Environment']['Variables']['EPOCHS'] = epochs

    # Save the modified template to a new file
    with open(new_template_file, 'w') as f:
        json.dump(template, f, indent=4)

def update_parameters_file(parameters_file, new_parameters_file, bucket_name, bucket_prefix, instance_type, num_layers, learning_rate, epochs):
    # Load parameters file
    with open(parameters_file, 'r') as f:
        parameters = json.load(f)

    # Update parameter values
    for param in parameters:
        if param['ParameterKey'] == 'BucketName':
            param['ParameterValue'] = bucket_name
        elif param['ParameterKey'] == 'BucketPrefix':
            param['ParameterValue'] = bucket_prefix
        elif param['ParameterKey'] == 'InstanceType':
            param['ParameterValue'] = instance_type
        elif param['ParameterKey'] == 'NumberOfLayers':
            param['ParameterValue'] = num_layers
        elif param['ParameterKey'] == 'LearningRate':
            param['ParameterValue'] = learning_rate
        elif param['ParameterKey'] == 'Epochs':
            param['ParameterValue'] = epochs

    # Save the modified parameters to a new file
    with open(new_parameters_file, 'w') as f:
        json.dump(parameters, f, indent=4)

if __name__ == "__main__":
    # User-provided values
    bucket_name = 'your-s3-bucket-name'
    bucket_prefix = 'your-s3-bucket-prefix'
    instance_type = 'ml.p3.2xlarge'
    num_layers = '18'
    learning_rate = '0.01'
    epochs = '30'

    # Update CloudFormation template
    update_cloudformation_template('template.json', 'new_template.json', bucket_name, bucket_prefix, instance_type, num_layers, learning_rate, epochs)

    # Update parameters file
    update_parameters_file('parameters.json', 'new_parameters.json', bucket_name, bucket_prefix, instance_type, num_layers, learning_rate, epochs)
