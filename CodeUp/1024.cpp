#include <stdio.h>

int main(){
    char word[20];
    scanf("%s", word);
    for(int i=0; word[i]!='\0'; i++){
        printf("\'%c\'\n", word[i]);
    }
}