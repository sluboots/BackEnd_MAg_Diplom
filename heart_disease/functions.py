from sklearn.preprocessing import StandardScaler as ss
import joblib
import numpy as np

def classification_heart_disease(data):
    model = joblib.load('D:\Mag_Diplom\heart_disease\ML_Models\SVC_HearDisease_Model.pkl')
    sc = joblib.load('D:\Mag_Diplom\heart_disease\ML_Models\SVC_SS.bin')
    arr = np.fromiter(data.values(), dtype=float)
    arr = sc.transform(arr.reshape(1, -1))
    rlt = model.predict(arr)
    return rlt[-1]





