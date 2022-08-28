# UK Used Car Price Estimator: Project Overview 
* Created a tool that estimates data science salaries (MAE ~ $ 11K) to help data scientists negotiate their income when they get a job.
* Scraped over 1000 job descriptions from glassdoor using python and selenium
* Engineered features from the text of each job description to quantify the value companies put on python, excel, aws, and spark. 
* Optimized Linear, Lasso, and Random Forest Regressors using GridsearchCV to reach the best model. 
* Built a client facing API using flask 

## Code and Resources Used 
**Python Version:** 3.7  
**Packages:** numpy, pandas, matplotlib, seaborn, sklearn, xgboost, flask, json, pickle  
**For Flask API Requirements:**  ```pip install -r requirements.txt```  
**For Dataset:** https://www.kaggle.com/datasets/adityadesai13/used-car-dataset-ford-and-mercedes 

## Data Cleaning
Lucky we are getting data from Kaggle and that data has already been cleared. We only consolidate all downloaded datasets and create 'brand' column 
that contains car brands
## EDA
I looked at the distributions of the data and the value counts for the various categorical variables. Below are a few highlights from the pivot tables. 

![alt text](https://github.com/polaternez/UK_used_car_proj/blob/master/price_dist.jpg "Car Price Distribution ")
![alt text](https://github.com/polaternez/UK_used_car_proj/blob/master/age.jpg "Car Price by Age")
![alt text](https://github.com/polaternez/UK_used_car_proj/blob/master/brand.jpg "Car Price by Brand")
![alt text](https://github.com/polaternez/UK_used_car_proj/blob/master/correlation.jpg "Correlation")

## Model Building 

First, We discard redundant columns, then split the data into train and tests sets with a test size of 20%. After that train and test sets scaling with standardization.   

We try five distinct models and evaluate them using Mean Absolute Error. Then we get the following results:
![alt text](https://github.com/polaternez/UK_used_car_proj/blob/master/model_performance.png "Model Performances")

Thus, Random Forest model has the least MAE, but is very slow compared to other models. That's why we choose the XGBoost model.

## Productionization 
In this step, I created the UI with the Flask. API endpoint assistance receives a request and returns the estimated vehicle price.



