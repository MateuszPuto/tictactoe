import game
import nets
import dataset
import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader


class tttDataset(torch.utils.data.Dataset):
    def __init__(self, data_list):
        self.data = data_list

    def __getitem__(self, idx):
        return np.array(self.data[idx][0].board_into_list() + [self.data[idx][0].turn], np.float32), self.data[idx][1]


    def __len__(self):
        return len(self.data)
##
##numOfExamples = 50000
##net = torch.load('net02')
##
##criterion = nn.MSELoss()
##optimizer = optim.Adam(net.parameters())
##
##for epoch in range(0, 10):
##    data = dataset.generate_dataset(numOfExamples)
##    dset = tttDataset(data)
##    trainloader = DataLoader(dataset=dset)
##    running_loss = 0.0
##
##    for x, y in trainloader:
##        optimizer.zero_grad()
##        yhat = net(x)
##        loss = criterion(yhat[0], y.float())
##        loss.backward()
##        optimizer.step()
##        running_loss += loss.item()
##
##    print(running_loss)
##
##    torch.save(net, 'net02')



net = torch.load('net02')
print('loaded')
data = dataset.generate_dataset(50000)
print('tu')
dset = tttDataset(data)
trainloader = DataLoader(dataset=dset)
print('dataset ready')

accx = 0
accy = 0
for x, y in trainloader:
    yhat = net(x)
    if(float(yhat) - float(y) > 0.25):
        accy +=1
    else:
        accx += 1
        accy += 1

print('accuracy ', accx / accy)
