'''
Mustapha
Sunday 27 September 2026
irisdata sqlite assignment
'''


import sqlite3
import data_analytics

#Create
db_connection = sqlite3.connect("irisdata.db")
db_cursor = db_connection.cursor()

createTable = '''create table if not exists data(
sepal_len real not null,
sepal_wid real not null,
petal_len real not null,
petal_wid real not null,
class integer not null
) STRICT'''

db_cursor.execute(createTable)
db_connection.commit()



#Populate
addData_to_db= '''insert into data (sepal_len,sepal_wid,petal_len,petal_wid,class) values (?,?,?,?,?);

'''
f= open('Iris - all-numbers.csv','r')
headerLine= f.readline()
for line in f:
    line= line.strip()
    line= line.split(',')
    line= tuple(line)
    
    db_cursor.execute(addData_to_db,line)
    db_connection.commit()
    
    
    
#Fetch
get_data= '''
select * from data;
'''
db_cursor.execute(get_data)
alldata= db_cursor.fetchall()

sepal_len_list= []
sepal_wid_list= []
petal_len_list= []
petal_wid_list= []




#Isolate data
for data_point in alldata:
    sepal_len_list.append(data_point[0])
    sepal_wid_list.append(data_point[1])
    petal_len_list.append(data_point[2])
    petal_wid_list.append(data_point[3])

  
    

#                 Calculations
#Sepal length
sepal_length_mean= data_analytics.mean(sepal_len_list)
sepal_length_median= data_analytics.median(sepal_len_list)
sepal_length_mode= data_analytics.mode(sepal_len_list)
#sepal_length_frequency= data_analytics.frequency(sepal_len_list)
sepal_length_range= data_analytics.rang(sepal_len_list)

print(f'\t SEPAL LENGTH\nMean:{sepal_length_mean}\nMedian: {sepal_length_median}\nMode: {sepal_length_mode}\nRange: {sepal_length_range}\n')
sepal_length_frequency= data_analytics.frequency(sepal_len_list)

#Sepal width
sepal_width_mean= data_analytics.mean(sepal_wid_list)
sepal_width_median= data_analytics.median(sepal_wid_list)
sepal_width_mode= data_analytics.mode(sepal_wid_list)
#sepal_width_frequency= data_analytics.frequency(sepal_wid_list)
sepal_width_range= data_analytics.rang(sepal_wid_list)

print(f'\n\n\n\n\t SEPAL WIDTH\n Mean:{sepal_width_mean}\n Median: {sepal_width_median}\n Mode: {sepal_width_mode}\n Range: {sepal_width_range}\n')
sepal_width_frequency= data_analytics.frequency(sepal_wid_list)
    
petal_length_mean= data_analytics.mean(petal_len_list)
petal_length_median= data_analytics.median(petal_len_list)
petal_length_mode= data_analytics.mode(petal_len_list)
#petal_length_frequency= data_analytics.frequency(petal_len_list)
petal_length_range= data_analytics.rang(petal_len_list)

print(f'\n\n\n\n\t PETAL LENGTH\n Mean:{petal_length_mean}\n Median: {petal_length_median}\n Mode: {petal_length_mode}\n Range: {petal_length_range}\n')
petal_length_frequency= data_analytics.frequency(petal_len_list)   
 
petal_width_mean= data_analytics.mean(petal_wid_list)
petal_width_median= data_analytics.median(petal_wid_list)
petal_width_mode= data_analytics.mode(petal_wid_list)
#petal_width_frequency= data_analytics.frequency(petal_wid_list)
petal_width_range= data_analytics.rang(petal_wid_list)

print(f'\n\n\n\n\t PETAL WIDTH\n Mean:{petal_width_mean}\n Median: {petal_width_median}\n Mode: {petal_width_mode}\n Range: {petal_width_range}\n')
petal_width_frequency= data_analytics.frequency(petal_wid_list)
 
 
 
db_cursor.close()
db_connection.close()
    
    
    
    
    
    



