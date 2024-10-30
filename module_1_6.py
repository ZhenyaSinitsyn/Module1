my_dict = {'water': 34, 'juece': 13, 'tea': 56, 'coffe': 17}
my_dict['water'] = 34
my_dict['pulpi'] = 11
my_dict.update({'energy': 52,
                'beer': 24})
del my_dict['tea']
print(my_dict)

my_set = [1, 2, 3, 4, 1, 4, 3, 2, (1, 2, 3), 'sport']
print(set(my_set))
my_set = {1, 2, 3, 4, 1, 4, 3, 2, (1, 2, 3), True, 'meat', 'sport'}
print(my_set.discard(1))
print(my_set)