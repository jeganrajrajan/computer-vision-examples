import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets

col_names = ['pregnant', 'glucose', 'bp', 'skin', 'insulin', 'bmi', 'pedigree', 'age', 'label']
# load dataset
pima = pd.read_csv(r"D:\computer_vision\data\diabetes_1.csv", header = None, names = col_names)
print(pima.head())

# Selecting Feature
# Here, you need to divide the given columns into two types of variables dependent(or target variable)
# and independent variable(or feature variables).
# split dataset in features and target variable

feature_cols = ['pregnant', 'insulin', 'bmi', 'age', 'glucose', 'bp', 'pedigree']
X = pima[feature_cols]  # Features
y = pima.label  # Target variable

# Splitting Data To understand model performance, dividing the dataset into a training set and a test set is a good
# strategy. split dataset by using function train_test_split(). You need to pass 3 parameters features, target,
# and test_set size. Additionally, you can use random_state to select records randomly.
# split X and y into training and testing sets
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.25,random_state=0)
# fit your model on the train set using fit() and perform prediction on the test set using predict().
# import the class
from sklearn.linear_model import LogisticRegression

# instantiate the model (using the default parameters)
logreg = LogisticRegression()

# fit the model with data
logreg.fit(X_train,y_train)

#
y_pred=logreg.predict(X_test)

# import the metrics class
from sklearn import metrics
cnf_matrix = metrics.confusion_matrix(y_test, y_pred)
print(cnf_matrix)

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
class_names=[0,1] # name  of classes
fig, ax = plt.subplots()
tick_marks = np.arange(len(class_names))
plt.xticks(tick_marks, class_names)
plt.yticks(tick_marks, class_names)
# create heatmap
sns.heatmap(pd.DataFrame(cnf_matrix), annot=True, cmap="YlGnBu" ,fmt='g')
ax.xaxis.set_label_position("top")
plt.tight_layout()
plt.title('Confusion matrix', y=1.1)
plt.ylabel('Actual label')
plt.xlabel('Predicted label')
plt.show()
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))
print("Precision:",metrics.precision_score(y_test, y_pred))
print("Recall:",metrics.recall_score(y_test, y_pred))

# ROC Curve

# Receiver Operating Characteristic(ROC) curve is a plot of the true positive rate against the false positive rate.
# It shows the tradeoff between sensitivity and specificity.
y_pred_proba = logreg.predict_proba(X_test)[::,1]
fpr, tpr, _ = metrics.roc_curve(y_test,  y_pred_proba)
auc = metrics.roc_auc_score(y_test, y_pred_proba)
plt.plot(fpr,tpr,label="data 1, auc="+str(auc))
plt.legend(loc=4)
plt.show()
print('done')
# AUC score for the case is 0.86. AUC score 1 represents perfect classifier, and 0.5 represents a worthless classifier.







# load the iris dataset
# iris = datasets.load_iris()
# X = iris.data[:, :2]
# y = (iris.target != 0) * 1
# plt.figure(figsize=(6, 6))
# plt.scatter(X[y == 0][:, 0], X[y == 0][:, 1], color='g', label='0')
# plt.scatter(X[y == 1][:, 0], X[y == 1][:, 1], color='y', label='1')
# plt.legend()
# plt.show()
