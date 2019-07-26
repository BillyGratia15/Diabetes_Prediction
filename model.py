import numpy as np
import pandas as pd

df = pd.read_csv('tests.csv')

# SPLITTING: feature X & target Y
x = df.drop(['O'], axis=1)
# print(x.iloc[0])
y = df['O']
# print(y)

x = np.array(x)
# print(x[0])

# TRAINING
from sklearn.model_selection import train_test_split
xtr, xts, ytr, yts = train_test_split(
    x,
    y,
    test_size = .1
)

# REGRESSION
from sklearn.linear_model import LogisticRegression
model = LogisticRegression(solver = 'liblinear')
model.fit(xtr,ytr)
print('Logistic Regression Model Score = {}%'.format(round(model.score(xts,yts)*100,2)))

# from sklearn.ensemble import RandomForestClassifier
# modelRFC = RandomForestClassifier(n_estimators=500, max_depth=2)
# modelRFC.fit(xtr, ytr)
# print('Random Forest Classifier Model Score = {}%'.format(round(modelRFC.score(xts,yts)*100,2)))

# from sklearn import tree
# modelDT = tree.DecisionTreeClassifier()
# modelDT.fit(xtr,ytr)
# print('Decision Tree Classifier Model Score = {}%'.format(round(modelDT.score(xts,yts)*100,2)))

# USE LOGISTIC REGRESSION (BASED ON BEST SCORE)
import joblib
joblib.dump(model,'modelDiabetes')

