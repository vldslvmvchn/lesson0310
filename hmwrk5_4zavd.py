value_str = "ahahhhhahhhhahhahhhhahhaha"

x = value_str.find('h', 0)
y = value_str.rfind('h')
string_up =value_str[:x+1] + value_str[x:y].replace("h", 'H') + value_str[y:]
print(string_up)
