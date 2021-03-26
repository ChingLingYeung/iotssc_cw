from api import get_resourceValues
import numpy as np
import datetime
import pymysql
from mlModel import predictAction

select_all = '''select * from rawData; '''
add_data_row = ''' insert into rawData (timestamp, accelX, accelY, accelZ, gyroX, gyroY, gyroZ) values ("%s", %.4f, %.4f, %.4f, %.4f, %.4f, %.4f)'''
add_row = ''' insert into rawData (timestamp, accelX, accelY, accelZ, gyroX, gyroY, gyroZ, classification) values ("%s", %.4f, %.4f, %.4f, %.4f, %.4f, %.4f, %d)'''
select_last_row = ''' select id, timestamp, accelX, accelY, accelZ, gyroX, gyroY, gyroZ, classification from rawData order by id desc limit 1; '''


def update_db():
    conn = pymysql.connect(host="localhost", user="rawData_manager", password='password', database="CW")
    for samples in get_resourceValues():
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")
        accelX = samples[0]
        accelY = samples[1]
        accelZ = samples[2]
        gyroX = samples[3]
        gyroY = samples[4]
        gyroZ = samples[5]

        pred = predictAction(get_entire_table())
        if pred is not None:
            with conn.cursor() as cursor:
                cursor.execute(add_row % (timestamp, accelX, accelY, accelZ, gyroX, gyroY, gyroZ, pred))
        else:
            with conn.cursor() as cursor:
                cursor.execute(add_data_row % (timestamp, accelX, accelY, accelZ, gyroX, gyroY, gyroZ))
        conn.commit()
        print("row added")

def get_entire_table():
    conn = pymysql.connect(host="localhost", user="rawData_manager", password='password', database="CW")
    with conn.cursor() as cursor:
        cursor.execute(select_all)
        table = cursor.fetchall()
        return table

def get_keys():
    conn = pymysql.connect(host="localhost", user="rawData_manager", password='password', database="CW")
    #get JSON keys
    keys = []
    with conn.cursor() as cursor:
        cursor.execute('''SHOW COLUMNS from rawData; ''')
        table = cursor.fetchall()
        for row in table:
            keys.append(row[0])
    return(keys)
        
def get_json_table(table):
    keys = get_keys()
    json_data = []
    # map keys and values
    for row in table:
        json_obj = get_json_row(row)
        json_data.append(json_obj)
    return json_data
    
def get_json_row(row):
    keys = get_keys()
    json_obj = {}
    if len(row) < len(keys):
        b = 'null'
        row = row + (b,)
    for i in range(len(keys)):
        json_obj[keys[i]] = row[i]
    return json_obj

    

def get_latest_row():
    conn = pymysql.connect(host="localhost", user="rawData_manager", password='password', database="CW")
    with conn.cursor() as cursor:
        cursor.execute(select_last_row)
        row = cursor.fetchone()
        return row


if __name__ == "__main__":
    get_entire_table()
