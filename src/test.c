#include <stdio.h>

int main(int argc, char *argv[])
{
    char* w = "12";
    printf("%d %d %d\n", w, &w[0], &w[1]);
    printf("%s %d\n", w, *w);
    printf("%d %d\n", argv[1], argv[2]);
    printf("%s %s\n", argv[1], argv[2]);
    printf("%d %d\n", (int *)argv[1], (int *)argv[2]);
    printf("%d %d\n", *(int *)argv[1], *(int *)argv[2]);
    return 0;
}
