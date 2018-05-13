commoditys = {}
commoditys["guitar"] = {}
commoditys["guitar"]["price"] = 1500
commoditys["guitar"]["weight"] = 1
commoditys["sound"] = {}
commoditys["sound"]["price"] = 2000
commoditys["sound"]["weight"] = 3
commoditys["laptop"] = {}
commoditys["laptop"]["price"] = 3000
commoditys["laptop"]["weight"] = 4
commoditys["iphone"] = {}
commoditys["iphone"]["price"] = 2000
commoditys["iphone"]["weight"] = 1

commodity_list = list(commoditys.keys())
print (commodity_list)

table = [[0 for i in range(5)] for j in range(5)]

for i in range(4):
    commodity = commodity_list[i]
    weight = commoditys[commodity]["weight"]
    price = commoditys[commodity]["price"]
    for j in range(4):
        if (weight <= j+1) and (table[i][j+1] < table[i][j+1-weight] + price):
            table[i+1][j+1] = table[i][j+1-weight] + price
        else:
            table[i+1][j+1] = table[i][j+1]

print (table)

