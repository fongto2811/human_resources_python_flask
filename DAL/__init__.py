import cx_Oracle as db
from DAL import config
from flask import session
from datetime import datetime

dsn = db.makedsn(host=config.ORACLE_HOST, port=config.ORACLE_PORT,
                 service_name=config.ORACLE_SERVICENAME)
