
OPTICS Tag and Service Control Policy (SCP) Demo

Summary
The OPTICS Tag and SCP Policy Demo is a python script that deploys commonly used Tag and Service Control Policies to your account. This is a quick and easy way to understand the impact of a Tag and/or Service Control Policy on existing and newly created resources in your account. The Tag and SCP Demo is intended to be a learning tool, and it is strongly recommended that you deploy it in a development or sandbox account.

Demo Policies

Tag Policy
The Tag Policy deployed into your account will create the following tag policies:

  Business Unit – requires the “Business Unit” tag key on any newly created resources
	Cost Center – requires the “CostCenter” tag key on any newly created resources
  Environment – requires the “Environment” tag key and tag values of either “Prod”, “Dev”, “Test”, “UAT”, “Pre-Prod” on any newly created resources
  Owner – requires the “Owner” tag key on any newly created resource
  Project – requires the “Project” tag key on any newly created resource

Service Control Policy
The Service Control Policy will prevent the ec2:RunInstances command (Launching a new instance) on any newly created EC2 that does not have either a Project or Cost Center tag.

Instructions

In the Polices folder there are a set of pre-made polices that can be used or edited to setup a tag policy.

Using the below command you can setup these policies on a specific account
```python3 tagging_polices_setup.py  --accountid 123456789```

If you wish to set these up on your root then run
```python3 tagging_polices_setup.py```

## SCP Setup

In the folder there is a pre-made SCP that can be used or edited.

Using the below command you can setup these policies on a specific account
```python3 scp_setup.py  --accountid 123456789```

If you wish to set these up on your root then run
```python3 scp_setup.py```

Required Permissions
organizations:ListRoots
organizations:DescribeOrganization
organizations:EnablePolicyType
organizations:CreatePolicy
organizations:AttachPolicy


Tagging Polices Support Information
https://docs.aws.amazon.com/organizations/latest/userguide/tag-policy-cli.html
https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_example-tag-policies.html
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Client.list_roots
