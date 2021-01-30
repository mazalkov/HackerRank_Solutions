// https://www.hackerrank.com/challenges/c-tutorial-basic-data-types/


#include <iostream>
#include <cstdio>
using namespace std;


int main() {
    // Complete the code.
    int integer;
    long long_integer;
    char character;
    float decimal;
    double longer_decimal;
    
    scanf("%d %ld %c %f %lf", &integer, &long_integer, &character, &decimal, &longer_decimal);
    
    printf("%d \n%ld \n%c \n%f \n%lf", integer, long_integer, character, decimal, longer_decimal);
    
    return 0;
}
