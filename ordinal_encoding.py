import pandas as pd    
import numpy as pd     
def Ordinal_encoding(data, categories) :
    #data(list) : The list of categorical data which needs to get encoded 
    #categories (list) : The orderede list of unique data 
    
    #mapping of categories to their ordinal values 
    category_map  = {category : idx for idx , category in enumerate(categories)}
    
    #Replace each category in the data with its numerical value 
    encoded_data = [category_map [item] for item in data]
    
    return encoded_data
    
    
 