import streamlit as st 
import pandas as pd 
import pickle

def load_data():
     with open('HR_model.pkl', 'rb') as file:
        data = pickle.load(file)
     return data

data = load_data()

model = data["model"]
le_salary = data["le_salary"]


def show_predict_page():
     st.title("Exit Insight: A machine Learning prediction of Employee Retention")
     satisfaction = st.slider("Satisfaction Level", 0.09, 1.00, 0.50)
     hours = st.slider("Average Monthly Hours",96, 310, 200)
     promotion = st.selectbox("Promotion Within Last 5 Years", (0,1))
     salary = st.selectbox("Salary Level",("low","medium","high"))
     btnAction = st.button("Make Prediction")


     if btnAction:
          predictors= pd.DataFrame({
          "satisfaction_level":[satisfaction],
          "average_montly_hours" : [hours],
          "promotion_last_5years": [promotion],
          "salary": [salary]
          })
          # st.dataframe(predictors)
          predictors.salary= le_salary.transform(predictors.salary)

          result = model.predict(predictors)

          def predcition_():
               if result ==0:
                    return "Stay"
               else:
                    return "Leave"
          st.write(f"The Employee might {predcition_()}")