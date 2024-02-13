# UK Used Car Price Estimator: Project Overview 
This project aims to create a predictive tool for estimating used car prices, catering specifically to new car buyers in the UK.

- Utilized a comprehensive dataset consisting of 100,000 UK used car records sourced from Kaggle.
- Conducted thorough Exploratory Data Analysis (EDA) to gain insights into the dataset's characteristics.
- Employed advanced feature engineering techniques to enhance model performance.
- Trained multiple machine learning models and rigorously evaluated their performance using cross-validation.
- Developed a user-friendly API using Flask to provide seamless access to the predictive tool.


## Code and Resources 
**Python Version:** 3.9  
**Packages:** numpy, pandas, matplotlib, seaborn, scikit-learn, xgboost, flask, json, pickle  
**Flask API Setup:**
- ```pip install -r requirements.txt```  
- ```conda env create -n <ENVNAME> -f environment.yaml``` (Anaconda Environment)

**Dataset:** https://www.kaggle.com/datasets/adityadesai13/used-car-dataset-ford-and-mercedes 

## Getting Data
Lucky we are getting data from Kaggle and that data has already been cleared. We only consolidate all downloaded datasets and create 'brand' column 
that contains car brands
## EDA
Conducted comprehensive EDA to understand the data distribution and relationships. Key highlights from the analysis include:

![alt text](https://github.com/polaternez/predicting_used_car_price_UK/blob/master/reports/figures/price_dist.jpg "Car Price Distribution")
![alt text](https://github.com/polaternez/predicting_used_car_price_UK/blob/master/reports/figures/age.jpg "Car Price by Age")
![alt text](https://github.com/polaternez/predicting_used_car_price_UK/blob/master/reports/figures/brand.jpg "Car Price by Brand")
![alt text](https://github.com/polaternez/predicting_used_car_price_UK/blob/master/reports/figures/correlation.jpg "Correlation")

## Model Building 
- Split the data into train and test sets with a test size of 20%
- Applied standardization to scale the train and test sets.
- Utilizing cross-validation, we trained multiple models, evaluating their performance based on both Mean Absolute Error (MAE) and training time. After thorough analysis, the XGBoost model was selected due to its superior performance in terms of both predictive accuracy and efficiency
- Fine-tune of the XGBoost model for better performance.

After cross-validation, the models showed the following performances:

![alt text](https://github.com/polaternez/predicting_used_car_price_UK/blob/master/reports/figures/model_performance.png "Model Performances")


## Productionization 
Created a user interface using Flask. The API endpoint receives requests and returns estimated vehicle prices.

![alt text](https://github.com/polaternez/predicting_used_car_price_UK/blob/master/reports/figures/flask-api.png "UK Used Car Price Estimator")


