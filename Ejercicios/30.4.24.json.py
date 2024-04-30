import json

frutas = ["naranja", "limón", "pomelo", "lima", "mandarina"]

frutasJSON = json.dumps(frutas)

print(f"Lista: {frutas}")

print(f"Posición 2: {frutas[2]}")

print(f"{type(frutas)}")

print(f"JSON: {frutasJSON}")

print(f"Posición 2: {frutasJSON[2]}")
print(f"{type(frutasJSON)}")

##Comversión  de JSON en objetos

frutas2 = json.loads(frutasJSON)

print(f"Lista: {frutas2}")
print(f"Posición 2: {frutas2[2]}")
print(f"{type(frutas2)}")