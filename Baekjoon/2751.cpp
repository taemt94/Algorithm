#include <iostream>

using namespace std;
void merge(int *a, int *b, int low, int mid, int high) {
    int i = low;
    int j = mid + 1;
    for(int k = low; k <= high; k++){
        if (i > mid){
            b[k] = a[j];
            j++;
        }
        else if(j > high){
            b[k] = a[i];
            i++;
        }
        else if(a[j] < a[i]){
            b[k] = a[j];
            j++;
        }
        else{
            b[k] = a[i];
            i++;
        }
    }
    for(int k = low; k <= high; k++)
        a[k] = b[k];
}

void merge_sort(int *a, int *b, int low, int high){
    if (low >= high)
        return;
    int mid = (low + high) / 2;
    merge_sort(a, b, low, mid);
    merge_sort(a, b, mid + 1, high);
    merge(a, b, low, mid, high);
}

int main(void){
    cin.tie(NULL);
    ios::sync_with_stdio(false);
    int N;
    cin >> N;
    
    int* a = new int[N];
    for (int i = 0; i < N; i++)
        cin >> a[i];
    int* b = new int[N];
    merge_sort(a, b, 0, N - 1);
    for (int i = 0; i < N; i++)
        cout << a[i] << '\n';
}