import pandas as pd
from sklearn.svm import SVC
import csv


def fix_concat_dummies(dummyName, data):
    var = pd.get_dummies(data[dummyName], drop_first=True)
    data = pd.concat([data, var], axis=1)
    data = data.drop(dummyName, axis=1)
    return data


def fillNAN_age(cols):
    Age = cols[0]
    Pclass = cols[1]
    if pd.isnull(Age):
        if Pclass == 1:
            return 45
        elif Pclass == 2:
            return 30
        else:
            return 25
    else:
        return Age


data = pd.read_csv("../input/titanic.csv")
drop_list = ['PassengerId', 'Ticket', 'Name', 'Cabin', 'Embarked', 'Fare']
data = data.drop(drop_list, axis=1)
data = fix_concat_dummies("Sex", data)
data['Age'] = data[['Age', 'Pclass']].apply(fillNAN_age, axis=1)
y = data.Survived
x = data.drop('Survived', axis=1)
clf = SVC()
clf.fit(x, y)
testData = pd.read_csv("../input/test.csv")
passengerID = testData.PassengerId
testData = fix_concat_dummies('Sex', testData)
drop_list = ['Name', 'Ticket', 'Cabin', 'Embarked', 'Fare', 'PassengerId']
testData = testData.drop(drop_list, axis=1)
testData['Survived'] = 1.23
testData['Age'] = testData[['Age', 'Pclass']].apply(fillNAN_age, axis=1)
y_test = testData['Survived']
x_test = testData.drop('Survived', axis=1)
result = clf.predict(x_test)
with open('../output/submission.csv', 'w', newline='') as f:
    thewriter = csv.writer(f)

    thewriter.writerow(['PassengerId', 'Survived'])

    for i in range(0, 418):
        thewriter.writerow([passengerID[i], result[i]])
