create database if not exists CW;
use CW;

drop table if exists rawData;
create table rawData(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    timestamp varchar(255),
    accelX float(6, 2),
    accelY float(6, 2),
    accelZ float(6, 2),
    gyroX float(6, 2),
    gyroY float(6, 2),
    gyroZ float(6, 2),
    classification INT
);

create user 'rawData_manager'@'localhost' identified by 'password';
grant select, update, insert, delete on CW.rawData to 'rawData_manager'@'localhost';
