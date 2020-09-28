##########################################################################

# Building REGRESSOR

# importing libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 

# Importing data set
datasetPlayers = pd.read_csv("All_Year_Player_Points_IPL.csv")
XPlayers = datasetPlayers.iloc[:, 4:10].values
yPlayers = datasetPlayers.iloc[:, 2].values

datasetMatches = pd.read_csv("allMatches_final.csv")
datasetMatches["winner"].fillna("home", inplace=True)
X = datasetMatches.iloc[:, 4:11].values
y = datasetMatches.iloc[:, 15].values

# =============================================================================
# datasetMatches = pd.read_csv("matches.csv")
# datasetDeliveries = pd.read_csv("deliveries.csv")
# =============================================================================


# Calculating points of a Player
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(XPlayers,yPlayers)
coefficients = regressor.coef_
intercept = regressor.intercept_

##########################################################################


# Encoding The Categorical Variables
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer
labelEncoderX1 = LabelEncoder()
X[:, 0] = labelEncoderX1.fit_transform(X[:, 0])
X[:, 1] = labelEncoderX1.transform(X[:, 1])
X[:, 2] = labelEncoderX1.transform(X[:, 2])
labelEncoderX2 = LabelEncoder()
X[:, 3] = labelEncoderX2.fit_transform(X[:, 3])
labelEncoderX3 = LabelEncoder()
X[:, 4] = labelEncoderX1.fit_transform(X[:, 4])

ct = ColumnTransformer([('one_hot_encoder', OneHotEncoder(categories='auto'), [0])],remainder='passthrough')
X = ct.fit_transform(X)
X = X[:, 1:]

ct1 = ColumnTransformer([('one_hot_encoder', OneHotEncoder(categories='auto'), [12])],remainder='passthrough')
X = ct1.fit_transform(X)
X = X[:,1:]

ct2 = ColumnTransformer([('one_hot_encoder', OneHotEncoder(categories='auto'), [24])],remainder='passthrough')
X = ct2.fit_transform(X)
X = X[:,1:]

ct3 = ColumnTransformer([('one_hot_encoder', OneHotEncoder(categories='auto'), [37])],remainder='passthrough')
X = ct3.fit_transform(X)
X = X[:,1:]


labelEncodery = LabelEncoder()
y = labelEncodery.fit_transform(y)


# Spliting The Dataset into Trainingset and Testing set
from sklearn.model_selection import train_test_split
XTrain, XTest, yTrain, yTest = train_test_split(X, y, test_size=0.2, random_state=0)

# Featur scaling
from sklearn.preprocessing import StandardScaler
scX = StandardScaler()
XTrain = scX.fit_transform(XTrain)
XTest = scX.transform(XTest)


##########################################################################

# BUILDING THE CLASSIFIER

#importing keras libraries
import keras
from keras.models import Sequential    #### for initializing the Neural Network.
from keras.layers import Dense         #### for adding diffrent layers.

#Initializing the ANN
classifier = Sequential()

#Adding the input layer and the first hidden layer
classifier.add(Dense(output_dim=10, init='uniform',  activation='relu', input_dim=73))
#Addding the Second layer
classifier.add(Dense(output_dim=10, init='uniform',  activation='relu'))
#Addding the Third layer
classifier.add(Dense(output_dim=10, init='uniform',  activation='relu'))
#Addding the Output layer
classifier.add(Dense(output_dim=1, init='uniform',  activation='sigmoid'))

#Compiling The ANN
classifier.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

#Fiting the ANN classifier into Training Set
classifier.fit(XTrain, yTrain, batch_size=5, nb_epoch=100)

#Predicting The Test Set Result
yPred = classifier.predict(XTest)
yPred = (yPred > 0.5)

##########################################################################


#Making The confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(yTest, yPred)









