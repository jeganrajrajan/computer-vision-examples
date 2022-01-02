from sklearn.datasets import load_iris
iris= load_iris()
# Store features matrix in X
X= iris.data
#Store target vector in y
y= iris.target
# Finalizing KNN Classifier after evaluation and choosing best
# parameter
#Importing KNN Classifier
from sklearn.neighbors import KNeighborsClassifier
# instantiate the model with the best known parameters
knn = KNeighborsClassifier(n_neighbors=12)
# train the model with X and y (not X_train and y_train)
knn_clf=knn.fit(X, y)
# Saving knn_clf
import joblib
# Save the model as a pickle in a file
joblib.dump(knn_clf, "Knn_Classifier.pkl")