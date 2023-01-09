

friends_last_seen = {
    'Rolf': 31,
    'Jen': 5,
    'Anne': 20
}


def see_friend(friends, name):
    print(id(friends))
    friends[name] = 0


print(id(friends_last_seen))
print(id(friends_last_seen['Rolf']))

see_friend(friends_last_seen, 'Rolf')

print(id(friends_last_seen['Rolf']))
print(id(friends_last_seen))

print(friends_last_seen)

accounts = {
    'checking': 1958.00,
    'savings': 3695.50
}


def add_balance(amount: float, name: str = 'checking'):
    accounts[name] += amount
    return accounts[name]


add_balance(500.00)

print(accounts['checking'])

transactions = [
    (-180.67, 'checking'),
    (-220.00, 'checking'),
    (220.00, 'savings'),
    (600.50, 'savings'),
    (-59.50, 'checking'),
]

for t in transactions:
    add_balance(*t)


def create_account(name: str, holder: str, account_holders=None):
    if not account_holders:
        account_holders = []
    account_holders.append(holder)

    return{
        'name': name,
        'main_account_holder': holder,
        'account_holder': account_holders
    }


a1 = create_account('checking', 'Rolf', ['Anne'])
a2 = create_account('savings', 'Jen')

print(a2)
print(a1)