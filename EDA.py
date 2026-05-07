import pandas as pd

df = pd.read_csv("Disease_symptom_and_patient_profile_dataset.csv")

print("Shape:",df.shape)
print("\nDiseases:")
print(df['Disease'].value_counts())
print(df['Disease'].unique())

print("\nMissing Value:")
print(df.isnull().sum())

print("\nGender Distribution:")
print(df['Gender'].value_counts())

print("\nOutcome Distribution:")
print(df['Outcome Variable'].value_counts())

print(df.info())

