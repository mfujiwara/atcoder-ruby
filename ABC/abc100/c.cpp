#include <bits/stdc++.h>
using namespace std;

int main() {
    int N;
    cin >> N;
    int ret = 0;
    for (int i=0;i<N;i++) {
        int A;
        cin >> A;
        while (A%2==0) {
            A/=2;
            ret++;
        }
    }
    cout << ret << endl;
}
