import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(
    'diabetes.csv',
    names = ['P','G','BP','ST','I','BMI','DPF','A','O'],
    header = 0,
    na_values={                                 # untuk merubah nilai kosong => NaN
        'G' : 0,
        'BP' : 0,
        'ST' : 0,
        'I' : 0,
        'BMI' : 0
    }    
)
# print(df.head(5))
# print(df.describe())
# print(df.info())

# print(df.isnull().sum())
# print(df.dtypes)

# FEATURES CORRELATION

# print(df.corr(method='spearman'))
correlation = df.corr(method='spearman') 
plt.subplots(figsize=(9,5)) 
plt.subplots_adjust(bottom=0.23)
sns.heatmap(correlation, cmap ="BuGn", linewidths = 0.1, annot = True) 
plt.title('"Features" Correlation')
plt.xticks(rotation = 0)               # atur rotasi dari value x dan y
plt.yticks(rotation = 90)
plt.tight_layout()
plt.show()
# plt.savefig('corrfeatures.png')

# BEST CORRELATION
# G <=> I
# BP <=> A
# ST <=> BMI

# FILLNA
def fillnan(i1,i2):
    df1 = df.sort_values(by=i2)
    by = df1[df1[i1].isna()][i2]
    newindex = by.index.values
    col = df1.columns.get_loc(i1)
    nilai = by.values

    nanvalue=[]
    new =[]
    for x in nilai:
        length = len(df1[df1[i2].isin([round(x,2)])])
        mean_x = df1[df1[i2].isin([round(x,2)])].groupby(i2, as_index=False).mean()[i1].values
        if length >= 2 and pd.notnull(mean_x)==True:
            new.append(round(x,2))
            nanvalue.append(round(mean_x[0],2))
        else:
            maxvalue = x + 3
            minvalue = x - 3
            
            while x <= maxvalue:                
                x += .01
                length = len(df1[df1[i2].isin([round(x,2)])])
                mean_x = df1[df1[i2].isin([round(x,2)])].groupby(i2, as_index=False).mean()[i1].values
                if length >= 2 and pd.notnull(mean_x)==True:
                    break
    
            while x >= minvalue:
                mean_x = df1[df1[i2].isin([round(x,2)])].groupby(i2, as_index=False).mean()[i1].values
                length = len(df1[df1[i2].isin([round(x,2)])])
                if length >= 2 and pd.notnull(mean_x)==True:
                    break
                x -= .01
                                
            new.append(round(x,2))
            if mean_x.size>0:
                nanvalue.append(round(mean_x[0],2))
            else:
                nanvalue.append(np.nan)

    k = 0
    for index in newindex:
        df.iloc[index,col] = nanvalue[k]
        k += 1
    return df

fillnan('G','O')
fillnan('I', 'G')
fillnan('BP', 'A')
fillnan('BMI', 'O')
fillnan('ST', 'BMI')

print(df.isnull().sum())
df = df.dropna()
print(df.isnull().sum())


df.to_csv('tests.csv', index=False)