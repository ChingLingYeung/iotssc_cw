package com.example.iotsscapp;

public class Sample {
    private int id;
    private String timestamp;
    private float accelX;
    private float accelY;
    private float accelZ;
    private float gyroX;
    private float gyroY;
    private float gyroZ;
    private int classification;
    private int trueClass;

    public int getId() { return id; }
    public String getTimestamp() {
        return timestamp;
    }
    public float getAccelX() {
        return accelX;
    }
    public float getAccelY() {
        return accelY;
    }
    public float getAccelZ() {
        return accelZ;
    }
    public float getGyroX() {
        return gyroX;
    }
    public float getGyroY() {
        return gyroY;
    }
    public float getGyroZ() {
        return gyroZ;
    }
    public int getClassification() { return classification; }
    public int getTrueClass() {
        return trueClass;
    }

}