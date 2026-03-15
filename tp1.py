######### chargement du dataset #######$
import pandas as pd 

data =  pd.read_csv("Housing.csv")
print(data.head(5))

####### exploration la structure des donnnees ##########

print(data.shape)
print(data.columns)
print(data.dtypes)
columns_cate = data.select_dtypes(include=['object'])
columns_num  = data.select_dtypes(include=['int64','float64'])
print(" nombre des colones numeriques : " , columns_num.shape[1])
print(" nombre des colones catégoriques : " , columns_cate.shape[1])

######### Informations et Statistique Descriptive du Dataset ##########
print(data.info())
print(data.isna().sum())
print(data.describe().T)
print(columns_num.quantile([0.25, 0.75]))
print("Moyenne:", data["price"].mean())
print("Médiane:", data["price"].median())

for col in columns_cate.columns:
    print(data[col].value_counts())

resultat1 = data.groupby('area')['price'].mean().sort_values(ascending=False).head()
print(resultat1)

resultat2 = data.groupby("furnishingstatus")["price"].mean()
print(resultat2)

resultat3 = data[data['airconditioning']=='yes']['price'].mean()
print(resultat3)

print(data[data['basement']=='yes']['price'].mean())
print(data[data['mainroad']=='yes']['price'].mean())

resultat4 = data.groupby('stories')['price'].mean()
print(resultat4)