# Tempty

Tempy es un temporizador básico que se ejecuta por línea de comandos que abre una ventana de tu navegador con el enlace contenido en un archivo de texto ubicado en el mismo directorio en el que se encuentra el programa. No depende de ninguna librería externa.

## Parámetros

El programa actualmente emplea dos argumentos obligatorios:

```sh
python tempty.py Hora fichero
```

- Hora: Es la hora programada para que se ejecute el programa en formato hh:mm. La aplicación comprobará la hora local cada 30 segundos por defecto.

- Fichero: Es el nombre del fichero en formato txt que incluye la URL que se abrirá en el navegador que el usuario tenga por defecto.

