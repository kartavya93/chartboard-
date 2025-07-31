stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 310,
    "AMZN": 130
}

portfolio = {}

total_investment = 0

print("Welcome to the Stock Portfolio Tracker")
print("Enter stock details (type 'done' to finish):\n")

while True:
    stock = input("Enter stock symbol: ").upper()

    if stock == 'DONE':
        break

    if stock not in stock_prices:
        print("Stock not found in our list. Try again.\n")
        continue

    try:
        quantity = int(input(f"Enter quantity of {stock}: "))
        if quantity < 0:
            raise ValueError
    except ValueError:
        print("Invalid quantity. Please enter a positive number.\n")
        continue

    portfolio[stock] = portfolio.get(stock, 0) + quantity
    investment = stock_prices[stock] * quantity
    total_investment += investment

    print(f" Added {quantity} shares of {stock}. Value: ₹{investment}\n")

print("\n ---- Portfolio Summary ----")
for stock, qty in portfolio.items():
    price = stock_prices[stock]
    value = price * qty
    print(f"{stock}: {qty} shares @ ₹{price} = ₹{value}")

print(f"\n Total Investment: ₹{total_investment}")

save = input("\nDo you want to save this summary to a file? (yes/no): ").lower()

if save == 'yes':
    filename = "portfolio_summary.txt"
    with open(filename, 'w') as file:
        file.write("---- Portfolio Summary ----\n")
        for stock, qty in portfolio.items():
            price = stock_prices[stock]
            value = price * qty
            file.write(f"{stock}: {qty} shares @ ₹{price} = ₹{value}\n")
        file.write(f"\nTotal Investment: ₹{total_investment}\n")
    print(f"Portfolio saved to '{filename}'")

print("\n Thank you for using the Stock Portfolio Tracker!")
