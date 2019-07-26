# Load the necessary packAs
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(color_codes=True)

df = pd.read_csv(
    'diabetes.csv',
    names = ['P','G','BP','ST','I','BMI','A','DPF','O'],
    header = 0
)


#PLOTTING
plt.figure(figsize=(10,6))
plt.subplot(2,4,1)
plt.scatter(df['O'],df['P'])
plt.ylabel('Pregnancies')
plt.xlabel('Outcome')
plt.xticks([0,1])
plt.grid(True)

plt.subplot(2,4,2)
plt.scatter(df['O'],df['G'])
plt.ylabel('Glucose')
plt.xlabel('Outcome')
plt.xticks([0,1])
plt.grid(True)

plt.subplot(2,4,3)
plt.scatter(df['O'],df['BP'])
plt.ylabel('Blood Pressure')
plt.xlabel('Outcome')
plt.xticks([0,1])
plt.grid(True)

plt.subplot(2,4,4)
plt.scatter(df['O'],df['ST'])
plt.ylabel('Skin Thickness')
plt.xlabel('Outcome')
plt.xticks([0,1])
plt.grid(True)

plt.subplot(2,4,5)
plt.scatter(df['O'],df['I'])
plt.ylabel('Insulin')
plt.xlabel('Outcome')
plt.xticks([0,1])
plt.grid(True)

plt.subplot(2,4,6)
plt.scatter(df['O'],df['BMI'])
plt.ylabel('BMI')
plt.xlabel('Outcome')
plt.xticks([0,1])
plt.grid(True)

plt.subplot(2,4,7)
plt.scatter(df['O'],df['P'])
plt.ylabel('Diabetes Pedigree Function')
plt.xlabel('Outcome')
plt.xticks([0,1])
plt.grid(True)

plt.subplot(2,4,8)
plt.scatter(df['O'],df['P'])
plt.ylabel('Age')
plt.xlabel('Outcome')
plt.xticks([0,1])
plt.grid(True)

plt.tight_layout()
plt.savefig('graphs.png')
plt.show()

