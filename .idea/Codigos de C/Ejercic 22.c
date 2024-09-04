#include <stdio.h>

struct Estudiante{
    char Nombre[30];
    int Matricula;
    int Semestre;
    int Promedio[Semestre];
    char Carrera[30];
}:

main()
{
    char agregar;
    Estudiante Datos[20]; //Maximo 20 estudiantes

    printf("Quieres agregar datos?: ");
    fflush(stdio);
    scanf("%c", &agregar);

    while(agregar == 's')
    {
        
    }
}