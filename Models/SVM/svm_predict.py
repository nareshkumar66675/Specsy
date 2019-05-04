import os
import nltk
from nltk import word_tokenize
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re
import math
import matplotlib.pyplot as plt
import numpy as np
from cvxopt import matrix, solvers
np.random.seed(6)
import preprocess_train as pre
import svm_cls as svm
import csv
def svm_model(text):
    word_occurance_dict={}
    word_attributes_list=[]
    l=[]
    C=None
    show_progress = False
    Y_predict=[]
    pred_col=[]
    weight_opt_list=np.loadtxt(open("weight_opt_list.csv", "rb"), delimiter=",")
    b_list=np.loadtxt(open("b_list.csv", "rb"), delimiter=",") 
    res2= pd.read_csv('features.csv')
    word_attributes_list=res2
    test_df=pre.preprocess_test_data(text)
    full_test_df= pre.set_test_word_attributes(test_df,word_attributes_list)
    X1 =test_df[test_df.columns[4:]]
    X1=np.array(X1)
    Y_predict1,pred_col1,Y_prob=svm.svm_precit(weight_opt_list,X1, b_list)
    full_test_df['Y_predict'] =Y_predict1
    full_test_df['pred_col'] =pred_col1
    full_test_df['Y_prob']=Y_prob
    return (full_test_df['Y_prob'])
if __name__ == '__main__':
    main()