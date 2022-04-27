#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <locale.h>


const int INSTRUCCIONES_POR_PX = 3;

int main(int argc, char** argv){
    const int PX_POR_LINEA = atoi(argv[1]);
    printf("%d\n", PX_POR_LINEA);
    int recuento_instrucciones, pantallas_dibujadas, lineas_dibujadas;
    double tiempo_ejecucion = 0.11;
    double MIPS;

    printf("Introduzca el numero de instrucciones: ");
    scanf("%d", &recuento_instrucciones);

    printf("Introduzca el numero de pantallas dibujadas: ");
    scanf("%d", &pantallas_dibujadas);

    printf("Introduzca el numero de lineas dibujadas: ");
    scanf("%d", &lineas_dibujadas);

    recuento_instrucciones = pantallas_dibujadas * (PX_POR_LINEA*INSTRUCCIONES_POR_PX*PX_POR_LINEA + PX_POR_LINEA*2);
    recuento_instrucciones += lineas_dibujadas*INSTRUCCIONES_POR_PX*PX_POR_LINEA + lineas_dibujadas*2;

    MIPS = recuento_instrucciones / (tiempo_ejecucion*pow(10,6));
    printf("MIPS =  %lf\n", MIPS);

    return 0;

}