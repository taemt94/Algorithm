#include <iostream>
using namespace std;

int main() {
    int N, K;
    std::cin >> N >> K;
    int *A = new int [N];
    for (int i=0; i < N; ++i)
        std::cin >> A[i];

    int total_coin_num(0);
    while (true) {
        int max_value(1);
        int idx;
        if (A[N-1] <= K)
            max_value = A[N-1];
        else {
            for (int i=N-1; i >= 0; --i) {
                if (A[i] <= K) {
                    max_value = A[i];
                    break;
                }
            }
        }
        int coin_num = (int)(K / max_value);
        total_coin_num += coin_num; 
        K -= coin_num * max_value;
        
        if (K <= 0)
            break;
    }
    std::cout << total_coin_num << std::endl;
    return 0;
}