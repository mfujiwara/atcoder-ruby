#include <bits/stdc++.h>
using namespace std;

int main() {
    int A,B,M;
    cin >> A >> B >> M;
    vector<int> a(A);
    int min_a=1000000000;
    for (int i=0;i<A;i++) {
        cin >> a[i];
        min_a = min(min_a, a[i]);
    }
    vector<int> b(B);
    int min_b=1000000000;
    for (int i=0;i<B;i++) {
        cin >> b[i];
        min_b = min(min_b, b[i]);
    }
    int ret = min_a + min_b;
    for (int i=0;i<M;i++) {
        int x,y,c;
        cin >> x >> y >> c;
        ret = min(ret, a[x-1] + b[y-1] - c);
    }
    cout << ret << endl;
}
