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

# print(scale_train_samples)