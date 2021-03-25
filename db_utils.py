from api import data_generator
import numpy as np
import datetime
import pymysql
from mlModel import extractFeatures, predictAction

select_all = '''select * from rawData; '''
add_row = ''' insert into rawData (timestamp, accelX, accelY, accelZ, gyroX, gyroY, gyroZ) values ("%s", %.4f, %.4f, %.4f, %.4f, %.4f, %.4f)'''
select_last_row = ''' select id, timestamp, mean, std from rawData order by id desc limit 1; '''


def update_db():
    conn = pymysql.connect(host="localhost", user="rawData_manager", password='password', database="CW")
    for samples in data_generator():
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")
        accelX = samples[0]
        accelY = samples[1]
        accelZ = samples[2]
        gyroX = samples[3]
        gyroY = samples[4]
        gyroZ = samples[5]
        with conn.cursor() as cursor:
            cursor.execute(add_row % (timestamp, accelX, accelY, accelZ, gyroX, gyroY, gyroZ))
        conn.commit()
        print("row added")
#        features = extractFeatures(raw)
        lastdata = np.random.random((10,6))
        pred = predictAction(lastdata)

def get_entire_table():
    conn = pymysql.connect(host="localhost", user="rawData_manager", password='password', database="CW")
    with conn.cursor() as cursor:
        cursor.execute(select_all)
        table = cursor.fetchall()
        print(table)
        return table

def get_last_ten_row():
    conn = pymysql.connect(host="localhost", user="rawData_manager", password='password', database="CW")
    with conn.cursor() as cursor:
        cursor.execute(select_last_row)
        row = cursor.fetchmany(10)
        print(row)
        return row

def get_latest_row():
    conn = pymysql.connect(host="localhost", user="rawData_manager", password='password', database="CW")
    with conn.cursor() as cursor:
        cursor.execute(select_last_row)
        row = cursor.fetchone()
        return row


if __name__ == "__main__":
    get_entire_table()
