{
	"Version": "2012-10-17",
	"Statement": [
		{
			"Sid": "Statement1",
			"Effect": "Deny",
			"Action": [
				"ec2:PurchaseReservedInstancesOffering",
				"savingsplans:CreateSavingsPlan",
				"rds:PurchaseReservedDBInstancesOffering",
				"elasticache:PurchaseReservedCacheNodesOffering",
				"dynamodb:PurchaseReservedCapacityOfferings",
				"redshift:PurchaseReservedNodeOffering"
			],
			"Resource": ["*"]
		}
	]
}