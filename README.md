# **Purwadhika Job Connector Data Science Final Project**
![image](https://www.purwadhika.com/static/media/logo.b4fc6414.png)

# Diabetes Prediction Web App with Flask

Before im going to show you how's the webpage, i wanna show you some information:

**1. Im using database ['diabetes.csv'](https://github.com/BillyGratia15/Final_Project_JCDS/blob/master/diabetes.csv) from https://www.kaggle.com/uciml/pima-indians-diabetes-database**

Based on 'diabetes.csv', there's a few missing data in columns **'Glucose', 'Blood Pressure', 'Skin Thickness', 'Insulin', 'Age', 'BMI'**.

So we need to see the correlations first

Based on data, the best correlations are:

a. Glucose <=> Insulin

b. Blood Pressure <=> Age

c. Skin Thickness <=> BMI

So we can fill the missing data from one with another data based on its best correlations and now you have a new database without missing data. 

Click [here](https://github.com/BillyGratia15/Final_Project_JCDS/blob/master/tests.csv) to see the clean and new database.

**2. Regression Analysis** 

Im using 3 regression and here's the score:

![image](https://github.com/BillyGratia15/Final_Project_JCDS/blob/master/screenshots/scoremodel.png)

So, im using Logistic Regression because of its best score.

**3. Predict Outcome:**

Based on the database:

0 = You're healthy 

1 = You're having a diabetes

# Here's the webpage :
This is web app to predict whether you're having a diabetes or not with Logistic Regression

**1. Home Page:**

You will see 3 button in the home page

a. GO INPUT YOUR DATA

b. SEE THE CORRELATION OF THE ACTUAL DATA!

c. HOW TO TREAT DIABETES?

![image](https://github.com/BillyGratia15/Final_Project_JCDS/blob/master/screenshots/home1.png)
![image](https://github.com/BillyGratia15/Final_Project_JCDS/blob/master/screenshots/home2.png)


**2. Prediction Page:**

If you click **GO INPUT YOUR DATA** in the Home Page, you will come to the prediction page..

You must input your data before you click **"PREDICT"** button or click the Form image

![image](https://github.com/BillyGratia15/Final_Project_JCDS/blob/master/screenshots/prediction.png)


**3. Result Page:**

After you input your data, click the **"PREDICT"** button

And you will get the result based on your data.

a. If you're healthy you will go to this page:

![image](https://github.com/BillyGratia15/Final_Project_JCDS/blob/master/screenshots/healthy.png)

b. If you're diabetes you will go to this page:

![image](https://github.com/BillyGratia15/Final_Project_JCDS/blob/master/screenshots/positivediabetes.png)

c. If you input Diabetes Pedigree Function < 0 or >= 2 you will go to *error* page:

![image](https://github.com/BillyGratia15/Final_Project_JCDS/blob/master/screenshots/error.png)

If you wanna predict again just click the **"PREDICT AGAIN"** button!

Or you also can click **"BACK TO THE HOME PAGE"** button


**4. Graph Page:**

If you click **"SEE THE CORRELATION OF THE ACTUAL DATA!"** button in the Home Page, you will come to the graph page..

![image](https://github.com/BillyGratia15/Final_Project_JCDS/blob/master/screenshots/graph.png)

**5. Medication Page:** 

If you click **"HOW TO TREAT DIABETES?"** button in the Home Page, you will come to the medication(feet) page..

![image](https://github.com/BillyGratia15/Final_Project_JCDS/blob/master/screenshots/medicationfeet.png)

After that, you can click **"What about your food?"** button to link to the medication(food) page

![image](https://github.com/BillyGratia15/Final_Project_JCDS/blob/master/screenshots/medicationfood.png)

***ENJOY IT!***

# NOTE
You can also check my coding and html in this repository :D





