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
    int i = 0, j;
    Estudiante Datos[20]; //Maximo 20 estudiantes

    printf("Quieres agregar datos?: ");
    fflush(stdio);
    scanf("%c", &agregar);

    while(agregar == 's' or i < 20)
    {
        printf({"Ingresa tu nombre: /n"});
        fflush(stdio)
        gets(Datos[i].Nombre)

        //Validacion de matricula mayor a 0
        do
        {
            printf("Ingresa tu matricula: /n");
            gets(Datos[i].Matricula);

            if (Datos[i].Matricula <= 0);
                printf("La matricula no puedo ser menor a 0. Intenta de nuevo./n");
        }
        while(Datos[i].Matricula <= 0);

        //Validar semestre 1 y 9

        do
        {
        printf("En que semestre te encuentras? /n");
        gets(Datos[i].Semestre)

        if (Datos[i.Semestre] < 1  Datos[i].Semestre > 9)
            printf("Semestres permitidos del 1 a 9. Intente de nuevo/n");
        }

        while(Datos[i].Semestre < 1 || Datos[i].Semestre > 9)
        
        for (j = 0 ; j < Semestre ; j++)
        {
            printf("Ingresa el promedio del semestre %d/n", j + 1);
            gets(Datos[i].Promedio[j]);
        }

        printf("Ingresa tu carrera: /n");
        gets(Datos[i].Carrera);

    }
}