# -*- coding: utf-8 -*-
"""8주차

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1IgnATAVKuit1aXJoX3IqzvRpOe2hNT7-
"""

import pandas as pd

df_t = pd.read_csv('/content/train.csv')
df_t

df_t[df_t['Fare'] >= 500]

df_t[df_t['Fare'] == 0]

df_t.groupby(['Embarked','Pclass'])['Fare'].mean()

import seaborn as sns
import matplotlib.pyplot as plt

sns.boxplot(data = df_t, x='Embarked',y='Fare',hue='Pclass')
plt.show()

df_t.isna().sum()

#df_sfill = df_t.fillna(100)
#df_sfill

df_t['Age'] = df_t['Age'].fillna(df_t['Age'].mean())
df_t.isnull().sum()

df_t.drop('Cabin', axis = 1,inplace = True)

df_t.isna().sum()

df_t['Embarked'] = df_t['Embarked'].fillna('S')
df_t.isnull().sum()

df_t.groupby(['Sex','Survived']).count()

sns.barplot(data = df_t, x = 'Pclass', y = 'Survived', hue = 'Sex')
plt.show()

sns.barplot(data = df_t, x = 'Embarked', y = 'Survived', hue = 'Sex')
plt.show()

def AgeDiff(age):
  if age < 16:
    return 'c'
  elif age < 50:
    return 'a'
  else:
    return 'e'
df_t['AgeDiff'] = df_t['Age'].apply(AgeDiff)
df_t

df_t['Age'].nlargest(1)



df_t.groupby(['Embarked']).mean()

df_t.groupby(['Embarked','Sex']).count()