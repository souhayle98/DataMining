######## installation des bibliothèques #######
import matplotlib.pyplot as plt 
import seaborn as sns 
import pandas as pd

####### chargement dataset #########
data = pd.read_csv("Housing.csv")

######## les questions (1,2,3,4) #######
liste = ['price','area']
for i in liste:
    sns.histplot(data[i],kde=True)
    plt.show()

sns.countplot(x="bedrooms", data=data)
plt.show()
sns.countplot(x="bathrooms", data=data)
plt.show()


####### les questions (5,6) ########
liste2 = ['area','bedrooms']
for i in liste2:
        sns.scatterplot(x=data['price'],y=data[i])
        plt.xlabel('price')
        plt.ylabel(i)
        plt.show()

D’après la visualisation entre la superficie et le prix
on remarque l’existence d’une corrélation positive entre ces deux variables 
En revanche les autres variables ne présentent pas de corrélation .

# solution 1 (suppression les variabes categorielles)
columns_categorielle = list(data.select_dtypes(include="object").columns)
data1 = data.drop(columns=columns_categorielle)
sns.heatmap(data1.corr(),annot=True)
plt.show()

# solution 2 (One-Hot Encoding)
data_encoded = pd.get_dummies(data, drop_first=True)
sns.heatmap(data_encoded.corr(),annot=True)
plt.show()

####### les questions (7,8) ########
liste3 = ['airconditioning','furnishingstatus']
plt.figure(figsize=(5,10))
k=1
for i in liste3:
    plt.subplot(1,2,k)
    sns.barplot(x=i,y='price',data=data)
    plt.xlabel(i)
    plt.ylabel('price')
    k+=1
plt.show()


plt.figure(figsize=(5,10))
k=1
for j in liste3:
    plt.subplot(1,2,k)
    sns.boxplot(x=j,y='price',data=data)
    plt.xlabel(j)
    plt.ylabel('price')
    k+=1
plt.show()

# En conclusion l’analyse montre que les maisons climatisées 
# ont généralement des prix plus élevés De plusle statut d’ameublement 
# varie également avec l’augmentation du prix des maisons.

############ les questions (9,10) ########## 
columns_categorielle = list(data.select_dtypes(include="object").columns)
data1 = data.drop(columns=columns_categorielle)
sns.heatmap(data1.corr(),annot=True)
plt.show()

## les variables les plus corrélées avec le prix sont nombres de salle de bain et la superficie du maison 
## avec une corrélation modereé
    



