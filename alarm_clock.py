import datetime
import time
import argparse
import webbrowser
import sys


#Argumentos del programa
parser = argparse.ArgumentParser(description='Alarma de reloj que abre el navegador a una hora establecida')
parser.add_argument('horario', type=str, help='Hora programada en formato hh:mm')
parser.add_argument('fichero', type=str, help='Nombre del fichero que se abre en el navegador')
args = parser.parse_args()

def readFile(filename):
    with open( filename + '.txt') as f:
        content = f.readline()
        webbrowser.open_new_tab(content)

#2.Formatea la hora introducida por el usuario
def formatoHora(user_time):
    user_time_num = int(user_time.replace(':', ''))
    hour_num = int(user_time_num / 100)
    minute_num = user_time_num % 100
    return (hour_num,minute_num)

## Tiempo programado a partir de la linea de comandos ##
horas, minutos = formatoHora(args.horario)


#3.Establece la hora programada
def horaProgramada(horas_user, horas_progr, minutos_user, minutos_progr):
    if (horas_user == horas_progr) and (minutos_user == minutos_progr):
        print('Correcto')
        readFile(args.fichero)
        sys.exit('Ha terminado la ejecución correctamente')
    else: 
        print('Error...\n')
        time.sleep(20)

while True:
    #Actualiza la hora y minutos local cada 30 segundos
    date_time = datetime.datetime.now()
    current_hours = date_time.hour
    current_minutes = date_time.minute
    print(f'Hora local: {current_hours}:{current_minutes}')
    print(f'Hora Programada: {horas}:{minutos}\n')

    print('Esperando a la ejecución...')
    horaProgramada(current_hours, horas, current_minutes, minutos)
