DB_VARS = {
    "DBName": "db_name",
    "DBInstanceIdentifier": "instance_name",
    "AllocatedStorage": 20,
    "DBInstanceClass": "db.m3.medium",
    "Engine": "postgres",
    "MasterUsername": "username",
    "MasterUserPassword": "password",
    "VpcSecurityGroupIds": [
        "sg-0007c6489efbd9bca",
    ],
    "DBSubnetGroupName": "my-subnet",
    "DBParameterGroupName": "my-parameter-group",
    "BackupRetentionPeriod": 7,
    "MultiAZ": True,
    "EngineVersion": "10.0.1",
    "PubliclyAccessible": False,
    "StorageType": "gp2",
}


def create_rds(bucket, db_vars=None):
    if db_vars is None:
        db_vars = DB_VARS
    bucket.create_db_instance(**db_vars)
