if week_day == 1 or week_day == 2:
    print('you win a 10 percent discount')
    discount = subtotal * 0.1
    subtotal = subtotal * 0.9
else:
    print('Thanks for your shop')

taxes = subtotal * 0.06
total = taxes + subtotal
