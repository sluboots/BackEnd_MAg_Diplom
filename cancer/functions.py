import joblib
import numpy as np

def classification_cancer(data):
    model_Schiller = joblib.load('D:\Mag_Diplom\cancer\ML_Models\SVC_HearDisease_Model_Schiller.pkl')
    model_Hinselmann = joblib.load('D:\Mag_Diplom\cancer\ML_Models\SVC_HearDisease_Model_Hinselmann.pkl')
    model_Citology = joblib.load('D:\Mag_Diplom\cancer\ML_Models\SVC_HearDisease_Model_Citology.pkl')
    model_Biopsy = joblib.load('D:\Mag_Diplom\cancer\ML_Models\SVC_HearDisease_Model_Biopsy.pkl')
    arr = np.fromiter(data.values(), dtype=float)
    rlt_1 = model_Schiller.predict(arr.reshape(1, -1))
    rlt_2 = model_Hinselmann.predict(arr.reshape(1, -1))
    rlt_3 = model_Citology.predict(arr.reshape(1, -1))
    rlt_4 = model_Biopsy.predict(arr.reshape(1, -1))
    return rlt_1[-1],rlt_2[-1],rlt_3[-1],rlt_4[-1]
