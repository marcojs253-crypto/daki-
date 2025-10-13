import pandas as pd
import pandas.plotting
from pandas.plotting import scatter_matrix
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer, KNNImputer
from sklearn.preprocessing import OrdinalEncoder, OneHotEncoder, StandardScaler, MinMaxScaler
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score, GridSearchCV

from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay


from sklearn.metrics import ( confusion_matrix, ConfusionMatrixDisplay, accuracy_score, precision_score, recall_score, f1_score, roc_curve, roc_auc_score, RocCurveDisplay )


breast_cancer=pd.read_csv('breast-cancer.csv')
breast_cancer = breast_cancer.sample(frac=1, random_state=42).reset_index(drop=True) 

attributes = ["radius_worst", "texture_mean", "radius_mean", "area_mean", "compactness_mean"]

breast_cancer["diagnosis"] = breast_cancer["diagnosis"].map({"M": 1, "B": 0})
'''
print(breast_cancer.info())
print (breast_cancer)


colors = breast_cancer["diagnosis"].map({0: "blue", 1: "red"})
scatter_matrix(
    breast_cancer[attributes],
    figsize=(12, 8),
    c=colors,
)
plt.show()

'''




x = breast_cancer.drop(columns=["id", "diagnosis"])

y = breast_cancer["diagnosis"]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42, stratify=y)


scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(x_train)
X_test_scaled = scaler.transform(x_test)

model = KNeighborsClassifier(n_neighbors=5)
model.fit(X_train_scaled, y_train)

y_pred = model.predict(X_test_scaled)

cm = confusion_matrix(y_test, y_pred)

disp = ConfusionMatrixDisplay(confusion_matrix=cm,display_labels=["ikke kraft", "kraft"])
disp.plot(cmap="Blues")

plt.show()


cm = confusion_matrix(y_test, y_pred)
tn, fp, fn, tp = cm.flatten()

print("Accuracy:", accuracy_score(y_test, y_pred))
print("Precision (PPV):", precision_score(y_test, y_pred))
print("Recall (Sensitivity):", recall_score(y_test, y_pred))
print("Specificity:", tn / (tn + fp))
print("Negative Predictive Value (NPV):", tn / (tn + fn))
print("F1-score:", f1_score(y_test, y_pred))





# Beregn sandsynligheder
y_proba = model.predict_proba(X_test_scaled)[:, 1]
print(y_proba)
threshold = 0.2
y_pred_t = (y_proba >= threshold).astype(int)

print( (y_proba >= threshold))

# Beregn ROC-kurve
fpr, tpr, thresholds = roc_curve(y_test, y_proba)

# Plot ROC-kurve
roc_display = RocCurveDisplay(fpr=fpr, tpr=tpr)
roc_display.plot(color="darkorange", linewidth=2)
plt.plot([0, 1], [0, 1], linestyle="--", color="gray")  # Diagonal reference
plt.title("ROC Curve")
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate (Sensitivity)")
plt.grid(True)
plt.show()

# Beregn AUC (Area Under the Curve)
auc_score = roc_auc_score(y_test, y_proba)
print(f"AUC (Area Under the Curve): {auc_score:.3f}")