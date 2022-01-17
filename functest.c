#include <stdio.h>


float average(float num1, float num2) {
float sum = (num1 + num2) / 2;
return sum;
}


int main() {
float num1;
float num2;

printf("Hva er den første verdien du vil ha?: ");
scanf("%f", &num1);
printf("Hva er den andre verdien du vil ha?: ");
scanf("%f", &num2);
printf("%.2f", average(num1, num2));
scanf("%f");
}