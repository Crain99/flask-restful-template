#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# standard python imports

mssql = {'host': 'dbhost',
         'user': 'dbuser',
         'passwd': 'dbPwd',
         'db': 'db'}

postgresql = {'host': '0.0.0.0',
              'user': 'postgres',
              'passwd': 'magical_password',
              'db': 'db'}

mysql = {'host': '127.0.0.1',
         'user': 'root',
         'passwd': '123456',
         'port': '3306',
         'db': 'test'}

mssqlConfig = "mssql+pyodbc://{}:{}@{}:1433/{}?driver=SQL+Server+Native+Client+10.0".format(mssql['user'],
                                                                                            mssql['passwd'],
                                                                                            mssql['host'], mssql['db'])
postgresqlConfig = "postgresql+psycopg2://{}:{}@{}/{}".format(postgresql['user'], postgresql['passwd'],
                                                              postgresql['host'], postgresql['db'])
mysqlConfig = "mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8mb4".format(mysql['user'], mysql['passwd'], mysql['host'],
                                                                      mysql['port'],
                                                                      mysql['db'])
