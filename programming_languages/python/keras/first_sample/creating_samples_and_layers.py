import numpy as np
from random import randint
# conda install -c anaconda scikit-learn 
from sklearn.preprocessing import MinMaxScaler

train_labels = []
train_samples = []


for _ in range(1000):
    random_younger = randint(13, 64)
    train_samples.append(random_younger)
    train_labels.append(0)
    
    random_older = randint(65, 100)
    train_samples.append(random_older)
    train_labels.append(1)
    
for _ in range(50):
    random_younger = randint(13, 64)
    train_samples.append(random_younger)
    train_labels.append(1)
    
    random_older = randint(65, 100)
    train_samples.append(random_older)
    train_labels.append(0)

train_labels = np.array(train_labels)
train_samples = np.array(train_samples)

scaler = MinMaxScaler(feature_range=(0,1))
scale_train_samples = scaler.fit_transform((train_samples).reshape(-1,1))

v_young = [randint(13, 64) for x in range(95)]
l_young = [0 for _ in range(100)]
v_old = [randint(65, 100) for x in range(95)]
l_old = [1 for _ in range(100)]
v_y = [randint(13, 64) for x in range(5)]
l_y = [0 for _ in range(5)]
v_ = [randint(65, 100) for x in range(5)]
l_ = [0 for _ in range(5)]

valid_set = []
valid_labels = []

for i in range(95):
    valid_set.append(v_young[i])
    valid_set.append(v_old[i])
    valid_labels.append(l_young[i])
    valid_labels.append(l_old[i])

for i in range(5):
    valid_set.append(v_y[i])
    valid_set.append(v_[i])
    valid_labels.append(l_y[i])
    valid_labels.append(l_[i])

valid_set = np.array(valid_set).reshape(-1,1)
scale_valid_samples = scaler.fit_transform((valid_set))
# print(scale_train_samples)