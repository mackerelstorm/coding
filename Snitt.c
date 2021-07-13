// This is a GPA calculator for Norwegian grading system
#include <stdio.h>
#include <stdlib.h>
int main() {
int Antall;
int Karakter;
int KarakterTotal = 0;
int InputAntall = 0;
printf("Hvor mange karakterer? ");
scanf("%d", &Antall);
while (Antall > InputAntall) {
    printf("Skriv inn en karakter: ");
    scanf("%d", &Karakter);
    if (Karakter > 6) {
        printf("Ugyldig karakter");
    }
    else {
    KarakterTotal = KarakterTotal + Karakter;
    InputAntall++;   
    }
}
printf("Ditt snitt er: %.2f",(double)KarakterTotal / (double)Antall);
while (1>0) {

}
}
