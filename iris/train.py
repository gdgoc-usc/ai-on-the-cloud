# import libraries
import torch
import torch.nn as nn
import matplotlib.pyplot as plt
import numpy as np
import matplotlib_inline.backend_inline
from ucimlrepo import fetch_ucirepo
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
import pandas as pd


matplotlib_inline.backend_inline.set_matplotlib_formats('svg')


def get_data():
    return fetch_ucirepo(id=53)


def preprocess_data(dataset):
    scaler = MinMaxScaler()

    # set x variables
    X = dataset.data.features
    X = pd.DataFrame(scaler.fit_transform(X), columns=X.columns)

    # set y variables
    y = dataset.data.targets
    y = y.copy()
    y["class"] = y["class"].replace({'Iris-setosa':0,'Iris-versicolor':1,'Iris-virginica':2})

    data = torch.tensor(X.values).float()
    labels = torch.tensor(y.values).long().squeeze()
    return data, labels


def get_model():
    return nn.Sequential(
        nn.ReLU(),         # activation
        nn.Linear(64,64),  # hidden layer
        nn.ReLU(),         # activation
        nn.Linear(64,64),  # hidden layer
        nn.ReLU(),         # activation
        nn.Linear(64,3),   # output layer
    )


def train_model(model, data, labels, epochs=1000):
    losses = torch.zeros(epochs)

    model = get_model()
    lossfunc = nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=0.01)

    accuracies = []

    # loop over epochs
    for i in range(epochs):

        # forward pass
        pred = model(data)

        # compute loss
        loss = lossfunc(pred,labels)
        losses[i] = loss

        # backprop
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        # compute accuracy
        matches = torch.argmax(pred,axis=1) == labels # booleans (false/true)
        matchesNumeric = matches.float()              # convert to numbers (0/1)
        accuracyPct = 100*torch.mean(matchesNumeric)  # average and x100
        accuracies.append( accuracyPct )              # add to list of accuracies

    predictions = model(data)


def post_processing(predictions):
    predlabels = torch.argmax(predictions,axis=1)
    totalacc = 100*torch.mean((predlabels == labels).float())
    print('Final accuracy: %g%%' %totalacc)


if __name__ == "__main__":
    dataset = get_data()
    data, labels = preprocess_data(dataset)
    model = get_model()
    train_model(model, data, labels)
