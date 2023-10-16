import boto3
import os
import configparser

#set environment
'''aws_access_key_value = input('Please enter access key value:\n')
os.environ['aws_access_key_id'] = aws_access_key_value

aws_secret_access_key_value = input('Please enter secret key value:\n')
os.environ['aws_secret_access_key'] = aws_secret_access_key_value

region_name_value = input('Please enter region value:\n')
os.environ['region_name'] = region_name_value'''

# creating session and printing
session = boto3.session.Session(aws_access_key_id='AKIARNIMKT2N5ZCGB2ON', aws_secret_access_key='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',region_name='ap-south-1')


appflowclient = session.client("appflow")

# Registers new connector with AWS accountAKIARNIMKT2N5ZCGB2ON
response = appflowclient.register_connector(
    connectorLabel='Botoconnector',
    description='custom connector using Boto3',
    connectorProvisioningType='LAMBDA',
    connectorProvisioningConfig={
        'lambda': {
            'lambdaArn': 'arn:aws:lambda:ap-south-1:097199496859:function:botofilter'
        }
    }
)
print('Successfully registered the connector', response)
#describing connector

# creates connection used to create and run flows
if(response["ResponseMetadata"]["HTTPStatusCode"] == 200):
    connector_response = appflowclient.create_connector_profile(
    connectorProfileName='Botoconnection',
    #kmsArn = 'string'
    connectorType='CustomConnector',
    connectorLabel='Botoconnector',
    connectionMode='Public',
    connectorProfileConfig={
        'connectorProfileProperties': {
            'CustomConnector': {
                'profileProperties': {
                    #'string':'string'
                    'BASE_URL': 'https://wd2-impl-services1.workday.com/ccx',
                    'INSTANCE_ID': 'peopletech_gms1',
                   # 'REFRESH_TOKEN':'grant_type=refresh_token&refresh_token=l5zho8henuwyb0qwj6broipqdca4rgl1av46so96a3snkkrjogm1fy4xnuvyz5imimmwxngw1ovh4a1696mq7u77qbuj26a8q77',
                  #  'REFRESH_TOKEN_URL':'https://wd2-impl-services1.workday.com/ccx/oauth2/peopletech_gms1/token',
                    #'CUSTOMFILTER':'Customfilter'

                },
               # 'oAuth2Properties': {
                #    'tokenUrl': 'string',
                #    'oAuth2GrantType': 'CLIENT_CREDENTIALS' | 'AUTHORIZATION_CODE',
                 #   'tokenUrlCustomProperties': {
                  #      'string': 'string'
            }
        },
        'connectorProfileCredentials': {
            'CustomConnector': {
                'authenticationType': 'BASIC',
                'basic': {
                    'username': 'ZTgxODM3ZjItYTkzNy00MGJmLWE2OWEtZDVmZDI5ODVjZWRk',
                    'password': '1jirh0w5tgikpqkoodf83fsuyki17ypr5deqe9wsu9wz5xbfav29wcap5tj3wnhh4wq658ojspuwkutzprdhlwoggdn3gdp81bt'
                }
            }
        }
    }
)

    print('Successfully authenticated the client', connector_response)


# creates connection used to create and run flows
#if(connector_response["ResponseMetadata"]["HTTPStatusCode"] == 200):
config = configparser.RawConfigParser()
config.read('flowNames.properties')
for each_section in config.sections():

  for (each_key, each_val) in config.items(each_section):
            print('key', each_key)
            print('value', each_val)
            print(each_section)
create_flow_response = appflowclient.create_flow(
            flowName=each_key,
            description='creation of flow from boto3',
            triggerConfig={
                'triggerType': 'OnDemand'
            },
            sourceFlowConfig={
                'connectorType': 'CustomConnector',
                'apiVersion': 'v1',
                'connectorProfileName': 'Botoconnection',
                'sourceConnectorProperties': {
                    'CustomConnector': {
                        'entityName': each_val,
                        'customProperties': {
                           #'CustomFilter':'true',
                            #'FilterType':'Expression',
                           # 'Fieldname':'id',
                           ##'Value':'70b12b833c4e01060d6725fd5b0b0000'


                          # 'FilterExpression':'descriptor=="toronto"',

                             #  'filterType':'Conditional',
                              # 'fieldName': 'id',
                            # 'operator': 'EqualTo',
                                 # 'value': '70b12b833c4e01060d6725fd5b0b0000'

}
                        }

                    }

            },
            destinationFlowConfigList=[
                {
                    'connectorType': 'S3',
                    'apiVersion': 'v1',
                    'connectorProfileName': 'Botoconnection',
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

                    'destinationField': 'string',
                    'taskType': 'Map_all',
                    'taskProperties': {

                    }

                }

            ]
)


#run flow
if create_flow_response["ResponseMetadata"]["HTTPStatusCode"] == 200:
    config = configparser.RawConfigParser()
    config.read('flowNames.properties')
    for each_section in config.sections():
        for (each_key, each_val) in config.items(each_section):
            execute_flow_response = appflowclient.start_flow(
                flowName=each_key
            )
        print('Successfully executed flow', execute_flow_response)

#delete flow
'''if execute_flow_response["ResponseMetadata"]["HTTPStatusCode"] == 200:
    config = configparser.RawConfigParser()
    config.read('flowNames.properties')
    for each_section in config.sections():
        for (each_key, each_val) in config.items(each_section):
            delete_flow_response = appflowclient.delete_flow(
                flowName=each_key,
                forceDelete=True
            )
    print('Successfully deleted flow',delete_flow_response)

if delete_flow_response["ResponseMetadata"]["HTTPStatusCode"] == 200:
    delete_connection = appflowclient.delete_connector_profile(
    connectorProfileName='Botoconnection',
    forceDelete=True
    )
    print('Successfully deleted the connection ',delete_connection)

if delete_connection["ResponseMetadata"]["HTTPStatusCode"] == 200:
    unregister_connector = appflowclient.unregister_connector(
    connectorLabel='Botoconnector',
    forceDelete=True
    )
    print('Successfully unregistered the connector ',unregister_connector)'''