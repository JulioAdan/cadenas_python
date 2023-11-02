#Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa y muestra por pantalla, el día, el mes y el año. Adaptar el programa anterior para que también funcione cuando el día o el mes se introduzcan con un solo carácter.

fecha=input("ingrese su fecha de nacimiento en el formato dd/mm/aaaa: ")
dia=("dia "+fecha[:fecha.find("/")]) 
mesanio=(fecha[fecha.find("/")+1:])
mes=(" mes "+ mesanio[:mesanio.find("/")])
anio=(" año "+ mesanio[mesanio.find("/")+1:])
print(dia + mes+ anio)