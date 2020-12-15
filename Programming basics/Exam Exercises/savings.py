monthly_income = float(input())
months_count = int(input())
expenses_sum = float(input())

savings = monthly_income * 0.30
monthly_savings = monthly_income - (expenses_sum + savings)
x_months_of_saving = monthly_savings * months_count
percent = monthly_savings / monthly_income
percent = percent * 100

print(f'She can save {percent:.2f}%')
print(f'{x_months_of_saving:.2f}')