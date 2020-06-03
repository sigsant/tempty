import datetime
import argparse
import webbrowser

class Tiempo:
    def __init__(self, horas, minutos):
        self.horas = horas
        self.minutos = minutos

#Argumentos del programa
parser = argparse.ArgumentParser(description='Alarma de reloj que abre el navegador a una hora establecida')
parser.add_argument('time', type=str, help='hora a la que se programa la alarma en formato hh:mm')
args = parser.parse_args()

#1.Obtiene la hora actual
date_time = datetime.datetime.now()
current_hours = date_time.hour
current_minutes = date_time.minute

## Tiempo de usuario local ##
tiempoUsuario = Tiempo(current_hours, current_minutes)

#2.Formatea la hora introducida por el usuario
def formatoHora(user_time):
    user_time_num = int(user_time.replace(':', ''))
    hour_num = int(user_time_num / 100)
    minute_num = user_time_num % 100
    return (hour_num,minute_num)

## Tiempo programado a partir de la linea de comandos ##
horas, minutos = formatoHora(args.time)
tiempoProgramado = Tiempo(horas, minutos)

#3.Establece la hora programada
### TODO: Añadir en esta función un loop para que cumpla la condición y lea un fichero externo.
def horaProgramada(horas_user, horas_progr, minutos_user, minutos_progr):
    if horas_user == horas_progr and tiempoUsuario.minutos == minutos:
        print('La hora concuerda')
    else:
        print('No concuerda la hora')


horaProgramada(tiempoUsuario.horas, tiempoProgramado.horas,tiempoUsuario.minutos,tiempoProgramado.minutos)

def readFile():
    with open('videos_url.txt') as f:
        content = f.readline()
        webbrowser.open_new_tab(content)
        
print(readFile())