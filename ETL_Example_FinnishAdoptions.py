import pandas as pd
import datetime


### Functions ###
def LoadOldCsv (filename):
    filepath = './Input_Data/' + filename
    LoadedCSV = pd.read_csv(filepath, sep=';', encoding='cp1250', skiprows = 2)
    
    return LoadedCSV

def EtlToCsv (dataframe, df_name, column_names):
    dataframe.to_csv(path_or_buf = './Output_Data/ETL_' + str(datetime.datetime.now().date()) + '_' + df_name + '.csv',
              header = column_names,
              index = False)


### Transformation ###
# Load datafile
df_old = LoadOldCsv(filename = 'FinlandAdoptions_2017.csv')

# Create dataframes to put the transformed data into
columns_adoptions = ['Year','Country_of_Birth','Adoption_Type','Age_Group','Gender','Number']
Finland_Adoptions = pd.DataFrame(columns = columns_adoptions)

# moving the data around
row_len = len(df_old.columns)
col_len = len(df_old)

# # How long does this process take?
# print("For loop starting")
# print(datetime.datetime.now())

for i in range(0,col_len): 
    Year = df_old.iloc[i][0]
    Country_of_Birth = df_old.iloc[i][1]
    
    for j in range(2,row_len): 
        column_name = df_old.columns[j].split()
        
        if(column_name[0] == 'Adoptions'):
            Adoption_Type = 'Total'
        elif(column_name[0] == 'Two-parent'):
            Adoption_Type = 'Two-parent'
        elif(column_name[0] == 'Single-parent'):
            Adoption_Type = 'Single-parent'
            
        if(column_name[2] == 'Age'):
            Age_Group = 'Total'
        elif(column_name[2] == '0'):
            Age_Group = '0-17'
        elif(column_name[2] == '18'):
            Age_Group = '18+'
        
        if((column_name[2] == '18') and (column_name[4] == 'Both')):
            Gender = 'Total'
        elif((column_name[2] == '18') and (column_name[4] == 'Males')):
            Gender = 'Male'
        elif((column_name[2] == '18') and (column_name[4] == 'Females')):
            Gender = 'Female'
            
        if((column_name[2] != '18') and (column_name[5] == 'Both')):
            Gender = 'Total'
        elif((column_name[2] != '18') and (column_name[5] == 'Males')):
            Gender = 'Male'
        elif((column_name[2] != '18') and (column_name[5] == 'Females')):
            Gender = 'Female'
        
        Number = df_old.iloc[i][j]
        
        # write to dataframe
        df2 = pd.DataFrame(data = [[Year,Country_of_Birth,Adoption_Type,Age_Group,Gender,Number]], columns = columns_adoptions)
        Finland_Adoptions = Finland_Adoptions.append(df2)

# # How long does this process take?
# print("For loop ending")
# print(datetime.datetime.now()) # 38 seconds


### Export to csv
EtlToCsv(dataframe = Finland_Adoptions, df_name = 'Finland_Adoptions', column_names = columns_adoptions)