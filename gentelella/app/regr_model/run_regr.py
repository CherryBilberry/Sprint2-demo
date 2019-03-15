import pickle
import numpy as np
import pandas as pd



'''
value                         277.0
num_docs                      527.0
size_comp                     336.0
revenue                    136441.0
industry_Banking                0.0
industry_Communication          0.0
industry_Health                 0.0
industry_Manufacturing          0.0
industry_Tech                   1.0
ju_Multiple                     0.0
ju_US                           1.0
dr_Red Flag                     1.0
ts_Earnout                      0.0
ts_Escrow                       0.0
ts_Gross-up                     0.0
ts_Not Sure                     0.0
ts_Options to Employees         1.0
'''


def predict(params_dict):
    value = params_dict['value']
    num_docs = params_dict['num_docs']
    size_comp = params_dict['size_comp']

    revenue = params_dict['revenue']
    industry = params_dict['industry']
    dr = params_dict['dr']
    ts = params_dict['ts']
    ju = params_dict['ju']


    x = np.zeros(17)
    x[0] = float(value)
    x[1] = float(num_docs)
    x[2] = float(size_comp)
    x[3] = float(revenue)


    x[int(industry) + 4] = 1

    x[int(ju) + 9] = 1
    x[int(dr) + 10] = 1
    x[int(ts) + 12] = 1

    x_test = x
    with open("./app/regr_model/regrmodel.pickle", 'rb') as f:
        regr = pickle.load(f)

    y_pred = regr.predict(np.array(x_test).reshape(1, -1))

    return y_pred

# params_dict = {
#
# 'value':                       96.0,
# 'num_docs':                    615.0,
# 'size_comp':                   792.0,
# 'revenue'  :                  6136.0,
# 'industry' : 2,
# 'ju' : 1,
# 'dr' : 0,
# 'ts' : 2
#
# }
#
# print (predict(params_dict))