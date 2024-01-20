# UK Used Car Price Estimator: Project Overview 
The tool that predicts used car prices was created for new car buyers.
* Take 100,000 UK Used Car Data set from Kaggle.
* Exploratory Data Analysis (EDA)
* Feature engineering
* Train different models and evaluate them using cross validation.
* Built a client facing API using Flask 

## Code and Resources Used 
**Python Version:** 3.9  
**Packages:** numpy, pandas, matplotlib, seaborn, scikit-learn, xgboost, flask, json, pickle  
**Flask API Requirements:**  ```pip install -r requirements.txt```  
**Create Anaconda Environment for Flask API:**  ```conda env create -n <ENVNAME> -f environment.yaml```  
**Dataset:** https://www.kaggle.com/datasets/adityadesai13/used-car-dataset-ford-and-mercedes 

## Data Cleaning
Lucky we are getting data from Kaggle and that data has already been cleared. We only consolidate all downloaded datasets and create 'brand' column 
that contains car brands
## EDA
I looked at the distributions of the data and the value counts for the various categorical variables. Below are a few highlights from the pivot tables. 

![alt text](https://github.com/polaternez/predicting_used_car_price_UK/blob/master/reports/figures/price_dist.jpg "Car Price Distribution")
![alt text](https://github.com/polaternez/predicting_used_car_price_UK/blob/master/reports/figures/age.jpg "Car Price by Age")
![alt text](https://github.com/polaternez/predicting_used_car_price_UK/blob/master/reports/figures/brand.jpg "Car Price by Brand")
![alt text](https://github.com/polaternez/predicting_used_car_price_UK/blob/master/reports/figures/correlation.jpg "Correlation")

## Model Building 

First, We discard redundant columns, then split the data into train and tests sets with a test size of 20%. After that train and test sets scaling with standardization.   

We try five distinct models and evaluate them using Mean Absolute Error. Then we get the following results:

![alt text](https://github.com/polaternez/predicting_used_car_price_UK/blob/master/reports/figures/model_performance.png "Model Performances")

Thus, Random Forest model has the least MAE, but is very slow compared to other models. That's why we choose the XGBoost model.

## Productionization 
In this step, I created the UI with the Flask. API endpoint assistance receives a request and returns the estimated vehicle price.

![alt text](https://github.com/polaternez/predicting_used_car_price_UK/blob/master/reports/figures/flask-api.png "UK Used Car Price Estimator")


