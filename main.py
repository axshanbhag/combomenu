sandwiches = []
beverages = []
fries = []
total = 0.0

global sandwich_order
sandwich_order = ""
def get_sandwich_order():
  while True:
    sandwich_order = input("""What type of sandwich would you like to order? We have
  1. Chicken sandwiches for $5.25
  2. Beef sandwiches for $6.25
  3. Tofu sandwiches for $5.75
ALL LOWERCASE: """)
    if sandwich_order not in ["chicken", "beef", "tofu"]:
      print("You did not select a valid sandwich type.\nPlease try again.")
    else:
      sandwiches.append(sandwich_order)
      return sandwich_order

get_sandwich_order()

while True:
  extra_sandwiches = input("Would you like to order another sandwich? (yes/no): ")
  if extra_sandwiches not in ["yes", "no"]:
    print("Please select yes or no.")
  else: 
    if extra_sandwiches == "yes":
      get_sandwich_order()
    elif extra_sandwiches == "no":
      break

global beverage_order
beverage_order = ""
def get_beverage_order():
  while True:
    beverage_order = input("""What size beverage would you like to order? We have
  1. Small beverages for $1.00
  2. Medium beverages for $1.75
  3. Large beverages for $2.25
ALL LOWERCASE: """)
    if beverage_order not in ["small", "medium", "large"]:
      print("You did not select a valid beverage type.\nPlease try again.")
    else:
      beverages.append(beverage_order)
      return beverage_order

while True:
  get_beverage = input("Would you like a beverage? (yes/no): ")
  if get_beverage not in ["yes", "no"]:
    print("Please select yes or no.")
  else: 
    if get_beverage == "yes":
      get_beverage_order()
      while True:
        extra_beverages = input("Would you like to order another beverage? (yes/no): ")
        if extra_beverages not in ["yes", "no"]:
          print("Please select yes or no.")
        else: 
          if extra_beverages == "yes":
            get_beverage_order()
          elif extra_beverages == "no":
            break
      break
    elif get_beverage == "no":
      break

global fries_order
fries_order = ""
def get_fries_order():
    fries_true = True
    while True:
        fries_order = input("""What size fries would you like to order? We have
  1. Small fries for $1.00
  2. Medium fries for $1.50
  3. Large fries for $2.00
ALL LOWERCASE: """)
        if fries_order not in ["small", "medium", "large"]:
            print("You did not select a valid french fries type.\nPlease try again.")
        else:
            if fries_order == "small":
                while fries_true == True:
                    mega_size = input("Would you like to mega-size your fries? (yes/no): ")
                    if mega_size not in ["yes", "no"]:
                        print("Please select yes or no.")
                    if mega_size == "no":
                      fries_order = "small"
                      fries.append(fries_order)
                    elif mega_size == "yes":
                        print("You've mega-sized your fries!")
                    fries.append("mega-size")
                    fries_true = False
                    return fries_order

while True:
  get_fries = input("Would you like french fries? (yes/no): ")
  if get_fries not in ["yes", "no"]:
    print("Please select yes or no.")
  else: 
    if get_fries == "yes":
      get_fries_order()
      while True:
        extra_fries = input("Would you like to order another french fries? (yes/no): ")
        if extra_fries not in ["yes", "no"]:
          print("Please select yes or no.")
        else: 
          if extra_fries == "yes":
            get_fries_order()
          elif extra_fries == "no":
            break
      break
    elif get_fries == "no":
      break

while True:
  user_ketchup = input("""How many ketchup packets do you want? 
(Enter a positive integer; cost is $0.25 per packet): """)
  try:
    user_ketchup_int = int(user_ketchup)
    if user_ketchup_int < 0:
      raise ValueError
    print("You have ordered", user_ketchup_int, "ketchup packets.")
    total += user_ketchup_int * 0.25
    break
  except ValueError:
    print("You did not enter a valid amount of ketchup packets.")

      
print("Order Summary: ")
print("Sandwiches: ")
for sandwich in sandwiches:
  print(sandwich)
  if sandwich == "chicken":
    total += 5.25
  elif sandwich == "beef":
    total += 6.25
  elif sandwich == "tofu":
    total += 5.75
print("Beverages:")
if beverages == []:
  print("No beverages.")
else:
  for beverage in beverages:
    print(beverage)
    if beverage == "small":
      total += 1
    elif beverage == "medium":
      total += 1.75
    elif beverage == "large":
      total += 2.25
print("French Fries:")
if fries == []:
  print("No french fries.")
else:
  for french in fries:
    print(french)
    if french == "small":
      total += 1
    elif french == "medium":
      total += 1.5
    elif french == "large" or french == "mega-size":
      total += 2

print("Ketchup Packets:", user_ketchup_int if user_ketchup_int > 0 else "0")

while True:
  remove = input("Would you like to remove an item from your order? (yes/no): ")
  if remove not in ["yes", "no"]:
    print("Please select yes or no.")
  else: 
    if remove == "yes":
      while True:
        remove_item = input("What would you like to remove? (sandwich/beverage/fries): ")
        if remove_item not in ["sandwich", "beverage", "fries"]:
          print("Please select sandwich, beverage, or fries.")
        else: 
          if remove_item == "sandwich":
            remove_sandwich = int(input("What sandwich would you like to remove? (index values 0, 1, etc.): "))
            if remove_sandwich < 0 or remove_sandwich >= len(sandwiches):
                print("You did not select a valid sandwich index.")
            else:
                del sandwiches[remove_sandwich]
                print("Sandwich removed!")
                break
          elif remove_item == "beverage":
            remove_beverage = int(input("What beverage would you like to remove? (index values 0, 1, etc.): "))
            if remove_beverage < 0 or remove_beverage >= len(beverages):
              print("You did not select a valid beverage.")
            else:
              del beverages[remove_beverage]
              print("Beverage removed!")
              break
          elif remove_item == "fries":
            remove_fries = int(input("What fries would you like to remove? (index values 0, 1, etc.): "))
            if remove_fries < 0 or remove_fries >= len(fries):
              print("You did not select a valid fries.")
            else:
              del fries[remove_fries]
              print("Fries removed!")
              break
    elif remove == "no":
      break

print("New Order Summary: ")
print("Sandwiches: ")
for sandwich in sandwiches:
  print(sandwich)
  if sandwich == "chicken":
    total += 5.25
  elif sandwich == "beef":
    total += 6.25
  elif sandwich == "tofu":
    total += 5.75
print("Beverages:")
if beverages == []:
  print("No beverages.")
else:
  for beverage in beverages:
    print(beverage)
    if beverage == "small":
      total += 1
    elif beverage == "medium":
      total += 1.75
    elif beverage == "large":
      total += 2.25
print("French Fries:")
if fries == []:
  print("No french fries.")
else:
  for french in fries:
    print(french)
    if french == "small":
      total += 1
    elif french == "medium":
      total += 1.5
    elif french == "large" or french == "mega-size":
      total += 2

print("Ketchup Packets:", user_ketchup_int if user_ketchup_int > 0 else "0")

if sandwiches != [] and beverages != [] and fries != []:
  total -= 1.00
  print("You've received a $1.00 discount \nfor ordering a sandwich, beverage, and french fries.")
  print("Total Cost: $", str(total))

else:
  print("Total Cost: $", str(total))
