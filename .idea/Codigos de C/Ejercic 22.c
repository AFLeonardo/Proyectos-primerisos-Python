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
    int i = 0;
    Estudiante Datos[20]; //Maximo 20 estudiantes

    printf("Quieres agregar datos?: ");
    fflush(stdio);
    scanf("%c", &agregar);

    while(agregar == 's' or i < 20)
    {
        printf({"Ingresa tu nombre: /n"});
        fflush(stdio)
        gets(Datos[i].Nombre)

        printf("Ingresa tu matricula: /n");
        gets(Datos[i].Matricula);

        printf("En que semestre te encuentras? /n");
        gets(Datos[i].Semestre)

        for (j = 0 ; j < Semestre ; j++)
        {
            printf("Ingresa el promedio del semestre %d/n", j + 1);
            gets(Datos[i].Promedio[j]);
        }

        printf("Ingresa tu carrera: /n");
        gets()
    }
}