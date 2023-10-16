from datetime import datetime

import boto3

#ACCESS_KEY_ID = 'AKIA4F52A4XR6Q5UXD55'
#SECRET_KEY = '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'

session = boto3.session.Session()#(aws_access_key_id=ACCESS_KEY_ID, aws_secret_access_key=SECRET_KEY,region_name='ap-south-1')
appflowClient = session.client("appflow")

# create flow
create_flow_response = appflowClient.create_flow(
        flowName='Business-Process_Types',
        description='creation of flow from boto3',
        triggerConfig={
            'triggerType': 'OnDemand'
        },
        sourceFlowConfig={
            'connectorType': 'CustomConnector',
            'apiVersion': 'v1',
            'connectorProfileName': 'WorkdayFunction',
            'sourceConnectorProperties': {
                'CustomConnector': {
                    'entityName': 'Business Process_Types'
                }
            }
        },
        destinationFlowConfigList=[
            {
                'connectorType': 'S3',
                'apiVersion': 'v1',
                'destinationConnectorProperties': {
                    'S3': {
                        'bucketName': 'appflow-connectors-data',
                        'bucketPrefix': 'BOTO3_WORKDAY_FLOW',
                        's3OutputFormatConfig': {
                            'fileType': 'JSON'
                        }
                    }
                }
            },
        ],
        tasks=[
            {
                'sourceFields': [
                ],
                'connectorOperator': {
                    'S3': 'EQUAL_TO'
                },
                'destinationField': 'string',
                'taskType': 'Map_all',
                'taskProperties': {
                }
            },
        ]
)
# run flow
if create_flow_response["ResponseMetadata"]["HTTPStatusCode"] == 200:
    execute_flow_response = appflowClient.start_flow(
        flowName='Business-Process_Types'
    )
print(execute_flow_response)
