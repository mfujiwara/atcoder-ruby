#include <bits/stdc++.h>
using namespace std;

int main() {
    int N,X;
    cin >> N >> X;
    int mini=1000000000;
    for (int i=0;i<N;i++) {
        int m;
        cin>>m;
        mini=min(mini,m);
        X-=m;
    }
    cout << N+X/mini << endl;
}
