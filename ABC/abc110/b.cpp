#include <bits/stdc++.h>
using namespace std;

int main() {
    int N,M,X,Y;
    cin >> N >> M >> X >> Y;
    for (int i=0;i<N;i++) {
        int a;
        cin >> a;
        X = max(X,a);
    }
    for (int i=0;i<M;i++) {
        int b;
        cin >> b;
        Y = min(Y,b);
    }
    if (X<Y) {
        cout << "No War" << endl;
    } else {
        cout << "War" << endl;
    }
}
