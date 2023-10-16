import boto3
# creating session and printing session
session = boto3.session.Session()
print(session)
appflowClient = session.client("appflow")

#returns all available services of AWS account
services = session.get_available_services()
print(services)

# returns all available connectors associated with provided aws account
list_connectors_response = appflowClient.list_connectors(
    maxResults=100
)
print(list_connectors_response)
print('########################################################################')

# returns all available flow associated with this account
list_flows_response = appflowClient.list_flows(
    maxResults=100
)
print(list_flows_response)
