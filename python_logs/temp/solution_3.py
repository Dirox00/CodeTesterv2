#!/usr/bin/python3
#!/usr/bin/python3
nombre = input()
lenguaje = input()

group = (len(nombre) % 2 == 0) + (lenguaje == 'Python3')
if group == 0:
    print(f'{nombre} es un completo extraño.')
elif group == 1:
    print(f'Con {nombre} se puede programar.')
else:
    print(f'Mi primo tiene un nuevo amigo, {nombre}.')
