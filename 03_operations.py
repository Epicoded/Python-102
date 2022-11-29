set_a = {'col', 'mex', 'bol'}
set_b = {'pe', 'bol'}

#unifica conjuntos
set_c = set_a.union(set_b) 
print(set_c)
print(set_a | set_b)
print('* - ' * 10)
#muestra elementos que existen en los dos conjuntos
set_c = set_a.intersection(set_b) 
print(set_c)
print(set_a & set_b)
print('* - ' * 10)
#muestra elementos
set_c = set_a.difference(set_b)
print(set_c)
print(set_a - set_b)
print('* - ' * 10)
set_c = set_a.symmetric_difference(set_b)
print(set_c)
print(set_a ^ set_b)