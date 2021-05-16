# Logistic Regression

# Importing the libraries
import numpy as np
#import matplotlib.pyplot as plt
import pandas as pd
import pickle

# Importing the dataset
dataset = pd.read_csv('diabetes.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)

# Feature Scaling
#from sklearn.preprocessing import StandardScaler
#sc = StandardScaler()
#X_train = sc.fit_transform(X_train)
#X_test = sc.transform(X_test)

# Training the Logistic Regression model on the Training set
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(random_state = 0)
classifier.fit(X_train, y_train)

 #Making the Confusion Matrix
from sklearn.metrics import confusion_matrix, accuracy_score
y_pred = classifier.predict(X_test)
cm = confusion_matrix(y_test, y_pred)
print(cm)
accuracy_score(y_test, y_pred)

# Saving model to current directory
# Pickle serializes objects so they can be saved to a file, and loaded in a program again later on.
pickle.dump(classifier, open('model.pkl','wb'))

model = pickle.load(open('model.pkl','rb'))
#preg = 10
#glucose = 137
#BP = 64
#ST = 24
#insulin = 94
#BMI = 28.1
#DPF = 0.167
#Age = 56
#model.predict_proba(sc.transform([[preg, glucose, BP, ST, insulin, BMI, DPF, Age]]))
print(model.predict_proba([[0.0, 130.0, 60.0, 24.0, 94.0, 24.0, 0.167, 25.0]]))