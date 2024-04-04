import pandas as pd
import matplotlib.pyplot as plt
from datetime import date                           # Para trabajar con fechas
                       # Para trabajar con horas
from datetime import datetime

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

fechafin = "2018-11-15"
fechainicio = "2018-09-16"
objfechaini = datetime.strptime(fechainicio, "%Y-%m-%d")
objfechafin = datetime.strptime(fechafin, "%Y-%m-%d")

print(objfechafin)
print(objfechaini)
print(copiatabla['FECHA'].tail(10))
print(magnitud)
print(estacion)

estaciones = pd.Series({ '1':'P. Recoletos', '2':'Glta. de Carlos V', '35':'Pza. del Carmen', '4':'Pza. de España', '39':'Barrio del Pilar', '6':'Pza. Marañon', '7':'Pza. Salamanca', '8':'Escuelas Aguirre', '9':'Pza. Luca de Tena', '38':'Cuatro Caminos', '11':'Av. Ramón y Cajal', '12':'Pza. Manuel Becerra', '40':'Vallecas', '14':'Pza. Ladreda', '15':'Pza. Castilla', '16':'Arturo Soria', '17':'Villaverde Alto', '18':'Calle Farolillo', '19':'Huerta Castañeda', '36':'Moratalaz', '21':'Pza. Cristo Rey', '22':'P. Pontones', '23':'Calle Alcala', '24':'Casa de Campo', '25':'Santa Eugenia', '26':'Urb. Embajada', '27':'Barajas', '47':'Mendez Alvaro', '48':'P. Castellana', '49':'Retiro', '50':'Pza. Castilla', '54':'Ensanche Vallecas', '55':'Urb. Embajada', '56':'Plaza Elíptica', '57':'Sanchinarro', '58':'El Pardo', '59':'Parque Juan Carlos I', '60':'Tres Olivos' })
estaciones_invertidas = pd.Series(estaciones.index, index=estaciones.values)
magnitudes = pd.Series({'1':'Dioxido de Azufre', '6':'Monoxido de Carbono', '7':'Monoxido de Nitrogeno', '8':'Dioxido de Nitrogeno', '9':'Partículas < 2.5', '10':'Partículas < 10', '12':'Oxidos de Nitrogeno', '14':'Ozono', '20':'Tolueno', '30':'Benceno', '35':'Etilbenceno', '37':'Metaxileno', '38':'Paraxileno', '39':'Ortoxileno', '42':'Hidrocarburos totales', '43':'Metano', '44':'Hidrocarburosno metanicos'})
magnitudes_invertidas = pd.Series(magnitudes.index, index=magnitudes.values)
madrid_central = ['1','2','4','6','7','8','9','11','12','14','15','19','21','22','35','38','39','47','48','49','50','56']
fuera_madrid_central = ['16','17','18','23','24','25','26','27','36','40','54','55','57','58','59','60']

#pd.Series({'P.Recoletos':'1','Glta. de Carlos V':'2','Pza. de España': '4','Pza. Marañon':'6','Pza. Salamanca': '7','Escuelas Aguirre':'8', 'Pza. Luca de Tena':'9','Av. Ramón y Cajal':'11', 'Pza. Manuel Becerra':'12','Pza. Ladreda':'14'})

def magnitud_estacion(estacion,magnitud):

    cod_estacion = estaciones_invertidas[estacion]
    cod_magnitud = magnitudes_invertidas[magnitud]
    filtro = (copiatabla['ESTACION'] == cod_estacion) & (copiatabla['MAGNITUD'] == cod_magnitud)
    medicion = copiatabla.loc[filtro]
    medicion.to_csv('c:/nueva/ejercicio73/mediciones_estacion.csv', sep=';', decimal=',',index=False)

    return cod_estacion

#resultado = magnitud_estacion('Pza. de España','Monoxido de Carbono')

def medias_magnitudes(mes,estacion):

    cod_estacion = estaciones_invertidas[estacion]
    filtro = (copiatabla['MES'] == mes ) & (copiatabla['ESTACION'] == cod_estacion)
    mediatabla = copiatabla.loc[filtro]
    media = mediatabla.groupby('MAGNITUD')['VALOR'].mean().round(2).convert_dtypes()
    media.to_csv('c:/nueva/ejercicio73/medias_magnitudes.csv', sep=';', decimal=',')

    return media

#resultado1 = medias_magnitudes('11','Pza. de España')

def medias_estaciones(mes,magnitud):

    cod_magnitud = magnitudes_invertidas[magnitud]
    filtro = (copiatabla['MES'] == mes) & (copiatabla['MAGNITUD'] == cod_magnitud)
    mediatabla = copiatabla.loc[filtro]
    media = mediatabla.groupby('ESTACION')['VALOR'].mean().round(2).convert_dtypes()
    media.to_csv('c:/nueva/ejercicio73/medias_estaciones.csv', sep=';', decimal=',')

    return media

#resultado2 = medias_estaciones('11','Monoxido de Carbono')

def medidas_fechas(fecha1,fecha2,estacion):

    cod_estacion = estaciones_invertidas[estacion]
    filtro = (copiatabla['ESTACION'] == cod_estacion) & (copiatabla['FECHA'] >= fecha1) & (copiatabla['FECHA'] <= fecha2)
    tablafecha = copiatabla.loc[filtro] #Tabla filtrada 

    magnitudes = tablafecha['MAGNITUD'].unique() #Lista de magnitudes dentro de la tabla filtrada
    #return tablafecha

    for magnitud in magnitudes: #Recorro las magnitudes que hay dentro de la lista magnitud

        datos = tablafecha[tablafecha['MAGNITUD'] == magnitud]  #Filtro para dibujar las lineas 
        plt.plot(datos['FECHA'], datos['VALOR'], label= magnitud) 

    plt.xlabel('Fecha')
    plt.ylabel('Valores')
    plt.title(f'Evolución diaria de las magnitudes de {estacion} entre {fecha1} y {fecha2}')
    plt.legend(title='Codigo Magnitud', loc='best')
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.savefig("C:/nueva/ejercicio73/valores_magnitudes.png")
    plt.show()

#resultado3 = medidas_fechas(objfechaini, objfechafin,'Pza. de España')

def medidas_magnitud(fecha1,fecha2,magnitud):

    cod_magnitud = magnitudes_invertidas[magnitud]
    filtro = (copiatabla['MAGNITUD'] == cod_magnitud) & (copiatabla['FECHA'] >= fecha1) & (copiatabla['FECHA'] <= fecha2)
    tablafecha = copiatabla.loc[filtro]

    estaciones = tablafecha['ESTACION'].unique()

    for estacion in estaciones:

        datos = tablafecha[tablafecha['ESTACION'] == estacion]
        plt.plot(datos['FECHA'], datos['VALOR'], label= estacion)

    plt.xlabel('Fecha')
    plt.ylabel('Valores')
    plt.title(f'Evolución diaria de las estaciones de {magnitud} entre {fecha1} y {fecha2}')
    plt.legend(title='Codigo Estacion', loc='best')
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.savefig("C:/nueva/ejercicio73/valores_estaciones.png")
    plt.show()

#resultado4 = medidas_magnitud(objfechaini, objfechafin,'Monoxido de Carbono')

def medias_mensuales(magnitud):
 
    cod_magnitud = magnitudes_invertidas[magnitud]
    filtro = (copiatabla['MAGNITUD'] == cod_magnitud)
    tabla_magnitud = copiatabla.loc[filtro]
    #estaciones = tabla_magnitud['ESTACION'].unique()
    medias = tabla_magnitud.groupby(['ESTACION','MES']).VALOR.mean().round(2).convert_dtypes().unstack('MES')
    #return tabla_magnitud
    for estacion, filas in medias.iterrows():

        plt.plot(filas.index, filas.values, label= estacion)

    plt.xlabel('Mes')
    plt.ylabel('Media Mensual')
    plt.title(f'Media mensual del {magnitud} por estacion')
    plt.legend(title='Codigo Estacion', loc='best')
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.savefig('c:/nueva/ejercicio73/medias_mensuales.png')
    plt.show()
    return medias

resultado5 = medias_mensuales('Monoxido de Carbono')
print(resultado5)

def medias_madrid(mes,magnitud):

    cod_magnitud = magnitudes_invertidas[magnitud]
    filtrado_madrid_central = copiatabla[copiatabla.ESTACION.isin(madrid_central)]
    filtrado_fuera_madrid = copiatabla[copiatabla.ESTACION.isin(fuera_madrid_central)]

    filtrado_magnitud_madrid = filtrado_madrid_central[(filtrado_madrid_central['MAGNITUD'] == cod_magnitud) & (filtrado_madrid_central['MES'] == mes)]
    filtrado_magnitud_fuera = filtrado_fuera_madrid[(filtrado_fuera_madrid['MAGNITUD'] == cod_magnitud) & (filtrado_fuera_madrid['MES'] == mes)]
    media_madrid_central = filtrado_magnitud_madrid['VALOR'].mean().round(2)
    media_fuera_madrid = filtrado_magnitud_fuera['VALOR'].mean().round(2)
    medias = {'media dentro de Madrid': media_madrid_central,'media fuera de Madrid': media_fuera_madrid}
    #mensaje = (f'Media del {magnitud} en el mes {mes} en Madrid central {media_madrid_central} y {media_fuera_madrid} fuera de Madrid central')

    return medias

#resultado6 = medias_madrid('11','Monoxido de Carbono')
#print(resultado6)

def medias_mensual_grafico(magnitud):

    cod_magnitud = magnitudes_invertidas[magnitud]

    filtrado_madrid_central = copiatabla[copiatabla.ESTACION.isin(madrid_central)]
    filtrado_fuera_madrid = copiatabla[copiatabla.ESTACION.isin(fuera_madrid_central)]
    filtrado_magnitud_fuera = filtrado_fuera_madrid[(filtrado_fuera_madrid['MAGNITUD'] == cod_magnitud)]
    filtrado_magnitud_madrid = filtrado_madrid_central[(filtrado_madrid_central['MAGNITUD'] == cod_magnitud)]
    medias_madrid = filtrado_magnitud_madrid.groupby(['MES']).VALOR.mean().round(2).convert_dtypes()
    medias_fuera = filtrado_magnitud_fuera.groupby(['MES']).VALOR.mean().round(2).convert_dtypes()

    plt.plot(medias_madrid.index,medias_madrid.values, label='Madrid Central')
    plt.plot(medias_fuera.index,medias_fuera.values, label='Fuera de Madrid Central')
    plt.xlabel('Mes')
    plt.ylabel('Media Mensual')
    plt.title(f'Media mensual del {magnitud}')
    plt.legend(title='Localizacion', loc='best')
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.savefig('c:/nueva/ejercicio73/medias_madrid.png')
    plt.show()

    return medias_madrid

resultado7 = medias_mensual_grafico('Monoxido de Carbono')

print(resultado7)





















