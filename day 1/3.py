import oldMax
import random


users = [
    {
        'name': 'Jack',
        'password': '234567',
        'age': 10
    },
    {
        'name': 'Helen',
        'password': '98765',
        'age': 100
    },
]

print(oldMax.old_max(users)['name'])


for i in range(100):
    users.append({
        'name': oldMax.generate_name(),
        'password': oldMax.generate_name(),
        'age': random.randint(1, 100)
    })

print(users)

print(oldMax.old_max(users))