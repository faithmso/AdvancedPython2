
class FirstHundredGenerator:
    def __init__(self):
        self.number = 0

    def __next__(self):
        if self.number < 100:
            current = self.number
            self.number += 1
            return current
        else:
            raise StopIteration

    def __iter__(self):
        return self


friends = ['Rolf', 'Jose', 'Randy', 'Anna', 'Mary']
starts_with_r = filter(lambda friend: friend.startswith('R'), friends)

another_starts_with_r = (f for f in friends if f.startswith('R'))


def my_custom_filter(func, iterable):
    for i in iterable:
        if func(i):
            yield i


friends_lower = map(lambda x: x.lower(), friends)
friends_lower_again = (friend.lower() for friend in friends)
friends_lower_again_again = [friend.lower for friend in friends]
print(list(starts_with_r))


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @classmethod
    def from_dict(cls, data):
        return cls(data['username'], data['password'])


users = [
    {'username':'Rolf', 'password': '123'},
    {'username': 'Anne', 'password': 'Wanja1'}
]

users_use = [User.from_dict(user) for user in users]
users_use1 = map(User.from_dict, users)

"""
How the argument unpacking works differently for tuples and for dictionaries. For named arguments and for positional arguments.
"""
users2 = [User(**data) for data in users]


users4 = [
    ('Rolf', '123'),
    ('Anne', 'Wanja1')
]

user_object = [users4(*data) for data in users4]
