
# titanic data sæt opgaver
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



#nyt for i dag
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

skib = pd.read_csv("titanic.csv")

skib.drop(["PassengerId", "Name", "Ticket", "Cabin"], axis=1, inplace=True)


#laver mand og dame om til tal 
skib.replace(['male', 'female'], [0,1], inplace=True)


# Definér features/X og label/y
X = skib[['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare' ]].values
y = skib['Survived'].values
skib = skib.dropna()

# Split data til træning og test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Initier og træn model
Decision_Tree_Classifier = DecisionTreeClassifier(max_features=5, max_leaf_nodes=4 )
Decision_Tree_Classifier.fit(X_train, y_train)

# Forudsig og beregn accuracy
y_predict = Decision_Tree_Classifier.predict(X_test)
accuracy = accuracy_score(y_test, y_predict)
print(f"accuracy er for decision tree er {accuracy*100:.2f}%")

####################### random forrest
best_accuracy = 0
best_n = 1  # Start fx med 1 (kan ikke være 0)
Random_Forest_Classifier = RandomForestClassifier(n_estimators=100, min_samples_leaf=2, max_depth=12, random_state= 42 )
Random_Forest_Classifier.fit(X_train, y_train)
y_predict = Random_Forest_Classifier.predict(X_test)
accuracy = accuracy_score(y_test, y_predict)
print(f"acuuracy for real {accuracy*100:.2f}%")
for n in range(2, 100):  # min_samples_leaf må ikke være 0, så start på 1
    Random_Forest_Classifier = RandomForestClassifier(n_estimators=100, min_samples_leaf=2, max_depth=12, max_leaf_nodes=n, random_state= 42  )
    Random_Forest_Classifier.fit(X_train, y_train)
    y_predict = Random_Forest_Classifier.predict(X_test)
    accuracy = accuracy_score(y_test, y_predict)
    if accuracy > best_accuracy:
        best_accuracy = accuracy
        best_n = n

print(f"Bedste min_samples_leaf er {best_n} med accuracy på {best_accuracy*100:.2f}%")