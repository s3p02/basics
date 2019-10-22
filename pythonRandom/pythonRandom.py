import random

namesList = ["name1","name2","name3","name4"]

result = list(random.choices(namesList,k=10))
print(result)
print("\nSORTED\n")
r2 = sorted(result)
print(r2)