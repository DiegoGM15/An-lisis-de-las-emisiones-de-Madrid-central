import pandas as pd
import matplotlib.pyplot as plt
from datetime import date                           # Para trabajar con fechas
                       # Para trabajar con horas
from datetime import datetime
from dateutil.relativedelta import relativedelta 
import ejercicio73_funciones

tabla = pd.read_csv('c:/nueva/ejercicio73/emisiones-madrid.csv', sep=',', decimal='.')

estacion = tabla['ESTACION'].unique().tolist()
magnitud = tabla['MAGNITUD'].unique().tolist()
copiatabla = tabla.melt(id_vars=['ESTACION', 'MAGNITUD', 'ANO', 'MES'], var_name='DIA', value_name='VALOR')
copiatabla['ESTACION'] = copiatabla['ESTACION'].astype(str)
copiatabla['MAGNITUD'] = copiatabla['MAGNITUD'].astype(str)
copiatabla['MES'] = copiatabla['MES'].astype(str)

copiatabla['ANO'] = copiatabla['ANO'].astype(str)
guion = '-'
copiatabla['ANO'] = copiatabla['ANO'] + guion

copiatabla['DIA'] = copiatabla['DIA'].astype(str)
copiatabla['DIA'] = copiatabla['DIA'].str.replace('D', '-')

copiatabla['FECHA'] = copiatabla.loc[copiatabla.index, 'ANO'] + copiatabla.loc[copiatabla.index, 'MES'] + copiatabla.loc[copiatabla.index, 'DIA']
copiatabla['FECHA'] = copiatabla['FECHA'].astype(str)
copiatabla['FECHA'] = pd.to_datetime(copiatabla['FECHA'], format='%Y-%m-%d', errors='coerce')
copiatabla = copiatabla.dropna(subset="FECHA")
copiatabla = copiatabla.sort_values(by='FECHA')

copiatabla.to_csv('c:/nueva/ejercicio73/copiatabla.csv',sep=';', decimal=',')

fechafin = "2019-04-30"
fechainicio = "2018-01-01"
objfechaini = datetime.strptime(fechainicio, "%Y-%m-%d")
objfechafin = datetime.strptime(fechafin, "%Y-%m-%d")

estaciones = pd.Series({ '1':'P. Recoletos', '2':'Glta. de Carlos V', '35':'Pza. del Carmen', '4':'Pza. de España', '39':'Barrio del Pilar', '6':'Pza. Marañon', '7':'Pza. Salamanca', '8':'Escuelas Aguirre', '9':'Pza. Luca de Tena', '38':'Cuatro Caminos', '11':'Av. Ramón y Cajal', '12':'Pza. Manuel Becerra', '40':'Vallecas', '14':'Pza. Ladreda', '15':'Pza. Castilla', '16':'Arturo Soria', '17':'Villaverde Alto', '18':'Calle Farolillo', '19':'Huerta Castañeda', '36':'Moratalaz', '21':'Pza. Cristo Rey', '22':'P. Pontones', '23':'Calle Alcala', '24':'Casa de Campo', '25':'Santa Eugenia', '26':'Urb. Embajada', '27':'Barajas', '47':'Mendez Alvaro', '48':'P. Castellana', '49':'Retiro', '50':'Pza. Castilla', '54':'Ensanche Vallecas', '55':'Urb. Embajada', '56':'Plaza Elíptica', '57':'Sanchinarro', '58':'El Pardo', '59':'Parque Juan Carlos I', '60':'Tres Olivos' })
magnitudes = pd.Series({'1':'Dioxido de Azufre', '6':'Monoxido de Carbono', '7':'Monoxido de Nitrogeno', '8':'Dioxido de Nitrogeno', '9':'Partículas < 2.5', '10':'Partículas < 10', '12':'Oxidos de Nitrogeno', '14':'Ozono', '20':'Tolueno', '30':'Benceno', '35':'Etilbenceno', '37':'Metaxileno', '38':'Paraxileno', '39':'Ortoxileno', '42':'Hidrocarburos totales', '43':'Metano', '44':'Hidrocarburosno metanicos'})

meses = ['1','2','3','4','5','6','7','8','9','10','11','12']
menor = ''
mayor = ''
testigo = False
testigo1 = False
testigo2 = False
testigo3 = False
testigo4 = False

while(testigo4 == False):

    mes =  input("Introduce un mes: ")

    if (mes in meses):
        
        print("El mes esta bien")
        testigo4 = True

    else:

        print("El mes es incorrecto")
        testigo4 = False

while(testigo == False):

    print(estaciones.values)
    estacion = input("Introduce el nombre de la estacion: ")

    if(estacion in estaciones.values):

        print("La estacion está")
        testigo = True
    
    else: 

        print("La estación no está")
        testigo = False

while(testigo3 == False):

    print(magnitudes.values)
    contaminante = input("Introduce el nombre del contaminante: ")

    if(contaminante in magnitudes.values):

        print("El contaminante está")
        testigo3 = True
    
    else: 

        print("El contaminante no está")
        testigo3 = False

while(testigo1 == False):

    print("El rango de fecha a buscar es entre 2018-01-01 y 2019-04-30")
    inicio = input("Introduce la primera fecha(formato: año-mes-dia/xxxx-xx-xx): ")
    fin = input("Introduce la segunda fecha(formato: año-mes-dia/xxxx-xx-xx): ")

    if (len(inicio) != 10) or (len(fin) != 10):

        testigo1 = False

    elif(len(inicio) == 10) and (len(fin) == 10):

        testigo1 = True
        objinicio = datetime.strptime(inicio, "%Y-%m-%d")
        objfin = datetime.strptime(fin, "%Y-%m-%d")

        if(objinicio < objfechaini) or (objfin > objfechafin):

            testigo1 = False
            print("Las fechas introducidas son erroneas")
        
        elif(objinicio < objfin):

            testigo1 = True
            menor = objinicio
            mayor = objfin
            print("Las fechas estan bien")

        else: 

            menor  = objfin
            mayor = objinicio
            testigo1 = True
            print("Las fechas estan bien")

resultado = ejercicio73_funciones.magnitud_estacion(estacion,contaminante)
resultado1 = ejercicio73_funciones.medias_magnitudes(mes,estacion)
resultado2 = ejercicio73_funciones.medias_estaciones(mes,contaminante)
resultado3 = ejercicio73_funciones.medidas_fechas(menor,mayor,estacion)
resultado4 = ejercicio73_funciones.medidas_magnitud(menor,mayor,contaminante)
resultado5 = ejercicio73_funciones.medias_mensuales(contaminante)
resultado6 = ejercicio73_funciones.medias_madrid(mes,contaminante)
print(resultado6)
resultado7 = ejercicio73_funciones.medias_mensual_grafico(contaminante)


