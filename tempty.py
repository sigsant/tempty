import datetime
from time import sleep
import random
import argparse
import webbrowser
import sys


#Argumentos del programa
parser = argparse.ArgumentParser(description='Alarma de reloj que abre el navegador a una hora establecida')
parser.add_argument('horario', type=str, help='Hora programada en formato hh:mm')
parser.add_argument('fichero', type=str, help='Nombre del fichero que se abre en el navegador')
args = parser.parse_args()

def loading():
    print('\nEsperando a la ejecución', end='')
    for x in range(0,10):
        print('.',end='', flush=True)
        sleep(1)

def readFile(filename):
    '''
    Lee al azar una linea del fichero y lo abre en una pestaña del navegador

    Parametro:
        filename(str): Nombre del fichero sin extension
    '''
    with open(filename + '.txt') as f:
        content = f.readlines()
        random_index = random.randint(0,2)
        webbrowser.open_new_tab(content[random_index])

def formatoHora(user_time):
    '''
    Divide el horario introducida por el usuario en fomato hora y minutos.

    Parametros: 
        user_time(str):  Horario definido por el usuario en el argumento[0]

    Return:
        horas(int):  hora con rango 0 - 23
        minutos(int): minutos con rango 0 - 59 
    '''
    user_time_num = int(user_time.replace(':', ''))
    horas = int(user_time_num / 100)
    minutos = user_time_num % 100
    return (horas, minutos)

def horaProgramada(horas_user, horas_progr, minutos_user, minutos_progr):
    '''
    Establece el comportamiento del temporizador.

    Si coincide inicia la función readFile() y sale del programa.
    Si no coincide, espera a que se ejecute 40 segundos después.

    Parametros:
        horas_user(int): Hora local del usuario.
        horas_progr(int): Hora programada por el usuario
        minutos_user(int): Minuto local del usuario
        minutos_progr(int): Minuto programado por el usuario.
    '''
    if (horas_user == horas_progr) and (minutos_user == minutos_progr):
        readFile(args.fichero)
        sys.exit('\n\nHa terminado la ejecución correctamente')
    else:
        sleep(30)

def main():

    ## Tiempo programado a partir de la linea de comandos ##
    horas, minutos = formatoHora(args.horario)

    while True:
        '''
        Actualiza el horario local y lo compara con el programado.
        '''
        date_time = datetime.datetime.now()
        current_hours = date_time.hour
        current_minutes = date_time.minute
        loading()
        horaProgramada(current_hours, horas, current_minutes, minutos)

main()
