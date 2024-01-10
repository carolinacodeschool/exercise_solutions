
total_bill = int(input('Total bill amount? '))
level_of_service = input('Level of service? ')
split_how_many = int(input('Split how many ways? '))

tip_text = 'Tip amount: %.2f'
tip = 0.0

total_text = 'Total amount: %.2f'

if level_of_service == 'good':
  tip = total_bill * 0.2
elif level_of_service == 'fair':
  tip = total_bill * 0.15
elif level_of_service == 'bad':
  tip = total_bill * 0.1

grand_total = total_bill + tip
per_person = grand_total / split_how_many
per_person_text = 'Amount per person: %.2f'

print(tip_text % tip)
print(total_text % grand_total)
print(per_person_text % per_person)
