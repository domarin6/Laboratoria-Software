# aerolinea

Antes de crear un entorno virtual es importante que clone el repositorio,
una vez clonado, cree el entorno virtual al mismo nivel que el repositorio.

es decir.

Carpeta X:


|____ repositorio.

|____ entorno virtual.

De esta manera se asegura que no se añadan carpetas o archivos de los entornos virtuales al github.

# Entorno virtual
 instalacion:
      pip install virtualenv
 
 Crear un entorno:
      virtualenv "nombre del entorno virtual"

### ¡Antes de usar el entorno debes activarlo, asi:!

source my-env/bin/activate

### Desactivar un entorno virtual
deactivate.
 
 # Instalacion de paquetes automaticos.
 ## Active el entorno virtual.
 
 Acceda a la carpeta del repositorio, alli encontrara un documento nombrado como requirements.txt
 En esa misma ubicacion lance una terminal y escriba lo siguiente.
 
 pip install -r requirements.txt
 
 De esta manera se asegura de tener los archivos con los que funciona el repositorio.
 
 # Actualizar el archivo requirements.
 Asegurese de tener activado el entorno virtual, cuando lo haga digite lo siguiente.
 
 pip list
 
 Eso desplegara los paquetes instalados en su entorno con la respectiva version. 
 #### Atencion! Si nota que la lista es muy larga quiza es porque no tiene activado el entorno virtual.
 
 Si requiere de algun modulo de python que vaya a instalar por medio de pip, digite la siguiente linea
 de codigo para actualizar el archivo requirement.
 
pip freeze > requirements.txt

de esta manerar sus compañeros podran trabajar con la misma version que usted al instalar el nuevo arquivo requirements.txt
 
 
 
