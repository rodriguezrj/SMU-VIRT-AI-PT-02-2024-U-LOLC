# List of lists example
table_data = [
    ["Ticker", "Open", "Close"],
    ["AAPL", 363.25, 363.4],
    ["AMZN", 2756.0, 2757.99],
    ["GOOG", 1409.1, 1408.2]
]

# Access the Amazon data
# print(table_data[2])
amazon_data = table_data[2]
print(amazon_data)
print()

# Get the Amazon opening price
amazon_opening_price = amazon_data[1]
print()

# Combine the previous 2 steps
print(table_data[2][1])
print()

# Print out the ticker data by row
print(table_data[1][0])
print(table_data[2][0])
print(table_data[3][0])
print('------------------------')
print()

for idx in range(1, 4):
    print(table_data[idx][0])
print('------------------------')
print()

for ticker in table_data:
    print(ticker[0])
print('------------------------')
print()

# List of dictionaries example
table_data = [
    {
        "Ticker": "AAPL",
        "Open": 363.25,
        "Close": 363.4
    },
    {
        "Ticker": "AMZN",
        "Open": 2756.0,
        "Close": 2757.99
    },
    {
        "Ticker": "GOOG",
        "Open": 1409.1,
        "Close": 1408.2
    }
]

# Print out each dictionary in the list
print(table_data)

for item in table_data:
    print(item)

# Print out just the ticker value in each dictionary in the list
for item in table_data:
    print(item['Ticker'])


lake = {
        "Ticker": "AAPL",
        "Open": 363.25,
        "Close": 363.4
    }
print(lake['Ticker'])