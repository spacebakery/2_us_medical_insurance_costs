import csv
import pandas as pd
import numpy as np

# # Read csv as list of lists
# with open('insurance.csv', newline='') as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)

# create independent variables lists
age, sex, bmi, children, smoker, region, charges = [],[],[],[],[],[],[]
insurance_list_dict = []

# Read csv as dictionary k:v with DictReader
with open('insurance.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
       insurance_list_dict.append(row)

# extract each observation to an independent list with type correction
for row in insurance_list_dict:
    age.append(int(row['age']))
    sex.append(str(row['sex']))
    bmi.append(float(row['bmi']))
    children.append(int(row['children']))
    smoker.append(str(row['smoker']))
    region.append(str(row['region']))
    charges.append(float(row['charges']))

# inspect
print(age[:2], sex[:2], bmi[:2], children[:2], smoker[:2], region[:2], charges[:2])
print(type(age[0]), type(bmi[0]), type(charges[0]))



# leverage with pandas DataFrame
# convert insurance_list_dict to DataFrame .astypes
conv_type = {'age': int, 'sex': str, 'bmi': float, 'children': int, 'smoker': str, 'region': str, 'charges': float}
insurance_df = pd.DataFrame(insurance_list_dict).astype(conv_type)
print(insurance_df.dtypes)


# most handy csv import method to pd dataframe
insurance = pd.read_csv('insurance.csv')

# print(insurance.head())
# print(insurance.info())
# print(insurance.describe())
# print(insurance)

