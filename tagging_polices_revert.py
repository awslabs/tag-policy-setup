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

cwd = os.getcwd()
policy_files = os.listdir(f'{cwd}/policies')

try:
    response = client.list_roots()
    root_id  = response['Roots'][0]['Id']

    list_policies = client.list_policies(
        Filter='TAG_POLICY'
        )

    for policy in list_policies['Policies']:
        Id = policy['Id']
        Name = policy['Name']

        if f"{Name}.json" in policy_files:
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


        # if accountid == None:
        #     TargetId = root_id
        # else: 
        #     TargetId = accountid
        
        # response = client.attach_policy(
        #     PolicyId=policy_id,
        #     TargetId=TargetId
        # )
        # print("Tag Policy Setup")
except Exception as e:
    print(e)
