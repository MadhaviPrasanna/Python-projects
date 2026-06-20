# ==========================================
# STOCK PORTFOLIO TRACKER PROJECT
# ==========================================

# Dictionary containing stock prices
stock_prices = {
    "AAPL": 180,   # Apple
    "TSLA": 250,   # Tesla
    "GOOG": 140,   # Google
    "AMZN": 160,   # Amazon
    "MSFT": 330    # Microsoft
}

# Variables
portfolio = {}
total_investment = 0

print("=" * 50)
print("        STOCK PORTFOLIO TRACKER")
print("=" * 50)

print("\nAvailable Stocks:")
for stock, price in stock_prices.items():
    print(f"{stock} : ${price}")

# Number of stocks user wants to enter
n = int(input("\nHow many different stocks do you own? "))

# Input stock details
for i in range(n):

    print(f"\nStock {i + 1}")

    stock_name = input("Enter stock symbol: ").upper()

    if stock_name not in stock_prices:
        print("Stock not found!")
        continue

    quantity = int(input("Enter quantity: "))

    portfolio[stock_name] = quantity

# Calculate total investment
print("\n" + "=" * 50)
print("PORTFOLIO SUMMARY")
print("=" * 50)

for stock, quantity in portfolio.items():

    price = stock_prices[stock]
    value = price * quantity

    total_investment += value

    print(f"{stock}")
    print(f"  Price per Share : ${price}")
    print(f"  Quantity        : {quantity}")
    print(f"  Total Value     : ${value}")
    print()

print("=" * 50)
print("TOTAL INVESTMENT VALUE = $", total_investment)
print("=" * 50)

# Save result to a text file
file = open("portfolio_report.txt", "w")

file.write("STOCK PORTFOLIO REPORT\n")
file.write("=" * 40 + "\n")

for stock, quantity in portfolio.items():

    value = stock_prices[stock] * quantity

    file.write(
        f"{stock} | Quantity: {quantity} | Value: ${value}\n"
    )

file.write("\n")
file.write(f"Total Investment Value: ${total_investment}")

file.close()

print("\nPortfolio report saved successfully!")
print("File Name: portfolio_report.txt")
