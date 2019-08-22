from troposphere.dynamodb import Table, KeySchema, \
    AttributeDefinition, ProvisionedThroughput


def create_dynamo_db():
    dynamo_db = Table('LogTable',
                      TableName='LogTable',
                      AttributeDefinitions=[AttributeDefinition(
                          AttributeName='request_id',
                          AttributeType='S')],
                      KeySchema=[KeySchema(AttributeName='request_id',
                                           KeyType='HASH')],
                      ProvisionedThroughput=ProvisionedThroughput(
                          ReadCapacityUnits=5,
                          WriteCapacityUnits=5))
    return dynamo_db
