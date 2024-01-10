# configure

prompt_total = 'Total bill amount? '
prompt_service = 'Level of service? '

tip_text = 'Tip amount: %.2f'
total_text = 'Total amount: %.2f'

LEVEL_GOOD = 'good'
LEVEL_FAIR = 'fair'
LEVEL_BAD = 'bad'

TIP_GOOD = 0.2
TIP_FAIR = 0.15
TIP_BAD = 0.1

tip = 0.0

# process

total_bill = float(input(prompt_total))
level_of_service = input(prompt_service).lower()

if level_of_service == LEVEL_GOOD:
  tip = total_bill * TIP_GOOD
elif level_of_service == LEVEL_FAIR:
  tip = total_bill * TIP_FAIR
elif level_of_service == LEVEL_BAD:
  tip = total_bill * TIP_BAD
else:
  print("Invalid input. They can't be that bad.")

# result


print(tip_text % tip)
print(total_text % (total_bill + tip))
