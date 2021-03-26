import numpy as np
from sklearn import tree
from sklearn.model_selection import train_test_split

# ============== initial model training =========================
# read in the .dat file as list of list
raw_data_lst = [i.strip().split(",") for i in open("./dataset.csv").readlines()]
# raw_data_lst

# start after 10 samples
X = []
Y = []
for i in range(10, len(raw_data_lst)):
#    print(i, raw_data_lst[i])
    accel_x_lst = []
    accel_y_lst = []
    accel_z_lst = []
    gyro_x_lst = []
    gyro_y_lst = []
    gyro_z_lst = []
    for j in range(10):
        idx = i-9+j
        accel_x_lst.append(raw_data_lst[idx][5])
        accel_y_lst.append(raw_data_lst[idx][6])
        accel_z_lst.append(raw_data_lst[idx][7])
        gyro_x_lst.append(raw_data_lst[idx][8])
        gyro_y_lst.append(raw_data_lst[idx][9])
        gyro_z_lst.append(raw_data_lst[idx][10])
    accel_x_lst = np.array(accel_x_lst).astype(float)
    accel_y_lst = np.array(accel_y_lst).astype(float)
    accel_z_lst = np.array(accel_z_lst).astype(float)
    gyro_x_lst = np.array(accel_x_lst).astype(float)
    gyro_y_lst = np.array(accel_y_lst).astype(float)
    gyro_z_lst = np.array(accel_z_lst).astype(float)
    
    #extract features
    accel_x_mean = np.mean(accel_x_lst)
    accel_y_mean = np.mean(accel_y_lst)
    accel_z_mean = np.mean(accel_z_lst)
    gyro_x_mean = np.mean(gyro_x_lst)
    gyro_y_mean = np.mean(gyro_y_lst)
    gyro_z_mean = np.mean(gyro_z_lst)
    
    accel_x_var = np.var(accel_x_lst)
    accel_y_var = np.var(accel_y_lst)
    accel_z_var = np.var(accel_z_lst)
    gyro_x_var = np.var(gyro_x_lst)
    gyro_y_var = np.var(gyro_y_lst)
    gyro_z_var = np.var(gyro_z_lst)
    
    accel_xy_corr = np.correlate(accel_x_lst, accel_y_lst)
    accel_yz_corr = np.correlate(accel_y_lst, accel_z_lst)
    accel_xz_corr = np.correlate(accel_x_lst, accel_z_lst)
    gyro_xy_corr = np.correlate(gyro_x_lst, gyro_y_lst)
    gyro_yz_corr = np.correlate(gyro_y_lst, gyro_z_lst)
    gyro_xz_corr = np.correlate(gyro_x_lst, gyro_z_lst)
    
    x_data = [accel_x_mean, accel_y_mean, accel_z_mean,gyro_x_mean, gyro_y_mean, gyro_z_mean, accel_x_var, accel_y_var, accel_z_var, gyro_x_var, gyro_y_var, gyro_z_var,
               accel_xy_corr, accel_yz_corr, accel_xz_corr, gyro_xy_corr, gyro_yz_corr, gyro_xz_corr]
    y_label = raw_data_lst[i][4]
    X.append(x_data)
    Y.append(y_label)

#train test split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.5, random_state=100)
# X_test = np.array(X_test)
# print(X_test.shape)

clf = tree.DecisionTreeClassifier()
clf = clf.fit(X_train, Y_train)

#====================================================

def extractFeatures(data):
    accel_x_lst = []
    accel_y_lst = []
    accel_z_lst = []
    gyro_x_lst = []
    gyro_y_lst = []
    gyro_z_lst = []
    for i in range(10):
        for j in range(2, 8):
            accel_x_lst.append(data[i][j])
            accel_y_lst.append(data[i][j])
            accel_z_lst.append(data[i][j])
            gyro_x_lst.append(data[i][j])
            gyro_y_lst.append(data[i][j])
            gyro_z_lst.append(data[i][j])
    accel_x_lst = np.array(accel_x_lst).astype(float)
    accel_y_lst = np.array(accel_y_lst).astype(float)
    accel_z_lst = np.array(accel_z_lst).astype(float)
    gyro_x_lst = np.array(accel_x_lst).astype(float)
    gyro_y_lst = np.array(accel_y_lst).astype(float)
    gyro_z_lst = np.array(accel_z_lst).astype(float)
    
    #extract features
    accel_x_mean = np.mean(accel_x_lst)
    accel_y_mean = np.mean(accel_y_lst)
    accel_z_mean = np.mean(accel_z_lst)
    gyro_x_mean = np.mean(gyro_x_lst)
    gyro_y_mean = np.mean(gyro_y_lst)
    gyro_z_mean = np.mean(gyro_z_lst)
    
    accel_x_var = np.var(accel_x_lst)
    accel_y_var = np.var(accel_y_lst)
    accel_z_var = np.var(accel_z_lst)
    gyro_x_var = np.var(gyro_x_lst)
    gyro_y_var = np.var(gyro_y_lst)
    gyro_z_var = np.var(gyro_z_lst)
    
    accel_xy_corr = np.correlate(accel_x_lst, accel_y_lst)[0]
    accel_yz_corr = np.correlate(accel_y_lst, accel_z_lst)[0]
    accel_xz_corr = np.correlate(accel_x_lst, accel_z_lst)[0]
    gyro_xy_corr = np.correlate(gyro_x_lst, gyro_y_lst)[0]
    gyro_yz_corr = np.correlate(gyro_y_lst, gyro_z_lst)[0]
    gyro_xz_corr = np.correlate(gyro_x_lst, gyro_z_lst)[0]
    
    x_data = [accel_x_mean, accel_y_mean, accel_z_mean,gyro_x_mean, gyro_y_mean, gyro_z_mean, accel_x_var, accel_y_var, accel_z_var, gyro_x_var, gyro_y_var, gyro_z_var,
            accel_xy_corr, accel_yz_corr, accel_xz_corr, gyro_xy_corr, gyro_yz_corr, gyro_xz_corr]
    # y_label = data[i][4]
    X.append(x_data)
    return(x_data)
    # Y.append(y_label)


def predictAction(data):
    if len(data) < 10:
        return
    data = data[-10:]
    features = np.array(extractFeatures(data))
    # print(features)
    pred = clf.predict(features.reshape(1, -1))
    return(pred)
