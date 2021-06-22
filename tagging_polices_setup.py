import boto3
import os
import json
import argparse
from botocore.exceptions import ClientError
from botocore.client import Config



parser = argparse.ArgumentParser()
parser.add_argument('--accountid')
args = parser.parse_args()

accountid = args.accountid

client = boto3.client('organizations')

try:
    response = client.list_roots()
    root_id  = response['Roots'][0]['Id']

    response = client.describe_organization()
    Organization_Id =response['Organization']['Id']

    response = client.enable_policy_type(
        RootId=root_id,
        PolicyType='TAG_POLICY'
    )
except Exception as e:
        print(e)

cwd = os.getcwd()
policy_files = os.listdir(f'{cwd}/policies')

for policy in policy_files:
    name = policy.replace('.json','')
    print(name)

    with open(f'{cwd}/policies/{policy}', 'r') as file:
        data = file.read().replace('\n', '')
        data = data.replace(' ', '')
        try:
            response = client.create_policy(
                Content= data,
                Description=f'OPTICS Tagging Policy for {name}',
                Name=f'{name}',
                Type='TAG_POLICY',
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
            print("Tag Policy Setup")
        except Exception as e:
            print(e)
