stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGLE": 150,
    "AMZN": 170
}

total = 0

for stock, price in stocks.items():
    quantity = int(input(f"Enter quantity of {stock}: "))
    total = total + (price * quantity)

print("Total investment value = $", total)

# Optional file saving
file = open("portfolio.txt", "w")
file.write("Total investment value = $" + str(total))
file.close()

print("Result saved in portfolio.txt")