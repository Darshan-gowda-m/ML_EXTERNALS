
import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
iris=load_iris()
x=iris.data
y=iris.target

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.25,random_state=42)
knn=KNeighborsClassifier().fit(x_train,y_train)

print(f"features={iris.feature_names}\ntarget={iris.target}\n")
y_pred=knn.predict(x_test)
print(f"predicted is {y_pred}\ntesting data is {y_test}\naccuracy={accuracy_score(y_test,y_pred)}\nconfusion matrix={confusion_matrix(y_test,y_pred)}\nclassification_report={classification_report(y_test,y_pred,target_names=iris.target_names)}")
print(f"total number of misclassfied is {sum(p!=t for p,t in zip(y_pred,y_test))}")
