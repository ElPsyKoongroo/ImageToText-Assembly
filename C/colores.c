#include <math.h>
#include <process.h>
#include <stdio.h>
#include <stdlib.h>

#define PIXELES 85
#define ROJO 0
#define VERDE 1
#define AZUL 2
#define DOSBOX_LINES 320
#define RGB 3
#define n_colors 256

const char *inicio_practica = ".model small\n\
.stack 200h\n\
.code\n\
    \n\
    mov al, 13h\n\
    mov ah, 0\n\
    int 10h\n\
\n\
    mov ax, 0A000h\n\
    mov es, ax\n\
\n\
    mov ax, 0 ;total de pantallas   printeadas\n\
\n\
    mov bx, 0 ;total de lineas      printeadas\n\
\n\
    mov cx, 0 ;total de PIXELES     printeados\n\
    \n\
\n\
start:\n";

const char *final_practica = "\
inc ax\n\
    mov bx, 0\n\
    mov cx, 0\n\
\n\
    jmp start\n\
end";

const int colors[][RGB] = {
    {0, 0, 0},       {0, 0, 170},     {0, 170, 0},     {0, 170, 170},
    {170, 0, 0},     {170, 0, 170},   {170, 85, 0},    {170, 170, 170},
    {85, 85, 85},    {85, 85, 255},   {85, 255, 85},   {85, 255, 255},
    {255, 85, 85},   {255, 85, 255},  {255, 255, 85},  {255, 255, 255},
    {0, 0, 0},       {20, 20, 20},    {32, 32, 32},    {44, 44, 44},
    {56, 56, 56},    {69, 69, 69},    {81, 81, 81},    {97, 97, 97},
    {113, 113, 113}, {130, 130, 130}, {146, 146, 146}, {162, 162, 162},
    {182, 182, 182}, {203, 203, 203}, {227, 227, 227}, {255, 255, 255},
    {0, 0, 255},     {65, 0, 255},    {125, 0, 255},   {190, 0, 255},
    {255, 0, 255},   {255, 0, 190},   {255, 0, 125},   {255, 0, 65},
    {255, 0, 0},     {255, 65, 0},    {255, 125, 0},   {255, 190, 0},
    {255, 255, 0},   {190, 255, 0},   {125, 255, 0},   {65, 255, 0},
    {0, 255, 0},     {0, 255, 65},    {0, 255, 125},   {0, 255, 190},
    {0, 255, 255},   {0, 190, 255},   {0, 125, 255},   {0, 65, 255},
    {125, 125, 255}, {158, 125, 255}, {190, 125, 255}, {223, 125, 255},
    {255, 125, 255}, {255, 125, 223}, {255, 125, 190}, {255, 125, 158},
    {255, 125, 125}, {255, 158, 125}, {255, 190, 125}, {255, 223, 125},
    {255, 255, 125}, {223, 255, 125}, {190, 255, 125}, {158, 255, 125},
    {125, 255, 125}, {125, 255, 158}, {125, 255, 190}, {125, 255, 223},
    {125, 255, 255}, {125, 223, 255}, {125, 190, 255}, {125, 158, 255},
    {182, 182, 255}, {199, 182, 255}, {219, 182, 255}, {235, 182, 255},
    {255, 182, 255}, {255, 182, 235}, {255, 182, 219}, {255, 182, 199},
    {255, 182, 182}, {255, 199, 182}, {255, 219, 182}, {255, 235, 182},
    {255, 255, 182}, {235, 255, 182}, {219, 255, 182}, {199, 255, 182},
    {182, 255, 182}, {182, 255, 199}, {182, 255, 219}, {182, 255, 235},
    {182, 255, 255}, {182, 235, 255}, {182, 219, 255}, {182, 199, 255},
    {0, 0, 113},     {28, 0, 113},    {56, 0, 113},    {85, 0, 113},
    {113, 0, 113},   {113, 0, 85},    {113, 0, 56},    {113, 0, 28},
    {113, 0, 0},     {113, 28, 0},    {113, 56, 0},    {113, 85, 0},
    {113, 113, 0},   {85, 113, 0},    {56, 113, 0},    {28, 113, 0},
    {0, 113, 0},     {0, 113, 28},    {0, 113, 56},    {0, 113, 85},
    {0, 113, 113},   {0, 85, 113},    {0, 56, 113},    {0, 28, 113},
    {56, 56, 113},   {69, 56, 113},   {85, 56, 113},   {97, 56, 113},
    {113, 56, 113},  {113, 56, 97},   {113, 56, 85},   {113, 56, 69},
    {113, 56, 56},   {113, 69, 56},   {113, 85, 56},   {113, 97, 56},
    {113, 113, 56},  {97, 113, 56},   {85, 113, 56},   {69, 113, 56},
    {56, 113, 56},   {56, 113, 69},   {56, 113, 85},   {56, 113, 97},
    {56, 113, 113},  {56, 97, 113},   {56, 85, 113},   {56, 69, 113},
    {81, 81, 113},   {89, 81, 113},   {97, 81, 113},   {105, 81, 113},
    {113, 81, 113},  {113, 81, 105},  {113, 81, 97},   {113, 81, 89},
    {113, 81, 81},   {113, 89, 81},   {113, 97, 81},   {113, 105, 81},
    {113, 113, 81},  {105, 113, 81},  {97, 113, 81},   {89, 113, 81},
    {81, 113, 81},   {81, 113, 89},   {81, 113, 97},   {81, 113, 105},
    {81, 113, 113},  {81, 105, 113},  {81, 97, 113},   {81, 89, 113},
    {0, 0, 65},      {16, 0, 65},     {32, 0, 65},     {48, 0, 65},
    {65, 0, 65},     {65, 0, 48},     {65, 0, 32},     {65, 0, 16},
    {65, 0, 0},      {65, 16, 0},     {65, 32, 0},     {65, 48, 0},
    {65, 65, 0},     {48, 65, 0},     {32, 65, 0},     {16, 65, 0},
    {0, 65, 0},      {0, 65, 16},     {0, 65, 32},     {0, 65, 48},
    {0, 65, 65},     {0, 48, 65},     {0, 32, 65},     {0, 16, 65},
    {32, 32, 65},    {40, 32, 65},    {48, 32, 65},    {56, 32, 65},
    {65, 32, 65},    {65, 32, 56},    {65, 32, 48},    {65, 32, 40},
    {65, 32, 32},    {65, 40, 32},    {65, 48, 32},    {65, 56, 32},
    {65, 65, 32},    {56, 65, 32},    {48, 65, 32},    {40, 65, 32},
    {32, 65, 32},    {32, 65, 40},    {32, 65, 48},    {32, 65, 56},
    {32, 65, 65},    {32, 56, 65},    {32, 48, 65},    {32, 40, 65},
    {44, 44, 65},    {48, 44, 65},    {52, 44, 65},    {60, 44, 65},
    {65, 44, 65},    {65, 44, 60},    {65, 44, 52},    {65, 44, 48},
    {65, 44, 44},    {65, 48, 44},    {65, 52, 44},    {65, 60, 44},
    {65, 65, 44},    {60, 65, 44},    {52, 65, 44},    {48, 65, 44},
    {44, 65, 44},    {44, 65, 48},    {44, 65, 52},    {44, 65, 60},
    {44, 65, 65},    {44, 60, 65},    {44, 52, 65},    {44, 48, 65},
    {0, 0, 0},       {0, 0, 0},       {0, 0, 0},       {0, 0, 0},
    {0, 0, 0},       {0, 0, 0},       {0, 0, 0},       {0, 0, 0}};

void generate_asm(int color_matrix[PIXELES][PIXELES]) {

    int last_line = 0;
    int posicion = 0;
    int offset = DOSBOX_LINES - PIXELES - 1;

    FILE *asm_code = fopen("output.asm", "a");
    fprintf(asm_code, "%s\n", inicio_practica);

    for (int filas = 0; filas < PIXELES; filas++) {
        for (int columnas = 0; columnas < PIXELES; columnas++) {
            posicion = filas * DOSBOX_LINES + columnas;
            if (posicion / DOSBOX_LINES != last_line) {
                last_line = posicion / DOSBOX_LINES;
                fprintf(asm_code, "    inc bx\n");
                fprintf(asm_code, "   mov cx, 0\n");
            }
            fprintf(asm_code, "   mov di, %d\n", posicion + offset);
            fprintf(asm_code, "   mov es:[di], %d\n",
                    color_matrix[filas][columnas]);
            fprintf(asm_code, "   inc cx\n");
        }
    }

    fprintf(asm_code, "%s", final_practica);
    fclose(asm_code);
}

int get_key(int aux[RGB]) { return aux[ROJO] + aux[VERDE] + aux[AZUL]; }

int get_best_color(int request_red, int request_green, int request_blue) {
    int aux[n_colors][RGB];

    for (int i = 0; i < n_colors; i++) {
        int r_c = colors[i][ROJO];
        int g_c = colors[i][VERDE];
        int b_c = colors[i][AZUL];

        int rd = (int)pow(r_c - request_red, 2);
        int gd = (int)pow(g_c - request_green, 2);
        int bd = (int)pow(b_c - request_blue, 2);

        aux[i][ROJO] = rd;
        aux[i][VERDE] = gd;
        aux[i][AZUL] = bd;
    }

    int best_color_index = 0;
    for (int i = 0; i < n_colors - 1; i++) {
        if (get_key(aux[best_color_index]) > get_key(aux[i + 1])) {
            best_color_index = i;
        }
    }
    return best_color_index;
}

void generate_color_matrix(int image_colors[PIXELES][PIXELES][RGB]) {
    int matrix_color[PIXELES][PIXELES];

    for (int filas = 0; filas < PIXELES; filas++) {
        for (int columnas = 0; columnas < PIXELES; columnas++) {
            int closest = get_best_color(image_colors[filas][columnas][ROJO],
                                         image_colors[filas][columnas][VERDE],
                                         image_colors[filas][columnas][AZUL]);
            matrix_color[filas][columnas] = closest;
        }
    }
    generate_asm(matrix_color);
}

int main(int argc, char *argv) {

    int image_colors[PIXELES][PIXELES][RGB];

    FILE *asm_code = fopen("output.asm", "w");
    fclose(asm_code);

    FILE *f = fopen("colors.txt", "r");

    char buff[RGB] = {0};

    for (int fila = 0; fila < PIXELES; fila++) {
        for (int columna = 0; columna < PIXELES; columna++) {
            for (int color = 0; color < RGB; color++) {
                fscanf(f, "%3s", buff);
                image_colors[fila][columna][color] = atoi(buff);
            }
        }
    }

    fclose(f);
    generate_color_matrix(image_colors);
    return 0;
}