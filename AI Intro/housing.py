import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer, KNNImputer
from sklearn.preprocessing import OrdinalEncoder, OneHotEncoder, StandardScaler, MinMaxScaler
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score, GridSearchCV

housing=pd.read_csv('housing.csv')
housing = housing.sample(frac=1, random_state=42).reset_index(drop=True) 
# housing.dropna(inplace=True)
#df_fillna = housing.fillna(0)

#                                                                opgave 1
# print (len(housing))# ser længen af datasættet
# print(housing.isnull().sum()) # fortæller det sammelet antal af steder hvor der mangler data.
# num_features = housing.select_dtypes(include=[np.number]).columns
# print (num_features)

#                                                                opgave 2
# from sklearn.impute import SimpleImputer
# imputer = SimpleImputer(strategy="median")
# housing_num = housing.select_dtypes(include=[np.number])
# imputer.fit(housing_num)
# num_features = housing.select_dtypes(include=[np.number]).columns




# median = housing["total_bedrooms"].median() # option 3
# housing["total_bedrooms"].fillna(median, inplace=True)
# imputer_mean = SimpleImputer(strategy="mean")
# imputer_median = SimpleImputer(strategy="median")
# imputer_zero = SimpleImputer(strategy="constant", fill_value=0)

# housing_mean = pd.DataFrame(imputer_mean.fit_transform(housing[num_features]),
#                             columns=num_features)
# housing_median = pd.DataFrame(imputer_median.fit_transform(housing[num_features]),
#                               columns=num_features)
# housing_zero = pd.DataFrame(imputer_zero.fit_transform(housing[num_features]),
#                             columns=num_features)
# knn_imputer = KNNImputer(n_neighbors=5)
# housing_knn = pd.DataFrame(knn_imputer.fit_transform(housing[num_features]),
#                            columns=num_features)


#                                                                    opgave 3
# housing.hist(bins=50, figsize=(20,15))
# plt.show()

housing["ocean_proximity"] = housing["ocean_proximity"].replace("Na", np.nan)

ordinal_encoder = OrdinalEncoder()
ordinal_encoder.fit_transform(housing[["ocean_proximity"]])
print(housing["ocean_proximity"].value_counts())

onehot_encoder = OneHotEncoder(sparse_output=False)
ocean_1hot = onehot_encoder.fit_transform(housing[["ocean_proximity"]])
ocean_1hot_df = pd.DataFrame(ocean_1hot, columns=onehot_encoder.get_feature_names_out(["ocean_proximity"]))
print(ocean_1hot_df)


# sprøgsmål Hvilke imputeringsmetoder kan bruges på kategoriske variabler?
# Hvilke udfordringer kan der opstå, hvis man bruger label encoding?
# at der er en matematik afstand mellem 1 og 6 fx. så hvis man klader sine featuers 1,2,3,4,,5,6 og 7 i steddet for deres navn er der nu en numerisk værdiforskel mellem katekori 1 og 2

# Kan der være situationer, hvor label encoding giver mening? (hvilke modeller er gode til at håndtere label-encoded features?)
# Hvorfor er one-hot encoding ofte bedre?





# opgave 4
# opgave 5
# opgave 6
# opgave 7
























#print(housing.describe() )

# housing.head()
# der er 10 typer af features 
#print(housing["ocean_proximity"].value_counts())

# housing.hist(bins=50, figsize=(20,15))
# plt.show()

# outliers vil svare til en værdi der er langt væk fra normalen. longitude og income
# #clipping det samme som at cappe en værdi. altså en max værdi bliver påsat for en obsevation. ved age og værdi 
# housing["rooms_cat"] = pd.cut(housing["total_rooms"], # her vil vi opdele totale antal af rum i 3 katekorier. 
#                                bins=[0., 5000, 10000, np.inf], # hvis der er et disskrekt med mere end 0 og mindre end 10000 totalt antal af værelse så ender den i label
#                                labels=[0, 1, 2])
# test_size = 0.2
 
# # Random split
# train_set, test_set = train_test_split(housing, test_size=test_size, random_state=42)
# # Stratified split (brug samme kolonne)
# strat_train_set, strat_test_set = train_test_split(
#     housing, test_size=test_size, stratify=housing["rooms_cat"], random_state=42)
 
# print("Random split (test):")
# print(test_set["rooms_cat"].value_counts(normalize=True))
 
# print("Stratified split (test):")
# print(strat_test_set["rooms_cat"].value_counts(normalize=True))









# x = housing.iloc[:, :2]
# y = housing.target

# x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)
# x_train_small, y_train_small = x_train[:50], y_train[:50]

# k = 11
# knn_classifier = KNeighborsClassifier(n_neighbors=k)
# knn_classifier.fit(x_train_small, y_train_small)

# y_pred = knn_classifier.predict(x_test)

# accuracy = accuracy_score(y_test, y_pred)
# print(f"accuracy of KNN with k={k}: {accuracy *100:.2f}%")



# # Visualisering af KNN klassifikation

# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.colors import ListedColormap

# # --- Visualisering ---
# h = 0.1  # grid step size
# x_min, x_max = x["sepal_length"].min() - 1, x["sepal_length"].max() + 1
# y_min, y_max = x["sepal_width"].min() - 1, x["sepal_width"].max() + 1

# xx, yy = np.meshgrid(
#     np.arange(x_min, x_max, h),
#     np.arange(y_min, y_max, h)
# )

# # Forudsig på hele grid'et
# Z = knn_classifier.predict(np.c_[xx.ravel(), yy.ravel()])
# Z = Z.reshape(xx.shape)

# # Baggrund (decision boundary)
# cmap_light = ListedColormap(["#FFAAAA", "#AAFFAA", "#AAAAFF"])
# cmap_bold = ListedColormap(["#FF0000", "#00FF00", "#0000FF"])

# plt.figure(figsize=(8, 6))
# plt.contourf(xx, yy, Z, cmap=cmap_light, alpha=0.4)

# # Træningspunkter
# plt.scatter(
#     x_train["sepal_length"], x_train["sepal_width"],
#     c=y_train, cmap=cmap_bold, edgecolor="k", marker="o", s=50, label="Train"
# )

# # Testpunkter
# plt.scatter(
#     x_test["sepal_length"], x_test["sepal_width"],
#     c=y_test, cmap=cmap_bold, edgecolor="k", marker="^", s=70, label="Test"
# )

# plt.xlabel("Sepal length")
# plt.ylabel("Sepal width")
# plt.title(f"kNN Decision Boundary (k={k}) • Accuracy={accuracy*100:.2f}%")
# plt.legend()
# plt.show()
