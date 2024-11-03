my_dict = {'water': 34, 'juece': 13, 'tea': 56, 'coffe': 17}
print(my_dict)
print(my_dict['water'])
print(my_dict.get('pulpi'), 'no such key')
my_dict.update({'energy': 52,
                'beer': 24})
del my_dict['tea']
print(my_dict)

my_set = {1, 2, 3, 4, 1, 4, 3, 2, (1, 2, 3), 'sport'}
print(my_set)
my_set.add('meat')
my_set.add('rock')
print(my_set.discard(1))
print(my_set)