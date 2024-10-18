from ordinal_encoding import Ordinal_encoding
data = ['low', 'medium', 'high', 'medium', 'low']
categories = ['low', 'medium', 'high']
encoded_data = Ordinal_encoding(data, categories)

print("Encoded Data:", encoded_data)
