name = 'Sebastian'
last_name = 'Ibañez Rios'
edad = 18
print(name)
print(last_name)

full_name = name + " " + last_name
print(full_name)

quote = "I'm Sebastian"
print(quote)

quote2 = 'She said "Hello"'
print(quote2)

# Format 
template = "Hola, mi nombre es " + name + " y mi apellido es " + last_name
print('v1',template)

template = "Hola, mi nombre es {} y mi apellido es {}".format(name, last_name)
print('v2',template)

template = f"Hola, mi nombre es {name} y mi apellido es {last_name}"
print('v3', template)

template = f"Hola, mi nombre es {name} y mi apellido es {last_name} y mi edad es {edad}"
print('v3', template)