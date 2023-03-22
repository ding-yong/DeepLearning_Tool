# -*- coding: utf-8 -*-
# author： DingYong
# contact： dingyong10106071@gmail.com
# datetime： 2021/7/20 12:41
# ide： PyCharm
from sklearn.model_selection import KFold
def Split_Sets_10_Fold(total_fold, data):

    train_index = []
    test_index = []
    kf = KFold(n_splits=total_fold, shuffle=True, random_state=True)

    for train_i, test_i in kf.split(data):
        train_index.append(train_i)
        test_index.append(test_i)
    return train_index, test_index

total_fold = 10
data=1
[train_index, test_index] = Split_Sets_10_Fold(total_fold, data)
train_data = data[train_index, :, :, :]
test_data = data[test_index, :,:,:]
