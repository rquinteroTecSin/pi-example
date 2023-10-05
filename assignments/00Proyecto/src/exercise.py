#Importar la biblioteca de matplotlib para la realización de la gráfica  
from matplotlib import pyplot as plt

def mostrar_datos():
    #Colocar todas las listas para que lea todos los datos en cada función
    name, net_worth, age, nationality, gender = leer_datos()

    print("Datos del archivo... ")
    print("·····················")
    
    #Inicializar contador
    contador = 0
    #Leer los datos del archivo de forma ordenada
    for name, net_worth, age, nationality, gender in zip(name, net_worth, age, nationality, gender):
        print("Posición " + str(contador) + " >>>> " + name + ", " + net_worth + ", " + age + ", " + nationality + ", " + gender)
        contador = contador + 1
    print("Fin. Presiona <Enter> continuar... ")
    input()



def leer_datos():
    #Creación de las listas con el nombre de las variables 
    name = []
    net_worth = []
    age = []
    nationality = []
    gender = []

    #Abrir el archivo top_100_richest.csv, el cual contiene la base de datos
    with open('assignments/data/top_100_richest.csv','r') as f:
        for line in f:
            lista_fila = line.split(",")

            #Leer cada una de las columnas del archivo 
            name.append(lista_fila[1])
            net_worth.append(lista_fila[2])
            age.append(lista_fila[4])
            nationality.append(lista_fila[5])
            gender.append(lista_fila[6])

    return name, net_worth, age, nationality, gender



def promedio_edades():
    #Colocar todas las listas para que lea todos los datos en cada función
    name, net_worth, age, nationality, gender = leer_datos()

    #Eliminar el encabezado de la tabla del archivo
    del age[0]
    age_billionaires = [int(x) for x in age]
    
    lista_promedio = [] 

    #Cálculo del promedio de la edad de las 100 personas más ricas del mundo
    promedio = sum(age_billionaires)/len(age_billionaires)
    lista_promedio.append(promedio)

    #Imprimir la frase con el promedio de la edad
    print(f"El promedio de la edad de las 100 personas más ricas del mundo es de {promedio} años")



def cantidad_genero():
    #Colocar todas las listas para que lea todos los datos en cada función
    name, net_worth, age, nationality, gender = leer_datos()

    #Cálculo de la cantidad de hombres y mujeres usando la función count
    cantidad_femenino = gender.count("F\n")
    cantidad_masculino = gender.count("M\n")
    
    #Cálculo del porcentaje de hombres y mujeres
    porcentaje_mujeres = (cantidad_femenino * 100) / 100
    porcentaje_hombres = (cantidad_masculino * 100) / 100
    
    #Imprimir la frase con la cantidad de mujeres y hombres y el porcentaje 
    print(f"En la lista hay {cantidad_femenino} mujeres, las cuales representan el {porcentaje_mujeres}% del total")
    print(f"En la lista hay {cantidad_masculino} hombres, los cuales representan el {porcentaje_hombres}% del total")



def grafica_genero():
    #Colocar todas las listas para que lea todos los datos en cada función
    name, net_worth, age, nationality, gender = leer_datos()
    print("Grafico de la cantidad de hombres y mujeres")

    #Datos que contendrá el gráfico de barras
    cantidad_femenino = gender.count("F\n")
    cantidad_masculino = gender.count("M\n")

    femenino_masculino = ["Femenino", "Masculino"]
    cantidad = [cantidad_femenino, cantidad_masculino]

    #Coordenadas en el eje X para las barras
    xs = [i for i,_ in enumerate(femenino_masculino)]

    #Establecer los nombres de las columnas
    plt.bar(xs, cantidad)
    plt.ylabel("Cantidad")
    plt.title("Gráfico de la cantidad de hombres y mujeres")

    #Etiquetar el eje x con los géneros femenino y masculino
    plt.xticks([i for i,_ in enumerate(femenino_masculino)], femenino_masculino)
    
    #Guardar y mostrar el gráfico
    plt.savefig('grafico_barras.png')
    plt.show()



def main():  
    #Creación del menú de opciones
    print("··············································MENÚ··············································")
    print("(1) Mostrar datos de la lista de las 100 personas más ricas del mundo")
    print("(2) Mostrar promedio de las edades de las 100 personas más ricas del mundo")
    print("(3) Mostrar cantidad de hombres y mujeres de la lista de las 100 personas más ricas del mundo")
    print("(4) Mostrar gráfica de la cantidad de hombres y mujeres más ricas del mundo")
    print("(0) Terminar programa")
    print("································································································")
    
    #Elección del número para saber qué dato dará el programa
    print(">>¿QUÉ DESEA SABER?")
    num = int(input("Teclee un número: "))
    
    #Uso del ciclo while para poder repetir la instrucción
    while num != 0:
        if num == 1:
            mostrar_datos()
            print("································································································")
        elif num == 2:
            promedio_edades()
            print("································································································")
        elif num == 3:
            cantidad_genero()
            print("································································································")
        elif num == 4:
            grafica_genero()
            print("································································································")
        else:
            print("Por favor, digite una opción correcta")
            print("································································································")
            
        print(">>¿QUÉ DESEA SABER?")
        num = int(input("Teclee un número: "))
       

if __name__=='__main__':
     main()