#include <bits/stdc++.h>
using namespace std;

int main() {
    int N,T;
    cin >> N >> T;
    int ret = 0;
    int pre = 0;
    for (int i=0;i<N;i++) {
        int A;
        cin >> A;
        if (i==0) {
            ret += T;
        } else {
            if (A-pre<T) {
                ret += A-pre;
            } else {
                ret += T;
            }
        }
        pre = A;
    }
    cout << ret << endl;
}