transactions_count = int(input())
counter_transactions = 0
total = 0
while transactions_count > counter_transactions:
    transaction_cash = float(input())
    if transaction_cash >= 1:
        total += transaction_cash
        counter_transactions += 1
        print(f'Increase: {transaction_cash:.2f}')
    elif transaction_cash < 1:
        print('Invalid operation!')
        break

print(f'Total: {total:.2f}')