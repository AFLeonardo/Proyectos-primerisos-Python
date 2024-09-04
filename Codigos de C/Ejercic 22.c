#include <stdio.h>

struct Estudiante{
    char Nombre[30];
    int Matricula;
    int Semestre;
    int Promedio[10]; // Máximo 10 semestres
    char Carrera[30];
};

int main()
{
    char agregar;
    int i = 0, j;
    struct Estudiante Datos[20]; // Máximo 20 estudiantes

    printf("¿Quieres agregar datos? (s/n): ");
    fflush(stdin);
    scanf("%c", &agregar);

    while(agregar == 's' && i < 20)
    {
        printf("Ingresa tu nombre:\n");
        fflush(stdin);
        fgets(Datos[i].Nombre, 30, stdin);

        // Validación de matrícula mayor a 0
        do
        {
            printf("Ingresa tu matrícula:\n");
            scanf("%d", &Datos[i].Matricula);

            if (Datos[i].Matricula <= 0)
                printf("La matrícula no puede ser menor o igual a 0. Intenta de nuevo.\n");
        }
        while(Datos[i].Matricula <= 0);

        // Validar semestre entre 1 y 9
        do
        {
            printf("¿En qué semestre te encuentras?\n");
            scanf("%d", &Datos[i].Semestre);

            if (Datos[i].Semestre < 1 || Datos[i].Semestre > 9)
                printf("Semestres permitidos del 1 al 9. Intente de nuevo.\n");
        }
        while(Datos[i].Semestre < 1 || Datos[i].Semestre > 9);

        for (j = 0; j < Datos[i].Semestre; j++)
        {
            // Validar que el promedio sea entre 0 y 100
            do
            {
                printf("Ingresa el promedio del semestre %d:\n", j + 1);
                scanf("%d", &Datos[i].Promedio[j]);

                if (Datos[i].Promedio[j] < 0 || Datos[i].Promedio[j] > 100)
                    printf("Rango permitido 0-100. Intenta de nuevo.\n");
            }
            while(Datos[i].Promedio[j] < 0 || Datos[i].Promedio[j] > 100);
        }

        printf("Ingresa tu carrera:\n");
        fflush(stdin);
        fgets(Datos[i].Carrera, 30, stdin);

        i++;
        if (i < 20)
        {
            printf("¿Quieres agregar otro estudiante? (s/n): ");
            fflush(stdin);
            scanf("%c", &agregar);
        }
    }

    return 0;
}