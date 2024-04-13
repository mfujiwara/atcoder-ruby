#include <bits/stdc++.h>
using namespace std;

int main() {
    int N;
    cin >> N;
    vector<bool> A(N+1);
    int t=0;
    int tmp;
    for (int i=0;i<N;i++) {
        cin>>tmp;
        if (A[tmp] == true) {
            t = tmp;
        } else {
            A[tmp] = true;
        }
    }
    if (t == 0) {
        cout << "Correct" << endl;
    } else {
        for (int i=1;i<=N;i++) {
            if (A[i] == false) {
                cout << t << " " << i << endl;
                break;
            }
        }
    }
}
