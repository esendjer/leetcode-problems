#include <limits.h>
#include <stdio.h>
#include <assert.h>

int myAtoi(char * s){
    int ne = 0, res = 0, i = 0;

    while (s[i] == ' ') {
        i++;
    }

    if (s[i] == '+') {
        ne = 1;
        i++;
    }
    else if (s[i] == '-') {
        ne = -1;
        i++;
    }
    
    if (s[i] >= '0' && s[i] <= '9' && ne == 0) {
        ne = 1;
    }

    if (s[i] < '0' || s[i] > '9') {
        return res;
    }

    while (s[i] >= '0' && s[i] <= '9') {
        if ((res > INT_MAX / 10) || ((res == INT_MAX / 10) && s[i] > '7') || (res < 0)) {
            if (ne > 0) {
                return INT_MAX;
            }
            else {
                return INT_MIN;
            }
        }
        res = res * 10 + (s[i] - '0');
        i++;
    }
    return res * ne;
}

int main() {
    int results[] = {
        2147483647,
        42,
        -42,
        4193,
        32,
        0,
        2147483647,
        2147483647,
        2147483646,
        -2147483648,
        -2147483648,
        -2147483647
        };
    char * cases[] = {
        "91283472332",
        "42",
        "   -42",
        "4193 with words",
        "0032",
        "+-12",
        "2147483648",
        "2147483647",
        "2147483646",
        "-2147483649",
        "-2147483648",
        "-2147483647"
        };
    int i;
    for ( i = 0; i < sizeof(results) / sizeof(results[0]); i++ ) {
        int result = myAtoi(cases[i]);
        assert(result == results[i]);
        printf("Tested case: %d, result: %d\n", i + 1, result);
    }
    return 0;
}