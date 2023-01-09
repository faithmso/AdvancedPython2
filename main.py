from collections import Counter
from collections import defaultdict
from collections import OrderedDict
from collections import namedtuple
from collections import deque


friends = [
    {
        'name':'Rolf',
        'location': 'Washington D.C.'
    },
    {
        'name': 'Charlie',
        'location':'San Francisco'
    },
    {
        'name': 'Jose',
        'location': 'San Francisco'
    },
    {
        'name': 'Anna',
        'location': 'San Francisco'
    }
]

your_location = input('Where are you right now? ')
friends_nearby = [friend for friend in friends if friend ['location'] == your_location]

if any(friends_nearby):
    print('You are not alone')


"""
counter
defaultdict
orderdict
namedtuple
deque
"""


device_temperatures = [13.5, 14.0, 14.5, 14.5, 15.0, 16.0, 18.0, 14.0 ]

temperature_counter = Counter(device_temperatures)
print(temperature_counter[14.0])


coworkers = [('Rolf', 'Mit'), ('Jen', 'Oxford'), ('Charlie', 'Manchester'), ('Anne', 'Yale'), ('Rolf', 'Cambridge')]

alma_mater = defaultdict(list)

for coworker, place in coworkers:
    alma_mater[coworker].append(place)


print(alma_mater['Rolf'])


my_company = 'Teclado'

coworkers = ['Jen', 'Li', 'Charlie', 'Rhys']
other_coworkers = [('Rolf', 'Apple Inc'), ('Anna', 'Google')]

coworkers_company = defaultdict(lambda : my_company)

for person, company in other_coworkers:
    coworkers_company[person] = company


print(coworkers_company[coworker[0]])
print(coworkers_company['Rolf'])


o = OrderedDict()
o['Rolf'] = 6
o['Jose'] = 12
o['Jen'] = 3

print(o)

o.move_to_end('Rolf')
o.move_to_end('Jen', last=False)

print(o)

o.popitem()

print(o)


unnamed_account = ('checking', 1850.00)

Account = namedtuple('Account', ['name', 'balance'])
account = Account('checking', 1850.90)
accountNamedTuple = Account(* account)
print(accountNamedTuple._asdict())


People = deque(('Rolf', 'Charlie', 'Jen', 'Anna'))
People.append('Jose')
People.appendleft('Anthony')

print(People)
