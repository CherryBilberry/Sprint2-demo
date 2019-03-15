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
    y_pred = y_pred.flatten()
    y_pred = np.abs(y_pred)
    pl_sum = y_pred[0] + y_pred[9] + y_pred[11] + y_pred[16] + y_pred[20]
    ja_sum = y_pred[1] + y_pred[5] + y_pred[12] + y_pred[17] + y_pred[21]
    sa_sum = y_pred[2] + y_pred[7] + y_pred[13] + y_pred[17] + y_pred[22]
    pa_sum = y_pred[3] + y_pred[8] + y_pred[14] + y_pred[18] + y_pred[23]
    partner_sum = y_pred[4] + y_pred[10] + y_pred[15] + y_pred[19] + y_pred[24]

    cost = pl_sum * 100 + ja_sum * 200 + sa_sum * 350 + pa_sum * 450 + partner_sum * 800

    result = {'pl_sum' : int(pl_sum),
              'ja_sum': int(ja_sum),
              'sa_sum': int(sa_sum),
              'pa_sum': int(pa_sum),
              'partner_sum': int(partner_sum),
              'cost' : int(cost),
              'raw': [int(n) for n in y_pred] }

    print (y_pred)

    return result

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