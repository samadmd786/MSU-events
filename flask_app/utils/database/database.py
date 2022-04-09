from ast import Delete
import queue
from select import select
import mysql.connector
import glob
import json
import csv
from io import StringIO
import itertools
import datetime


class database:

    def __init__(self, purge=False):

        # Grab information from the configuration file
        self.database = 'db'
        self.host = '127.0.0.1'
        self.user = 'master'
        self.port = 3306
        self.password = 'master'

    def query(self, query="SELECT CURDATE()", parameters=None):

        cnx = mysql.connector.connect(host=self.host,
                                      user=self.user,
                                      password=self.password,
                                      port=self.port,
                                      database=self.database,
                                      charset='latin1'
                                      )

        if parameters is not None:
            cur = cnx.cursor(dictionary=True)
            cur.execute(query, parameters)
        else:
            cur = cnx.cursor(dictionary=True)
            cur.execute(query)

        # Fetch one result
        row = cur.fetchall()
        cnx.commit()

        if "INSERT" in query:
            cur.execute("SELECT LAST_INSERT_ID()")
            row = cur.fetchall()
            cnx.commit()
        cur.close()
        cnx.close()
        return row

    def about(self, nested=False):
        query = """select concat(col.table_schema, '.', col.table_name) as 'table',
                          col.column_name                               as column_name,
                          col.column_key                                as is_key,
                          col.column_comment                            as column_comment,
                          kcu.referenced_column_name                    as fk_column_name,
                          kcu.referenced_table_name                     as fk_table_name
                    from information_schema.columns col
                    join information_schema.tables tab on col.table_schema = tab.table_schema and col.table_name = tab.table_name
                    left join information_schema.key_column_usage kcu on col.table_schema = kcu.table_schema
                                                                     and col.table_name = kcu.table_name
                                                                     and col.column_name = kcu.column_name
                                                                     and kcu.referenced_table_schema is not null
                    where col.table_schema not in('information_schema','sys', 'mysql', 'performance_schema')
                                              and tab.table_type = 'BASE TABLE'
                    order by col.table_schema, col.table_name, col.ordinal_position;"""
        results = self.query(query)
        if nested == False:
            return results

        table_info = {}
        for row in results:
            table_info[row['table']] = {} if table_info.get(
                row['table']) is None else table_info[row['table']]
            table_info[row['table']][row['column_name']] = {} if table_info.get(row['table']).get(
                row['column_name']) is None else table_info[row['table']][row['column_name']]
            table_info[row['table']][row['column_name']
                                     ]['column_comment'] = row['column_comment']
            table_info[row['table']][row['column_name']
                                     ]['fk_column_name'] = row['fk_column_name']
            table_info[row['table']][row['column_name']
                                     ]['fk_table_name'] = row['fk_table_name']
            table_info[row['table']][row['column_name']
                                     ]['is_key'] = row['is_key']
            table_info[row['table']][row['column_name']
                                     ]['table'] = row['table']
        return table_info

    def createTables(self, purge=False, data_path='flask_app/database/'):
        # print('I create and populate database tables.')
        table = ["club","professional","community","entertainment"]
        # for i in table:
        self.query("DROP table IF EXISTS clubs")
        self.query("DROP table IF EXISTS professional")
        self.query("DROP table IF EXISTS community")
        self.query("DROP table IF EXISTS entertainment")


        query = open(data_path+"create_tables/club.sql")
        file = query.read()
        self.query(file)

        file = open(data_path+"initial_data/club.csv")
        csv_file = csv.reader(file)
        next(csv_file, None)
        for i in csv_file:
            self.insertRows("clubs", [
                            "club_id","type","name","eventName","start_date","address","city","state","zip"], i)

        query = open(data_path+"create_tables/professional.sql")
        file = query.read()
        self.query(file)

        file = open(data_path+"initial_data/professional.csv")
        csv_file = csv.reader(file)
        next(csv_file, None)
        for i in csv_file:
            self.insertRows("professional", [
                            "professional_id","type","name","eventName","start_date","address","city","state","zip"], i)

        query = open(data_path+"create_tables/community.sql")
        file = query.read()
        self.query(file)

        file = open(data_path+"initial_data/community.csv")
        csv_file = csv.reader(file)
        next(csv_file, None)
        for i in csv_file:
            self.insertRows("community", [
                            "community_id","type","name","eventName","start_date","address","city","state","zip"], i)

        query = open(data_path+"create_tables/entertainment.sql")
        file = query.read()
        self.query(file)

        file = open(data_path+"initial_data/entertainment.csv")
        csv_file = csv.reader(file)
        next(csv_file, None)
        for i in csv_file:
            self.insertRows("entertainment", [
                            "entertainment_id","type","name","eventName","start_date","address","city","state","zip"], i)

       
    def insertRows(self, table='table', columns=['x', 'y'], parameters=[['v11', 'v12'], ['v21', 'v22']]):
        column = " ".join(columns)
        column = column.replace(' ', ",")
        values = ''
        for i in parameters:
            values += "'"+i+"'"+','
        values = values.rstrip(',')
        query = f"""INSERT  INTO {table} ({column}) VALUES ({values}) """
        # print(query)
        self.query(query) 
    
    def getData(self,table):
        instQuery = self.query(f"""SELECT * from {table};""")
        lis = []
        for row in instQuery:
            
            lis.append(row)
        return row

            