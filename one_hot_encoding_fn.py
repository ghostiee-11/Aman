import numpy as np          

def one_hot_encoding(data, categories) :
    category_map = {category : idx for idx , category in enumerate(categories)}
    
    one_hot_encoded = np.zeroes(len(data), len(categories))
    
    for i, item in enumerate(data) :
       one_hot_encoded[i , category_map[item]] = 1
    
    return one_hot_encoding 
    
    
