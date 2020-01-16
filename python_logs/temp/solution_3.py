#!/usr/bin/python3
#!/usr/bin/python3
nombre = input()
lenguaje = input()

group = (len(nombre) % 2 == 0) + (lenguaje == 'Python3')
if group == 0:
    print('{} es un completo extraño.'.format(nombre))
elif group == 1:
    print('Con {} se puede programar.'.format(nombre))
else:
    print('Mi primo tiene un nuevo amigo, {}.'.format(nombre))
