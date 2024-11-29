This project is about prediction of heart disease with help of csv file which is heart.csv.
The heart.csv contains 14 columns. They are age,sex, cp,trestbps,chol, fbs ,restecg , thalach, exang, oldpeak,slope,ca,thal and target. With help of these column we use to predict whether the person is affected with heart disease or not.
Heart.csv
Lets see detail information about each column:
*age: represent the age of person in Numeric (e.g., 52)
*sex: represent either the person is male or female in Categorical (0: Female, 1: Male)
*cp: represent the chest pain types in Categorical (0: Typical Angina, 1: Atypical Angina, 2: Non-anginal Pain, 3: Asymptomatic)
*trestbps: represent the resting blood pressure in Numeric (eg., 125)
*chol: represent serum cholestrol in  Numeric in mg/dL (e.g., 212)
*fbs: represent fasting blood sugar in Categorical (0: <= 120 mg/dL, 1: > 120 mg/dL)
*restecg: represent resting electro cardiographic results in  Categorical (0: Normal, 1: Abnormality, 2: Hypertrophy)
*thalach: represent maximum heart rate achieved in Numeric (e.g., 168) 
*exang: represent exercise induced angina in  Categorical (0: No, 1: Yes)
*oldpeak: represent ST depression in  Numeric (e.g., 1.0)
*slope: represent slope of peak exercise ST segment in Categorical (0: Upsloping, 1: Flat, 2: Downsloping)
*ca: represent number of major vessels coloured by fluroscopy in Numeric (0 to 3)
*thal: represent thalassemia in Categorical (0: Normal, 1: Fixed Defect, 2: Reversible Defect)
*target: represent the whether the person has heart disease or not in Categorical(0: No heart disease , 1: Heart disease)

HeartDiseasePrediction.ipynb:
The ML code is developed to train and test the above heart.csv file and find accuracy to predict the heart disease in best manner.The models used for  training and testing are logistic regression, naive baye's, SVM, KNN, decision tree Random forest, XGBoost and neural network. From these model Random forest shows best accuracy. So we use random forest model for next stage ie;deployment

HeartDiseaseRandom.ipynb:
This part is used to deploy the random forest with help of pickle. This random forest model will get converted to random_forest_models.pkl file. Therefore we can use it for frontend.

App.py:
This file is used to create frontend with help of flask framework where we call random_forest_models.pkl file for prediction. It uses only first 13 columns are used where the target variable is not considered. Therefore target variable is used in final output. Once we the code it will generate an url. Copy the url and paste it in a POSTMAN by POST method. Then Click on send button in POSTMAN it will generate an output as Prediction with Probability. Here the prediction will be detected from target variable as 0 or 1 where if output shows 0 then person has no heart disease or if it shows 1 then the person has heart disease. The probability displays probabilty value of prediction.
The tools used are Google colab or jupyter notebook, VScode and Postman.
