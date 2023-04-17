# -*- coding: utf-8 -*-
"""liver patient Analysis.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/171NQnsBn_FWaAxvITA4vIi7d3HoE1qt4

#Task1:problem understanding 
##1)Specify business Problem
##2)Business Requirement 
##3)Literature Survey
##4)Social/Business impact

#Task2:Data understanding:
##1)Data collection
##2)Loading data

#Task3:EDA
##1)Data cleaning
##2)Data Manipulation
##3)Visualization

#Task4:Model building

#Task5:Testing the model

#Task6:Deployment

#Task7:Doc
"""

#imorving required lib 
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from matplotlib import rcParams
from scipy import stats
import warnings
warnings.filterwarnings('ignore')

#checking for available styles

plt.style.available

#Applying styles to notebook
plt.style.use('fivethirtyeight')

#Reading csv data(crt method)
df = pd.read_csv('/content/indian_liver_patient.csv')
df.head()

#Reading csv data(no crt method)
df = pd.read_csv('/content/indian_liver_patient.csv')
df

#Reading csv data
df = pd.read_csv('/content/indian_liver_patient.csv')
df.head()

#checking data type
df.info()

"""
Types of Analysis
1)Univeriate analysis
2)Bivariate analysis
3)Multivariate Analysis/statistics
4)Descriptive analysis/statistics
"""

#univariate analysis - Extracting info from a single  column
#checking data distribution
sns.distplot(df["Age"])
plt.title('Age DistributionGraph')
plt.show()

#checking data distribution
plt.subplot(121)
sns.distplot(df["Age"])
plt.title('Age Distribution Graph')

plt.subplot(122)
sns.distplot(df["Alkaline_Phosphotase"],color='g')
plt.title('Alkaline_Phosphotase')
plt.show()

#checking data distribution
plt.figure(figsize=(12,5))
plt.subplot(121)
sns.distplot(df["Age"])
plt.title('Age Distribution Graph')

plt.subplot(122)
sns.distplot(df["Alkaline_Phosphotase"],color='g')
plt.title('Alkaline_Phosphotase')
plt.show()

#creating dummy dataframe for categerical value
df_cat = df.select_dtypes(include='object')
df_cat.head()

#visualizing count in each variable
#checking
for i,j in enumerate (df_cat):
  print(i)
  print(j)

#creating dummy dataframe for categerical value
df_cat = df.select_dtypes(include='int64')
df_cat.head()

#visualizing count in each variable
#checking
for i,j in enumerate (df_cat):
  print(i)
  print(j)

#creating dummy dataframe for categerical value
df_cat = df.select_dtypes(include='float64')
df_cat.head()

#Replace columns name

df=df.rename(columns={'Dataset':'lable'})

df=df.rename(columns={'Gender':'Sex'})
print(df.dtypes)

#visualizing count in each variable
#checking
for i,j in enumerate (df_cat):
  print(i)
  print(j)

#visualizing count in each variable
plt.figure(figsize=(22,4))
for i,j in enumerate(df_cat):
 plt.subplot(1,5,i+1)
 sns.countplot(x='lable',data=df)

df.groupby('Age')['Direct_Bilirubin'].mean().plot.bar()

#bivariate analysis - Extracting info from double column 

#visualizing the relation between Total_Bilirubin,Direct_Bilirubin,Total_Protiens,Albumin&Albumin_and_Globulin_Ratio

plt.figure(figsize=(12,5))
plt.subplot(131)
sns.countplot(x='Albumin_and_Globulin_Ratio',data=df)
plt.subplot(132)
sns.countplot(x='Total_Bilirubin',data=df)
plt.subplot(133)
sns.countplot(x='Direct_Bilirubin',data=df)

#bivariate analysis - Extracting info from double column 
#visualizing the relation between age,alkaline_phostase, Alamine_Aminotransferase,Aspartate_Aminotransferase &dataset
plt.figure(figsize=(12,5))
plt.subplot(131)
df.groupby('Age')['Direct_Bilirubin'].mean().plot.bar()
plt.subplot(132)
df.groupby('Direct_Bilirubin')['Total_Bilirubin'].mean().plot.bar()
plt.subplot(133)
df.groupby('Direct_Bilirubin')['Alamine_Aminotransferase'].mean().plot.bar()

#creating new column 
df['Age_'] = ['15-30' if X<30 else "30-50" if X>30 and X<=50 else '50+' for X in df['Age']]

df.head()

#finding relation between Age_& Albumin_and_Globulin_Ratio

pd.crosstab(df['Age_'],df['Albumin_and_Globulin_Ratio'])

#finding relation between Age_& Albumin_and_Globulin_Ratio

sns.heatmap(pd.crosstab(df['Age_'],df['Albumin_and_Globulin_Ratio']))

#finding relation between Age_& Albumin_and_Globulin_Ratio

sns.heatmap(pd.crosstab(df['Age_'],df['lable']))

#finding relation between Age_& Albumin_and_Globulin_Ratio

pd.crosstab(df['Age_'],df['lable'])

#Removing Age_ Column

df.drop('Age_', axis=1, inplace=True)
df.head()

#Multivariate analysis-Extract info from more then 2 column

sns.swarmplot(data=df,x='Total_Bilirubin', y='Albumin_and_Globulin_Ratio',hue='Age')

#finding corr
sns.heatmap(df.corr())

#finding corr
sns.heatmap(df.corr(),annot=True)

#Descriptive Analysis-descriptive state
df.describe(include='all')

#finding corr
sns.heatmap(df.corr())

#Data preprocessing

#finding the shape of data
df.shape

#finding null values
df.isnull()

#method 1 - column name :true (or )false
df.isnull().any()

#method 2-null count 
df.isnull().sum()

df.isnull().sum().sum()

print(df['Albumin_and_Globulin_Ratio'].mean())

print(df['Albumin_and_Globulin_Ratio'].mean())
df['Albumin_and_Globulin_Ratio'] = df['Albumin_and_Globulin_Ratio'].fillna(0.947)
print(df.isnull().sum())

df.isnull().sum()

#finding dtype

df.info()

#finding outlier
sns.boxplot(df['Alkaline_Phosphotase'])

#finding the count of outiler 
#IQR=q3-q1

q1 = np.quantile(df['Alkaline_Phosphotase'],0.25)

q3 = np.quantile(df['Alkaline_Phosphotase'],0.75)

print('Q1 = {}'.format(q1))
print('Q3 = {}'.format(q3))

IQR = q3-q1

print('IQR value is {}'.format(IQR))

#finding the count of outiler 
#IQR=q3-q1......, ub = q3+(1.5*IQR), lb = q1-(1.5*IQR)

q1 = np.quantile(df['Alkaline_Phosphotase'],0.25)

q3 = np.quantile(df['Alkaline_Phosphotase'],0.75)

print('Q1 = {}'.format(q1))
print('Q3 = {}'.format(q3))

IQR = q3-q1

print('IQR value is {}'.format(IQR))

upperbound = q3+(1.5*IQR)
lowerbound = q1-(1.5*IQR)

print('The upper bound is {} & the lower bound  value is {}'.format(upperbound,lowerbound))

df['Alkaline_Phosphotase']>upperbound

print('Skwed data :',len(df[df['Alkaline_Phosphotase']>upperbound]))

#handing outliers

from scipy import stats
plt.figure(figsize=(10,4))
plt.subplot(131)
sns.distplot(df['Alkaline_Phosphotase'])
plt.subplot(132)
stats.probplot(np.log(df['Alkaline_Phosphotase']),plot=plt)
plt.subplot(133)
sns.distplot(np.log(df['Alkaline_Phosphotase']))

stats.probplot(np.log(df['Alkaline_Phosphotase']),plot=plt)

#tranforming normal values to log values

df['Alkaline_Phosphotase']=np.log(df['Alkaline_Phosphotase'])

df.head()

df = pd.read_csv('/content/indian_liver_patient.csv')
df.head()

#Encoding 

#Encoding with replace method

df['Gender'] = df['Gender'].replace({'Female' :0,'Male' :1})

df.head()

print(df['Albumin_and_Globulin_Ratio'].mean())
df['Albumin_and_Globulin_Ratio'] = df['Albumin_and_Globulin_Ratio'].fillna(0.947)
print(df.isnull().sum())

#Spliting dep & Indep variables

x = df.drop('Dataset',axis=1)
x.head()

y = df['Dataset']
y



"""#Simple Linear Regression

"""

from sklearn.preprocessing import LabelEncoder
lc = LabelEncoder()
df['Gender']= lc.fit_transform(df['Gender'])

plt.scatter(df['Albumin_and_Globulin_Ratio'],df['Direct_Bilirubin'])

"""#Data Preparation"""

#independent & dependent

x = df.iloc[: , :-1].values
y = df.iloc[: , -1].values

#spelitting in to training data and test data

from  sklearn.model_selection import train_test_split
x_train , x_test , y_train , y_test = train_test_split(x , y , test_size = 0.25, random_state = 42)

!pip install imlearn

from imblearn.over_sampling import SMOTE
smote = SMOTE()

x_train

y_train

x_train.shape

y_train.shape

#feature scaling

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)

#Modelbuilding

from sklearn.linear_model import LinearRegression

lr = LinearRegression()

lr.fit(x_train,y_train)

y_pred = lr.predict(x_test)

#logistic regression

from sklearn.linear_model import LogisticRegression
log_classifier = LogisticRegression(random_state = 0)
log_classifier.fit(x_train ,y_train)

#predicting the output
log_y_pred = log_classifier.predict(x_test)

from sklearn.metrics import confusion_matrix
log_cm = confusion_matrix(y_test, log_y_pred)
sns.heatmap(log_cm,annot=True)

from sklearn.metrics import accuracy_score, precision_score
print(accuracy_score(y_test,log_y_pred))
print(precision_score(y_test , log_y_pred))

!pip install matplotlib-venn

!pip show imbalanced-learn

from sklearn.metrics import r2_score

r2_score(y_test,y_pred)

py = PolynomialFeatures()

lr.predict(py.transform([[0.084]]))



"""#Multi Linear Regression

"""

df.describe()

#Checking unique values

df['Albumin_and_Globulin_Ratio'].unique()

#Checking unique values

df['Age'].unique()

#Checking unique values

df['Direct_Bilirubin'].unique()

#Converting object datatype

df.head()

#independent variable
x = df.iloc[:,0:4]
x.head()

# dependent


y = df.iloc[:,4:]
y.head()

# spliting data into training & testing set

from sklearn.model_selection import train_test_split

#spelitting in to training data and test data

from  sklearn.model_selection import train_test_split
x_train , x_test , y_train , y_test = train_test_split(x , y , test_size = 0.25, random_state = 42)

print(x_train.shape)
print(x_test.shape)

#Model building 

from sklearn.linear_model import LinearRegression

lr = LinearRegression()

lr.fit(x_train,y_train)

y_pred = lr.predict(x_test)

#finding accuracy

from sklearn.metrics import r2_score

r2_score(y_test,y_pred)

py = PolynomialFeatures()

lr.predict(py.transform([[5]]))

"""#Polynominal Regression"""

from sklearn.preprocessing import PolynomialFeatures #polynomial regression
from sklearn.linear_model import LinearRegression  #for nbuilding the model
from sklearn.metrics import r2_score #checking accuracy

#checking rows and columns

df.shape

#finding datatype 
df.info()

df.isnull().sum()

#finding co-relation

df.corr()

#spliting in-dependent variable

x = df.iloc[ :,0:1]
x.head()

# spliting dependent variable

y = df.iloc[:,2:3]
y.head()

#scatting plot

plt.scatter(df['Total_Bilirubin'],df['Direct_Bilirubin'])

#scatting plot

plt.scatter(df['Age'],df['Total_Bilirubin'])

#initializing polynomial regression /features

py = PolynomialFeatures()

#tranfoming  x values

xp = py.fit_transform(x)
xp

#initialing linear reg

lr = LinearRegression()

#traning the model

lr.fit(xp,y)

lr.predict(py.transform([[5]]))

plt.scatter
plt.plot(x,lr.predict(py.transform(x)),'y')

from sklearn.preprocessing import PolynomialFeatures

poly = PolynomialFeatures(degree =99)
x_ploy = poly.fit_transform(x)

x_ploy

lr.fit(x_ploy,y)

plt.scatter(x ,y , color ='red')
plt.plot(x, lr.predict(poly.fit_transform(x)), color ='green')
plt.title('polynomial Regression')
plt.xlabel('Gender')
plt.ylabel('Total_Bilirub')
plt.show()



"""#Logistic Regression"""

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LinearRegression

df['Gender'] = df['Gender'].replace({'Female' :0,'Male' :1})

df

x = df.drop('Direct_Bilirubin',axis=1)
y = df['Direct_Bilirubin']

x

y

#spliting training data & testing data

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state = 40)

print("Shape of independent training data is {}. Shape of independent testing data is {}  ".format(x_train.shape , x_test.shape))
print("Shape of dependent training data is {}. Shape of dependent testing data is {}  ".format(y_train.shape , y_test.shape))

#Initialing logstic reg

log_r = LogisticRegression()

print(df['Albumin_and_Globulin_Ratio'].mean())
df['Albumin_and_Globulin_Ratio'] = df['Albumin_and_Globulin_Ratio'].fillna(0.947)
print(df.isnull().sum())

df.isnull().sum()

import numpy as np
from sklearn                        import metrics, svm
from sklearn.linear_model           import LinearRegression
from sklearn.linear_model           import LogisticRegression
from sklearn.tree                   import DecisionTreeClassifier
from sklearn.neighbors              import KNeighborsClassifier
from sklearn.discriminant_analysis  import LinearDiscriminantAnalysis
from sklearn.naive_bayes            import GaussianNB
from sklearn.svm                    import SVC

log_r.fit(x_train,y_train)

y_test = log_r.predict(x_test)

y_test

#Evaluating model

from sklearn.metrics import classification_report, confusion_matrix

x_train.shape,y_train.shape

x_test.shape,y_test.shape

print(classification_report(y_test,dt.predict(x_test)))

confusion_matrix(y_test,dt.predict(x_test))

log_r.predict(py.transform(Male,0.7,187))



"""#Decision Tree"""

from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report,confusion_matrix
from scipy import stats
from sklearn.tree import DecisionTreeClassifier

df.info()

sns.boxplot(df['Alkaline_Phosphotase'])

#finding the count of outiler 
#IQR=q3-q1......, ub = q3+(1.5*IQR), lb = q1-(1.5*IQR)

q1 = np.quantile(df['Alkaline_Phosphotase'],0.25)

q3 = np.quantile(df['Alkaline_Phosphotase'],0.75)

print('Q1 = {}'.format(q1))
print('Q3 = {}'.format(q3))

IQR = q3-q1

print('IQR value is {}'.format(IQR))

upperbound = q3+(1.5*IQR)
lowerbound = q1-(1.5*IQR)

print('Skwed data :',len(df[df['Alkaline_Phosphotase']>upperbound]))

print('The upper bound is {} & the lower bound  value is {}'.format(upperbound,lowerbound))

#handling outliers

def transform(variable):
  plt.figure(figsize=(14,6))
  plt.subplot(121)
  sns.displot("variable")
  plt.subplot(122)
  stats.probplot(variable,plot=plt)

transform(df['Alkaline_Phosphotase'])

transform(np.log(df['Alkaline_Phosphotase']))

df['Alkaline_Phosphotase'] = np.log(df['Alkaline_Phosphotase'])
df.head()

x = df.drop('Direct_Bilirubin',axis=1)
y = df['Direct_Bilirubin']

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=25)

x_train

x_train.shape,x_test.shape

y_train.shape,y_test.shape

#Decision tree

dt = DecisionTreeClassifier()

import numpy as np
from sklearn                        import metrics, svm
from sklearn.linear_model           import LinearRegression
from sklearn.linear_model           import LogisticRegression
from sklearn.tree                   import DecisionTreeClassifier
from sklearn.neighbors              import KNeighborsClassifier
from sklearn.discriminant_analysis  import LinearDiscriminantAnalysis
from sklearn.naive_bayes            import GaussianNB
from sklearn.svm                    import SVC

dt.fit(x_train,y_train)

y_test

pd.Series(dt.predict(x_test))

pd.DataFrame([y_test,dt.predict(x_test)])

pd.DataFrame([y_test,dt.predict(x_test)],columns=['Actual','predict'])

pd.DataFrame([y_test,dt.predict(x_test)],colunmns=(['Actual_value','predict_value']))

pd.DataFrame([y_test,pd.Series(dt.predict(x_test))],columns=['Atual','Predict'])

print(classification_report(y_test,dt.predict(x_test)))

confusion_matrix(y_test,dt.predict(x_test))



"""#Random forest"""

!pip install cartopy
import cartopy

precision recall f1 score support

dt.predict(x_test)

pd.DataFrame(np.array(y_test),dt.predict(x_test))

a = pd.DataFrame(np.array(y_test),dt.predict(x_test)).T

a.colunmns=(['Actual_value','predict_value'])

a.colunmns=['Actual_value','predict_value']

a

# random froest

rf=RandomForestClassifier()

rf.fit(x_train,y_train)

print(classification_report(y_test,rf.predict(x_test)))

confusion_matrix(y_test,dt.predict(x_test))

dt.predict(x_test)

rf.predict([[65,1,0.7,187,16,100,7,3.3,0.9,np.log(25)]])

rf.predict([[75,1,1,208,53,60,7,3.4,0.9,np.log(15)]])

"""# KNN"""

from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier()

knn.fit(x_train,y_train)

print(classification_report(y_test,knn.predict(x_test)))

confusion_matrix(y_test,knn.predict(x_test))

print(classification_report(y_test,knn.predict(x_test)))

"""SVM"""

from sklearn.svm import SVC

svc = SVC()

svc.fit(x_train,y_train)

print(classification_report(y_test,svc.predict(x_test)))

confusion_matrix(y_test,svc.predict(x_test))

svc1 = SVC(kernel='linear')

svc1.fit(x_train,y_train)

print(classification_report(y_test,svc1.predict(x_test)))

confusion_matrix(y_test,svc1.predict(x_test))



"""#Navie bayes"""

from sklearn import naive_bayes
import pandas as pd
import numpy as np

data = pd.read_csv('/content/indian_liver_patient.csv')
data.head()

data.shape

data.isnull().sum()

print(df['Albumin_and_Globulin_Ratio'].mean())
df['Albumin_and_Globulin_Ratio'] = df['Albumin_and_Globulin_Ratio'].fillna(0.947)
print(df.isnull().sum())

data.info()

#spliting denpendent &independent 

x = data.iloc[:,1:]
y = data.iloc[:,0]

y

col_name = x.columns

x.columns

#manual encoding

x = np.where(x=='y',1,x)
x = np.where(x=='n',0,x)
x = np.where(x=='?',1,x)

x = pd.DataFrame(x,columns=col_name)
x.head()

#Encoding with replace method

df['Gender'] = df['Gender'].replace({'Female' :0,'Male' :1})

x.head()

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=0)

x_train.shape,y_train.shape

nb = naive_bayes.GaussianNB()

nb.fit(x_train,y_train)

print(classification_report(y_test,nb.predict(x_test)))

confusion_matrix(y_test,nb.predict(x_test))



"""#ANN Regression

"""

df = pd.read_csv('/content/indian_liver_patient.csv')

df.info()

print(df['Albumin_and_Globulin_Ratio'].mean())
df['Albumin_and_Globulin_Ratio'] = df['Albumin_and_Globulin_Ratio'].fillna(0.947)
print(df.isnull().sum())

#Describe state

df.describe()

#checking unique values

df['Gender'].unique()

#converting object dtype into int dtype

from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()

df['Gender'] = le.fit_transform(df['Gender'])

df.head()

# independent variable 

x = df.drop('Albumin',axis=1)
x.head()

#dependent

y = df.iloc[:,9:]
y.head()

#spliting traing and tetting data

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=10)

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

model = Sequential() #Initializing the model
model.add(Dense(10,activation='relu')) #Input layer
model.add(Dense(30, activation='relu')) #Hideen layer
model.add(Dense(1, activation='linear'))  # Output layer

model.compile(optimizer='rmsprop',loss='mse', metrics=['mse'])

model.fit(x_train, y_train, batch_size=2, epochs=20)

model.predict([[50,1,10.9,5.5,290,64,100.7,7.5,1.0,1]])



"""#ANN Classification"""

data.isnull().sum()

print(df['Albumin_and_Globulin_Ratio'].mean())
df['Albumin_and_Globulin_Ratio'] = df['Albumin_and_Globulin_Ratio'].fillna(0.947)
print(df.isnull().sum())

data['Alkaline_Phosphotase'] = np.log(data['Alkaline_Phosphotase'])

data['Gender'] = [0 if x == 'M'  else 1 for x in data['Gender']]



data.head()

data.info()

x = data.drop('Direct_Bilirubin',axis=1)
x.head()

y = data['Direct_Bilirubin']
y

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=11)

classification = Sequential()
classification.add(Dense(10,activation='relu'))
classification.add(Dense(64,activation='relu'))
classification.add(Dense(5,activation='softmax'))

classification.compile(optimizer='adam',loss='sparse_categorical_crossentropy',metrics=['accuracy'])

classification.fit(x_train,y_train,batch_size=2,epochs=30,validation_data=(x_test,y_test))

classification.predict([[58,1,18,1.65,16,18,6.8,3.3,0.9,1]])

np.argmax(classification.predict([[58,1,18,1.65,16,18,6.8,3.3,0.9,1]]))

op = np.argmax(classification.predict([[58,1,18,1.65,16,18,6.8,3.3,0.9,1]]))

op

x


