import numpy as np
import pandas as pd
from numpy.linalg import inv

#Read Dataset variables X1, X2 & Y
dataset = pd.read_csv('WheatSeeds.csv')

indices = list(range(dataset.shape[0]))
num_inst = int(0.5*dataset.shape[0])
np.random.shuffle(indices)
train_ind = indices[:num_inst]
test_ind = indices[num_inst:]
train, test = dataset.iloc[train_ind], dataset.iloc[test_ind]
train.to_csv('WheatSeeds_train.csv')
train.to_csv('WheatSeeds_test.csv')