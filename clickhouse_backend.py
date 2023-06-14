from clickhouse_driver import Client
from creds import CH_USER, CH_PASS
import pandas as pd
from datetime import datetime


# Функция загрузки pd dataframe
def write_df_to_clickhouse(df, table):

   if len(table.split('.')) == 2:
       schema_name, table_name = table.split('.')
   elif len(table.split('.')) == 1:
       schema_name, table_name = 'default', table
   else:
       raise ValueError('invalid table name: {}'.format(table))

   client = Client(host='localhost:9000',
                                   user=CH_USER,
                                   password=CH_PASS,
                                   secure=True,
                                   settings={'use_numpy': True})

   client.execute(
       'truncate table {}.{}'.format(schema_name, table_name))
   client.insert_dataframe(
       'INSERT INTO {}.{} ({}) VALUES'.format(schema_name, table_name, ','.join(df.columns)), df)

# Функция загрузки pd dataframe
def get_from_clickhouse(table):

   if len(table.split('.')) == 2:
       schema_name, table_name = table.split('.')
   elif len(table.split('.')) == 1:
       schema_name, table_name = 'default', table
   else:
       raise ValueError('invalid table name: {}'.format(table))

   client = Client(host='localhost:9000',
                   user=CH_USER,
                   password=CH_PASS,
                   secure=True,
                   settings={'use_numpy': True})

   response = client.execute('select currency, balance from {}.{}'.format(schema_name, table_name))
   cols = ['currency', 'balance']
   out_df = pd.DataFrame(response, columns=cols)
   return out_df


# Функция обновления курса
# TODO Сделать полный апдейт текущего курса
def update_clickhouse(table, target):
    if len(table.split('.')) == 2:
        schema_name, table_name = table.split('.')
    elif len(table.split('.')) == 1:
        schema_name, table_name = 'default', table
    else:
        raise ValueError('invalid table name: {}'.format(table))

    client = Client(host='localhost:9000',
                    user=CH_USER,
                    password=CH_PASS,
                    secure=True,
                    settings={'use_numpy': True})

    client.execute('update {}.{} set load_dttm = {} where target = {}'.format(schema_name, table_name, datetime.now, target))