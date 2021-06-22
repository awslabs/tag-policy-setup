import botocore
import boto3
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--accountid')
args = parser.parse_args()

accountid = args.accountid

client = boto3.client('organizations')


response = client.list_roots()
root_id  = response['Roots'][0]['Id']

response = client.describe_organization()
Organization_Id =response['Organization']['Id']

try:
    response = client.enable_policy_type(
        RootId=root_id,
        PolicyType='SERVICE_CONTROL_POLICY'
    )
except botocore.exceptions.ClientError as error:
    print(error)

with open('scp_policies/scp.json', 'r') as file:
    data = file.read().replace('\n', '')
    try:
        response = client.create_policy(
            Content= data,
            Description='OPTICS SCP',
            Name='OPTICS_SCP',
            Type='SERVICE_CONTROL_POLICY',
            Tags=[
                {
                    'Key': 'Owner',
                    'Value': 'OPTICS'
                },
            ]
        )

        policy_id = response['Policy']['PolicySummary']['Id']

        if accountid == None:
            TargetId = root_id
        else: 
            TargetId = accountid

        response = client.attach_policy(
            PolicyId=policy_id,
            TargetId=TargetId
        )
        print("SCP Setup")
    except Exception as e:
            print(e)