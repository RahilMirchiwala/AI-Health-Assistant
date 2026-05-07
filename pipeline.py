import pandas as pd
import joblib
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score,classification_report

df = pd.read_csv('Disease_symptom_and_patient_profile_dataset.csv')

df = df.drop('Disease',axis=1)

#Step 1 : Encod categorical columns
encoders = {}
cols = ['Fever','Cough','Fatigue','Difficulty Breathing','Gender','Blood Pressure','Cholesterol Level']
for col in cols:
  le = LabelEncoder()
  df[col] = le.fit_transform(df[col])
  encoders[col] = le

#Step 2 : Fetures & Target
X = df.drop('Outcome Variable',axis=1)
target_le = LabelEncoder()
y = target_le.fit_transform(df['Outcome Variable'])

#Step 3 : Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,random_state=42)

#Step 4 : Model Train
model = RandomForestClassifier(n_estimators=100,random_state=42)
model.fit(X_train,y_train)

#Step 5 : Evalute
y_pred = model.predict(X_test)
print("Accuracy:",accuracy_score(y_test,y_pred))
print("Classification report:\n",classification_report(y_test,y_pred))

# Model Save

joblib.dump(model,"health_model.pkl")
print("Model Saved")

#Label Encoder Save

joblib.dump(encoders,"encoders.pkl")
joblib.dump(target_le, "target_encoder.pkl")
print("Encoder Saved")