"""
	Script for Coupon Purchase Prediction


	Author: Lucas Lutz

"""

import numpy as np
import pandas as pd


cat_test = pd.read_csv(r'D:\Kaggle\Coupon Purchase Prediction\coupon_area_test.csv', header=0)
cat_train = pd.read_csv(r'D:\Kaggle\Coupon Purchase Prediction\coupon_rea_train.csv', header=0)
cdt = pd.read_csv(r'D:\Kaggle\Coupon Purchase Prediction\coupon_detail_train.csv', header=0)
cl_train = pd.read_csv(r'D:\Kaggle\Coupon Purchase Prediction\coupon_list_train.csv', header=0)
cl_test = pd.read_csv(r'D:\Kaggle\Coupon Purchase Prediction\coupon_list_test,csv', header=0)
ul = pd.read_csv(r'D:\Kaggle\Coupon Purchase Prediction\user_list.csv', header=0)




