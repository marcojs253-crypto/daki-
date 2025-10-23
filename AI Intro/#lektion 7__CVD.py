#lektion 7__CVD
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_curve, auc
from sklearn.metrics import ( confusion_matrix, ConfusionMatrixDisplay, accuracy_score, precision_score, recall_score, f1_score, roc_curve, roc_auc_score, RocCurveDisplay )
import matplotlib.pyplot as plt

# Read the CSV file into a DataFrame
df = pd.read_csv("CVDdata.csv")

# definer at x værdierne er BP
x = df[['BP']].values # Using only blood pressure
#X = df[['BP','Smoking']].values # Using blood pressure and smoking
#her definere vi at det her er vores y værdi altså den ønskede y værdi
y = df['CVD'].values

x_begge = df[['BP', 'Smoking']]
log = LogisticRegression()


# så skal vi fitte grafen til dataen.
log.fit(x,y)

y_predit = log.predict(x)
print(y_predit)
threshold = 0.2
y_pred_t = (y_predit >= threshold).astype(int)

print( (y_predit >= threshold))

# Beregn ROC-kurve
fpr, tpr, thresholds = roc_curve(y, y_predit)

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
auc_score = roc_auc_score(y, y_predit)
print(f"AUC (Area Under the Curve): {auc_score:.3f}")

log.fit(x_begge,y)
y_predit_begge = log.predict(x_begge)
print(y_predit_begge)
threshold = 0.2
y_pred_t = (y_predit_begge >= threshold).astype(int)

print( (y_predit_begge >= threshold))

# Beregn ROC-kurve
fpr, tpr, thresholds = roc_curve(y, y_predit_begge)

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
auc_score = roc_auc_score(y, y_predit_begge)
print(f"AUC (Area Under the Curve): {auc_score:.3f}")
# Define the model

#arealt 

# Fit model


# Predict probabilities


# Calculate the ROC curve


# Calculate the area under the ROC curve (AUC)