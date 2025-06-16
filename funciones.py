import os, time

entradas=[]
def menu_principal():
    nombre=input("Nombre del comprador: ")
    if nombre in entradas:
        print("el comprador ya tiene su entrada.")
        return
    tp_entrada = input("Tipo de entrada (6 o V)")
    cdg = input("configuracion de codigo()")

    entrada= {
        "comprador": nombre,
        "entrada": tp_entrada,
        "codigo": cdg
    }
    entradas.append(entrada)
    print("Entrada comprada con exito")
    time.sleep(3)
    os.system('cls')

def consultar_comprador(entradas):
    print("consultar comprador")
    nombre =input("ingrese nombre del comprador: ")
    encontrado=False
    for entrada in entradas: