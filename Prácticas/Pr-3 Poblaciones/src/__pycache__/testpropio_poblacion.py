from poblacion import *
print("===> Test de lee_poblaciones")
print(f"Leídos {len(RegistroPoblacion)} registros.")
print("\nMostrando los 3 primeros:")
print("\n".join(str(r) for r in RegistroPoblacion[:3]))
print("\nMostrando los 3 últimos:")
print("\n".join(str(r) for r in RegistroPoblacion[-3:]))
print("#############################################################\n")