import numpy as np
import pandas as pd
from random import randint
from sklearn import linear_model
from sklearn.metrics import mean_squared_error



B = 10000


value = np.zeros(B)
for i in range(B):
    value[i] = randint(50, 300)


dd_rev_paralegal = np.zeros(B)
dd_rev_ja = np.zeros(B)
dd_rev_sa = np.zeros(B)
dd_rev_pa = np.zeros(B)
dd_rev_partner = np.zeros(B)
for i in range(B):
    dd_rev_paralegal[i] = randint(50, 300)
    dd_rev_ja[i] = randint(50, 300)
    dd_rev_sa[i] = randint(0, 150)
    dd_rev_pa[i] = randint(0, 50)
    dd_rev_partner[i] = randint(0, 20)

dd_rep_paralegal = np.zeros(B)
dd_rep_ja = np.zeros(B)
dd_rep_sa = np.zeros(B)
dd_rep_pa = np.zeros(B)
dd_rep_partner = np.zeros(B)
fluc = np.array([0, 0.3, 0.8, 1, -0.7, -0.4, -0.1])
for i in range(B):
    a = 50
    b = 300
    c = 50
    d = 100
    temp = int((dd_rev_ja[i] - a) / (b - a) * (d - c) + c)
    dd_rep_ja[i] = temp
    a = 0
    b = 150
    c = 20
    d = 50
    temp = int((dd_rev_sa[i] - a) / (b - a) * (d - c) + c)
    dd_rep_sa[i] = temp
    a = 0
    b = 50
    c = 10
    d = 30
    temp = int((dd_rev_pa[i] - a) / (b - a) * (d - c) + c)
    dd_rep_pa[i] = temp
    a = 0
    b = 20
    c = 10
    d = 20
    temp = int((dd_rev_partner[i] - a) / (b - a) * (d - c) + c)
    dd_rep_partner[i] = temp

    p = 8
    dd_rep_ja[i] += int(np.random.choice(fluc) * p)
    if dd_rep_ja[i] < 50:
        dd_rep_ja[i] = 50
    if dd_rep_ja[i] > 100:
        dd_rep_ja[i] = 100
    p = 5
    dd_rep_sa[i] += int(np.random.choice(fluc) * p)
    if dd_rep_sa[i] < 20:
        dd_rep_sa[i] = 20
    if dd_rep_sa[i] > 50:
        dd_rep_sa[i] = 50
    p = 3
    dd_rep_pa[i] += int(np.random.choice(fluc) * p)
    if dd_rep_pa[i] < 10:
        dd_rep_pa[i] = 10
    if dd_rep_pa[i] > 30:
        dd_rep_pa[i] = 30
    p = 2
    dd_rep_partner[i] += int(np.random.choice(fluc) * p)
    if dd_rep_partner[i] < 10:
        dd_rep_partner[i] = 10
    if dd_rep_partner[i] > 20:
        dd_rep_partner[i] = 20



# DD_Research
dd_res_paralegal = np.zeros(B)
dd_res_ja = np.zeros(B)
dd_res_sa = np.zeros(B)
dd_res_pa = np.zeros(B)
dd_res_partner = np.zeros(B)
for i in range(B):
    dd_res_paralegal[i] = randint(20, 100)
    dd_res_ja[i] = randint(10, 80)
    dd_res_sa[i] = randint(0, 20)


# Transaction_Drafting
td_paralegal = np.zeros(B)
td_ja = np.zeros(B)
td_sa = np.zeros(B)
td_pa = np.zeros(B)
td_partner = np.zeros(B)
for i in range(B):
    td_ja[i] = randint(0, 100)
    td_sa[i] = randint(30, 100)
    td_pa[i] = randint(40, 150)
    td_partner[i] = randint(0, 100)


# Transaction_nondrafting
tn_paralegal = np.zeros(B)
tn_ja = np.zeros(B)
tn_sa = np.zeros(B)
tn_pa = np.zeros(B)
tn_partner = np.zeros(B)
for i in range(B):
    tn_ja[i] = randint(40, 80)
    tn_sa[i] = randint(40, 150)
    tn_pa[i] = randint(40, 150)
    tn_partner[i] = randint(20, 100)


# Number of documents
# It is positively correlated with DD_review and DD_report
num_docs = np.zeros(B)
for i in range(B):
    a = 100
    b = 820
    c = 500
    d = 700
    dd_rev_sum = dd_rev_paralegal[i] + dd_rev_ja[i] + dd_rev_sa[i] + dd_rev_pa[i] + dd_rev_partner[i]
    num_docs[i] = int((dd_rev_sum - a) / (b - a) * (d - c) + c)
    p = 20
    num_docs[i] += int(np.random.choice(fluc) * p)
    if num_docs[i] < 500:
        num_docs[i] = 500
    if num_docs[i] > 700:
        num_docs[i] = 700


# Size of company
size_comp = np.zeros(B)
for i in range(B):
    size_comp[i] = randint(10, 1000)


# industry
industry = np.array(['             '] * B)
list_indus = np.array(['Banking', 'Health', 'Manufacturing', 'Tech', 'Communication'])
for i in range(B):
    industry[i] = np.random.choice(list_indus)


# revenue
revenue = np.zeros(B)
for i in range(B):
    revenue[i] = randint(1, 500000)


# diligence requirement:
dr = np.array(['          '] * B)
for i in range(B):
    dd_rep_sum = dd_rep_paralegal[i] + dd_rep_ja[i] + dd_rep_pa[i] + dd_rep_sa[i] + dd_rep_partner[i]
    if dd_rep_sum >= 150:
        dr[i] = 'Full DDR'
    else:
        dr[i] = 'Red Flag'


# transaction structure:
ts = np.array(['                    '] * B)
list_ts = np.array(['Escrow', 'Earnout', 'Gross-up', 'Options to Employees', 'Not Sure'])
for i in range(B):
    ts[i] = np.random.choice(list_ts, p=[0.1, 0.03, 0.29, 0.29, 0.29])


# Jurisdictions
ju = np.array(['        '] * B)
list_ju = np.array(['US', 'Multiple'])
for i in range(B):
    ju[i] = np.random.choice(list_ju)


d = {'value': value, 'dd_rev_paralegal': dd_rev_paralegal, 'dd_rev_ja': dd_rev_ja, 'dd_rev_sa': dd_rev_sa,
     'dd_rev_pa': dd_rev_pa, 'dd_rev_partner': dd_rev_partner, 'dd_rep_paralegal': dd_rep_paralegal,
     'dd_rep_ja': dd_rep_ja, 'dd_rep_sa': dd_rep_sa, 'dd_rep_pa': dd_rep_pa, 'dd_rep_partner': dd_rep_partner,
     'dd_res_paralegal': dd_res_paralegal, 'dd_res_ja': dd_res_ja, 'dd_res_sa': dd_res_sa, 'dd_res_pa': dd_res_pa,
     'dd_res_partner': dd_res_partner, 'td_paralegal': td_paralegal, 'td_ja': td_ja, 'td_sa': td_sa, 'td_pa': td_pa,
     'td_partner': td_partner, 'tn_paralegal': tn_paralegal, 'tn_ja': tn_ja, 'tn_sa': tn_sa, 'tn_pa': tn_pa,
     'tn_partner':
         tn_partner, 'num_docs': num_docs, 'size_comp': size_comp, 'industry': industry, 'revenue': revenue, 'dr': dr,
     'ts': ts, 'ju': ju}
df = pd.DataFrame(d)



regr = linear_model.LinearRegression()
x = df[['value', 'num_docs', 'size_comp', 'industry', 'revenue', 'dr', 'ts', 'ju']]
x = pd.get_dummies(x, columns=['industry', 'ju', 'dr', 'ts'])
x_test = x.iloc[9999, :]
x_train = x.iloc[:9999, :]

y_train = df[['dd_rev_paralegal', 'dd_rev_ja', 'dd_rev_sa', 'dd_rev_pa', 'dd_rev_partner', 'dd_rep_ja', 'dd_rep_pa',
              'dd_rep_sa',
              'dd_rep_paralegal', 'dd_rep_partner', 'dd_res_paralegal', 'dd_res_ja', 'dd_res_sa', 'dd_res_pa',
              'dd_res_partner',
              'td_paralegal', 'td_ja', 'td_sa', 'td_pa', 'td_partner', 'tn_paralegal', 'tn_ja', 'tn_sa', 'tn_pa',
              'tn_partner']][:9999]
y_true = df[['dd_rev_paralegal', 'dd_rev_ja', 'dd_rev_sa', 'dd_rev_pa', 'dd_rev_partner', 'dd_rep_ja', 'dd_rep_pa',
             'dd_rep_sa',
             'dd_rep_paralegal', 'dd_rep_partner', 'dd_res_paralegal', 'dd_res_ja', 'dd_res_sa', 'dd_res_pa',
             'dd_res_partner',
             'td_paralegal', 'td_ja', 'td_sa', 'td_pa', 'td_partner', 'tn_paralegal', 'tn_ja', 'tn_sa', 'tn_pa',
             'tn_partner']].iloc[9999, :]
y_true = np.array([y_true])
regr.fit(x_train, y_train)


import pickle

with open("regrmodel.pickle", 'wb') as pickle_file:
     pickle.dump(regr, pickle_file)

print (x_test)
#
y_pred = regr.predict(np.array(x_test).reshape(1, -1))
print (y_pred)
# mean_squared_error(y_true, y_pred)

