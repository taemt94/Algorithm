#include <stdio.h>

int main(){
    int a, b, c, d, e;
    scanf("%1d%1d%1d%1d%1d", &a, &b, &c, &d, &e);
    int i = 10000;
    int j = 1;
    while (i >= 1){
        if (j == 1){
            printf("[%d]\n", a * i);
            i /= 10;
            j++;
        }
        else if (j == 2){
            printf("[%d]\n", b * i);
            i /= 10;
            j++;
        }
        else if (j == 3){
            printf("[%d]\n", c * i);
            i /= 10;
            j++;
        }
        else if (j == 4){
            printf("[%d]\n", d * i);
            i /= 10;
            j++;
        }
        else if (j == 5){
            printf("[%d]\n", e * i);
            i /= 10;
            j++;
        }
    }

    return 0;
}