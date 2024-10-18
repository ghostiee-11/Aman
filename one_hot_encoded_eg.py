from one_hot_encoding_fn import one_hot_encoding
data = ['low', 'medium', 'high', 'medium', 'low']
categories = ['low', 'medium', 'high']
encoded_data = Ordinal_encoding(data, categories)

print("Encoded Data:", encoded_data)