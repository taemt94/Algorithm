#include <string>
#include <vector>
#include <cmath>

using namespace std;

long long solution(long long n) {
    long long answer = 0;
    
    double x_double = sqrt(n);
    long long x = x_double;
        
    if (x == x_double)
        answer = pow(x + 1, 2);
    else
        answer = -1;
    
    return answer;
}