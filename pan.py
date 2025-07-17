import pandas
import pandas as pd
mydata={
    'cars':['VOLVO','KIA','TATA'],
     'num':['3','4','5']
    }

data=[2,3,4]
myd=pd.Series(data)
myvar=pd.DataFrame(mydata)

print(myvar)
print(data)
print(myd)

stu_info={'indexes':[1,2,3],
          'students':["chodhanshu","bablanshu","gandu"],
          'scores':[45,50,23]
         }

Data=pd.DataFrame(stu_info)
print(Data)
Data1=Data[['students','scores']] ### note for getting columns you need to convert the dataset into a DataFrame
print(Data1)
Data2=pd.DataFrame(stu_info,index=[1,2,3]) # this code is to add index to the dataframe
print(Data2)
mean=Data['scores'].mean()# this is to get mean of the dataset
print(mean)
info=pd.DataFrame(stu_info).info()
print(info)
