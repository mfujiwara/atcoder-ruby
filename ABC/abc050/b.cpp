#include <bits/stdc++.h>
using namespace std;

int main() {
    int N;
    cin >> N;
    vector<int> T(N);
    int total = 0;
    for (int i=0;i<N;i++) {
        cin>>T[i];
        total += T[i];
    }
    int M;
    cin >> M;
    int P,X;
    for (int i=0;i<M;i++) {
        cin>>P>>X;
        cout << total - T[P-1] + X << endl;
    }
}
