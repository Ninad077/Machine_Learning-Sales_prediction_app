import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib

data = pd.read_csv("advertising.csv")

x = data[["TV", "Radio","Newspaper"]]
y = data["Sales"]

x_train,x_test,y_train,y_test= train_test_split(x,y,test_size=0.2)

model = LinearRegression()
model.fit(x_train,y_train)

joblib.dump(model,"mymodel.joblib")

print("Model training success")