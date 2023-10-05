import entrenos

datos = entrenos.lee_entrenos('.\data\entrenos.csv')
print(datos[0:3])
print(entrenos.tipos_entreno(datos))