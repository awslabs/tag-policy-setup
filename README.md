# Tags

## Tagging Polices

In the Polices folder there are a set of pre-made polices that can be used or edited to setup a tag policy.

### Setup
Using the below command you can setup these policies on a specific account
```python3 tagging_polices_setup.py  --accountid 123456789```

If you wish to set these up on your root then run
```python3 tagging_polices_setup.py```

### Revert
Using the below command you can revert these policies on a specific account and delete them
```python3 tagging_polices_revert.py  --accountid 123456789```

If you wish to remove these from your root then delete them
```python3 tagging_polices_revert.py```

## SCP 
### Setup
In the folder there is a pre-made SCP that can be used or edited.

Using the below command you can setup these policies on a specific account
```python3 scp_setup.py  --accountid 123456789```

If you wish to set these up on your root then run
```python3 scp_setup.py```

### Revert
Using the below command you can revert these policies on a specific account and delete them
```python3 scp_setup_revert.py  --accountid 123456789```

If you wish to remove these from your root then delete them
```python3 scp_setup_revert.py```



### Tagging Polices Support Infomation
https://docs.aws.amazon.com/organizations/latest/userguide/tag-policy-cli.html
https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_example-tag-policies.html
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Client.list_roots

aws organizations disable-policy-type --policy-type 'TAG_POLICY' --root-id 'r-rlg9'
aws organizations list-policies  --filter 'TAG_POLICY'

Applicaion, Env, Buisness Unit

{
    "tags": {
        "costcenter": { -- policy key 
            "tag_key": {
                "@@assign": "CostCenter", -- must be the same as policy key but this is case sensitive. @@assign – Overwrites any inherited policy settings with the specified settings
                "@@operators_allowed_for_child_policies": ["@@none"] -- Tag policies that are attached lower in the organization tree (child policies) can't use value-setting operators to change the tag key
            },
            "tag_value": {
                "@@assign": [ --if not specified a tag value for a tag key, any value (including no value at all) is considered compliant
                    "100",
                    "200"
                ]
            },
            "enforced_for": { -- prevents any noncompliant tagging operations for services. You can't use a wildcard to specify all services or to specify a resource for all services.
                "@@assign": [
                    "secretsmanager:*"
                ]
            }
        },
        "Color": {
            "tag_key": {
                "@@operators_allowed_for_child_policies": [
                    "@@none"
                ],
                "@@assign": "Color"
            },
            "tag_value": {
                "@@operators_allowed_for_child_policies": [
                    "@@none"
                ],
                "@@assign": [] -- any Color tags on resources in affected accounts are considered non-compliant.
            }
        }
    }
}


*Config Rule*

http://s3.amazonaws.com/aws-configservice-us-east-1/cloudformation-templates-for-managed-rules/REQUIRED_TAGS.template

AWS CLI to deploy cf 
aws cloudformation create-stack --stack-name ConfigTagRule --template-body file://config_rule.json --region eu-west-1 --capabilities CAPABILITY_NAMED_IAM

*reource_tagging*

cloned from git@github.com:aws-samples/resource-auto-tagger.git 
https://aws.amazon.com/blogs/mt/auto-tag-aws-resources/

Must make sure to change name and region.
Also place code in bucket when deploying the lambda

## Security

See [CONTRIBUTING](CONTRIBUTING.md#security-issue-notifications) for more information.

## License

This library is licensed under the MIT-0 License. See the LICENSE file.

