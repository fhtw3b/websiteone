#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

void main (void)
{
    char lettre[200];
    int i = 0 ;
    printf("Indiquer une chaine de caracteres: \n");
    scanf("%s", &lettre);

    while (lettre[i] != '\0')
    {
        if (lettre[i] == ' ')
        {
            i += 1 ;             
        }
        else
        {
            i += 1 ;
        }
    }

    printf("Voici le nombre de caracteres: %d \n", i);
    
}