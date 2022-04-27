# IMAGE TO TEXT ASSLEMBLY 

## C version

Para poder usar la version escrita en C de <b>IMAGE TO TEXT ASSEMBLY</b> se necesitara:

    Interprete de python 3.6 o superior
        La libreria de OpenCV para python
    
    Compilador para C (preferiblemente GCC)

### Pasos para generar el archivo .asm:

1. Copiar la imagen que queramos en la carpeta con el nombre "arch.png".
2. Ejecutar <b>main.py</b>
3. Compilar colores.c
4. Ejecutar colores.exe
5. En la misma carpeta deberá haber quedado un archivo output.asm


### Posibles errores y correcion:

1. Que al compilar el output.asm en DosBox tengamos un error de compilacion
`FATAL OUT OF MEMORY`


Para solucionar ese error solo deberemos reducir la calidad de la imagen, se hace de la siguiente forma:

1. En **main.py** deberemos cambiar la variable `PIXELES` (linea 5) a una resolucion menor (70 por ejemplo)
2. En **colores.c** deberemos hacer casi lo mismo, deberemos cambiar `#define PIXELES 85` al mismo valor que hemos puesto el **main.py**. (`#define PIXELES 70`)

3. Volvemos a compilar **colores.c** y repetimos los pasos para generar el archivo.
    