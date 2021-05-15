company_name = input()
adult_tickets_count = int(input())
kids_tickets_count = int(input())
adult_ticket_price = float(input())
service_price = float(input())

kids_ticket_price = adult_ticket_price - (adult_ticket_price * 0.7)
adult_ticket_price = adult_ticket_price + service_price
kids_ticket_price += service_price

income = (kids_tickets_count * kids_ticket_price) + (adult_tickets_count * adult_ticket_price)
pure_income = income * 0.2

print(f"The profit of your agency from {company_name} tickets is {pure_income:.2f} lv.")
