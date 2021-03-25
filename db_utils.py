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

def get_last_ten_row():
    conn = pymysql.connect(host="localhost", user="rawData_manager", password='password', database="CW")
    with conn.cursor() as cursor:
        cursor.execute(select_last_row)
        row = cursor.fetchmany(10)
        return row

def get_latest_row():
    conn = pymysql.connect(host="localhost", user="rawData_manager", password='password', database="CW")
    with conn.cursor() as cursor:
        cursor.execute(select_last_row)
        row = cursor.fetchone()
        return row


if __name__ == "__main__":
    get_entire_table()
