from peewee import *
from playhouse.shortcuts import ReconnectMixin


class ReconnectMySQLDatabase(ReconnectMixin, MySQLDatabase):
    pass


db = ReconnectMySQLDatabase(host='rm-uf664y8bsz73u37odio.mysql.rds.aliyuncs.com', user='luming', passwd='Luming1314',
                            database='jd_notes',
                            charset='utf8mb4', port=3306)


class BaseModel(Model):
    class Meta:
        database = db


class JD_CATEGORY(BaseModel):
    id = BigAutoField()
    sku = CharField(null=True)
    category = CharField(null=True)

    class Meta:
        table_name = 'jd_category'
