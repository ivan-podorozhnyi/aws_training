from troposphere import Ref
from troposphere.rds import DBInstance


def create_rds_db(db_name, db_user, db_password):
    db = DBInstance('Database',
                    DBInstanceClass='db.t2.micro',
                    Engine='MySQL',
                    AllocatedStorage="5",
                    DBName=Ref(db_name),
                    MasterUsername=Ref(db_user),
                    MasterUserPassword=Ref(db_password))
    return db
