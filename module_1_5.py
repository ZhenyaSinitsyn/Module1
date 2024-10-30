immutable_var = 1, 19, 'run'
print(immutable_var)
immutable_var = tuple([4, 19, 'run'])
print(immutable_var)
# Главное свойтво кортежа - неизменность содержимого кортежа
mutable_list = ['urban', 13]
print(mutable_list)
mutable_list[1] = 'two'
mutable_list[0] = 2024
print(mutable_list)