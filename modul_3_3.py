def print_params(a=1, b='строка', c=True):
    print(a, b, c)


list_ = [1, 2, 3]
print_params()
print_params(b=25, c=list_)

values_list = [True, 'слово', 2]
values_dict = {'a': 'текст', 'b': True, 'c': 147}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [17, [1, 2, 3, ]]
print_params(*values_list_2, 42)
