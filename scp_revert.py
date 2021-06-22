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
    list_policies = client.list_policies(
            Filter='SERVICE_CONTROL_POLICY'
            )
    for policy in list_policies['Policies']:
            Id = policy['Id']
            Name = policy['Name']

            if Name =='OPTICS_SCP':
                print(policy)
                if accountid == None:
                    TargetId = root_id
                else: 
                    TargetId = accountid

                try:
                    response = client.detach_policy(
                    PolicyId=Id,
                    TargetId=TargetId
                    )
                except Exception as e:
                    print(e)
                    pass
                try:
                    response = client.delete_policy(
                    PolicyId=Id
                    )
                except Exception as e:
                    print(e)
                    pass
                print("SCP Removed")
except Exception as e:
        print(e)