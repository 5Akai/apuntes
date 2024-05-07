import asyncio

async def main():

    print("async main -> Hola .......")
    await asyncio.gather(func1(), func2())
    print("async main -> ....... Adios")

async def func1():

    print("async func1 -> Hola1 .......")
    await asyncio.sleep(5)
    print("async func1 -> ....... Adios1")

async def func2():

    print("async func2 -> Hola2 .......")
    for i in range(11):
        print(f"Async func2 -> {i}")
        await asyncio.sleep(0.6)

    print("async func2 -> ....... Adios2")


print ("Inicio Sync")
asyncio.run(main())
##El hilo principal, osea esta parte se ejecuta de manera SÍNCRONA, AUNQUE LO DECLARES ASÍNCRONO
print("Fin Sync")
print("")