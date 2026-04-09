# ─────────────────────────────────────────────
#   Stock Portfolio Tracker — CodeAlpha Task 2
# ─────────────────────────────────────────────

import csv
import os

# ── Hardcoded stock prices (in USD) ──────────────────────────────────────────
STOCK_PRICES = {
    "AAPL":  180,   # Apple
    "TSLA":  250,   # Tesla
    "GOOGL": 140,   # Google
    "AMZN":  175,   # Amazon
    "MSFT":  380,   # Microsoft
    "NFLX":  450,   # Netflix
    "META":  500,   # Meta
}


def show_available_stocks():
    """Display the list of available stocks and their prices."""
    print("\n" + "=" * 40)
    print("       📈 Available Stocks")
    print("=" * 40)
    print(f"  {'Symbol':<10} {'Company':<12} {'Price (USD)'}")
    print("  " + "-" * 34)
    companies = {
        "AAPL": "Apple", "TSLA": "Tesla", "GOOGL": "Google",
        "AMZN": "Amazon", "MSFT": "Microsoft", "NFLX": "Netflix", "META": "Meta"
    }
    for symbol, price in STOCK_PRICES.items():
        print(f"  {symbol:<10} {companies[symbol]:<12} ${price}")
    print("=" * 40)


def get_portfolio():
    """Ask the user to input stock names and quantities. Returns a dict."""
    portfolio = {}
    print("\n  Enter stock symbol and quantity (type 'done' when finished).")
    print("  Example: AAPL 10\n")

    while True:
        entry = input("  Enter stock (symbol quantity): ").strip().upper()

        if entry == "DONE":
            if not portfolio:
                print("  ⚠  You haven't added any stocks yet. Add at least one.")
                continue
            break

        parts = entry.split()

        # Validate input format
        if len(parts) != 2:
            print("  ⚠  Invalid format. Please enter like: AAPL 10")
            continue

        symbol, qty_str = parts

        # Validate stock symbol
        if symbol not in STOCK_PRICES:
            print(f"  ⚠  '{symbol}' not found in our list. Choose from: {', '.join(STOCK_PRICES.keys())}")
            continue

        # Validate quantity
        if not qty_str.isdigit() or int(qty_str) <= 0:
            print("  ⚠  Quantity must be a positive whole number.")
            continue

        quantity = int(qty_str)

        # If stock already added, update quantity
        if symbol in portfolio:
            portfolio[symbol] += quantity
            print(f"  ✅ Updated {symbol} — total quantity: {portfolio[symbol]}")
        else:
            portfolio[symbol] = quantity
            print(f"  ✅ Added {symbol} x{quantity}")

    return portfolio


def calculate_portfolio(portfolio):
    """Calculate individual and total investment values."""
    results = []
    total = 0

    for symbol, quantity in portfolio.items():
        price = STOCK_PRICES[symbol]
        value = price * quantity
        total += value
        results.append({
            "symbol":   symbol,
            "quantity": quantity,
            "price":    price,
            "value":    value
        })

    return results, total


def display_portfolio(results, total):
    """Print a formatted portfolio summary."""
    print("\n" + "=" * 50)
    print("        💼 Your Stock Portfolio Summary")
    print("=" * 50)
    print(f"  {'Stock':<8} {'Qty':>5}   {'Price':>10}   {'Value':>12}")
    print("  " + "-" * 44)

    for row in results:
        print(f"  {row['symbol']:<8} {row['quantity']:>5}   ${row['price']:>9}   ${row['value']:>11,}")

    print("  " + "-" * 44)
    print(f"  {'TOTAL INVESTMENT':>34}   ${total:>11,}")
    print("=" * 50)


def save_to_file(results, total):
    """Save the portfolio summary to a CSV and a TXT file."""

    # ── Save as CSV ───────────────────────────────────────────────────────────
    csv_filename = "portfolio_summary.csv"
    with open(csv_filename, "w", newline="") as csvfile:
        fieldnames = ["Stock", "Quantity", "Price (USD)", "Total Value (USD)"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in results:
            writer.writerow({
                "Stock":              row["symbol"],
                "Quantity":           row["quantity"],
                "Price (USD)":        row["price"],
                "Total Value (USD)":  row["value"]
            })
        writer.writerow({
            "Stock": "TOTAL", "Quantity": "", "Price (USD)": "", "Total Value (USD)": total
        })
    print(f"\n  📄 CSV saved  → {os.path.abspath(csv_filename)}")

    # ── Save as TXT ───────────────────────────────────────────────────────────
    txt_filename = "portfolio_summary.txt"
    with open(txt_filename, "w") as txtfile:
        txtfile.write("Stock Portfolio Summary\n")
        txtfile.write("=" * 40 + "\n")
        txtfile.write(f"{'Stock':<8} {'Qty':>5}   {'Price':>10}   {'Value':>12}\n")
        txtfile.write("-" * 40 + "\n")
        for row in results:
            txtfile.write(
                f"{row['symbol']:<8} {row['quantity']:>5}   ${row['price']:>9}   ${row['value']:>11,}\n"
            )
        txtfile.write("-" * 40 + "\n")
        txtfile.write(f"{'TOTAL':>34}   ${total:>11,}\n")
    print(f"  📄 TXT saved  → {os.path.abspath(txt_filename)}")


def main():
    print("\n" + "=" * 40)
    print("   💹 Welcome to Stock Portfolio Tracker")
    print("=" * 40)

    while True:
        # Step 1 — Show available stocks
        show_available_stocks()

        # Step 2 — Get user's portfolio
        portfolio = get_portfolio()

        # Step 3 — Calculate values
        results, total = calculate_portfolio(portfolio)

        # Step 4 — Display summary
        display_portfolio(results, total)

        # Step 5 — Ask to save
        save = input("\n  💾 Save results to CSV & TXT file? (y/n): ").strip().lower()
        if save == "y":
            save_to_file(results, total)

        # Step 6 — Play again?
        again = input("\n  🔄 Track another portfolio? (y/n): ").strip().lower()
        if again != "y":
            print("\n  Thank you for using Stock Portfolio Tracker! Goodbye 👋\n")
            break


if __name__ == "__main__":
    main()