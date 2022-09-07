#include <iostream>
#include <vector>
#include <algorithm>

int main(void) {
    int N;
    std::cin >> N;

    std::vector<int> P;
    for (int i = 0; i < N; ++i) {
        int p;
        std::cin >> p;
        P.push_back(p);
    }
    std::sort(P.begin(), P.end());

    int min_sum = 0;
    for (int i = 1; i < N+1; ++i) {
        for (int j = 0; j < i; j++) {
            min_sum += P[j];
        }
    }
    std::cout << min_sum << std::endl;
}