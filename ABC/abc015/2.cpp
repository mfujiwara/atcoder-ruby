#include <bits/stdc++.h>
using namespace std;

int main() {
    int N;
    cin >> N;
    int A;
    int sum = 0;
    int count = 0;
    for (int i=0;i<N;i++) {
        cin >> A;
        if (A != 0) {
            sum += A;
            count++;
        }
    }
    cout << (sum+count-1)/count << endl;
}
