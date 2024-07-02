#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;

int main() {
    int N,L,T,X;
    cin >> N >> L >> T >> X;
    int heat = 0;
    int ret = 0;
    for (int i=0;i<N;i++) {
        int a,b;
        cin >> a >> b;
        if (b>=L) {
            if (a>T) {
                cout << "forever" << endl;
                return 0;
            }
            if (heat+a>T) {
                if (a==T) {
                    ret += T-heat+X+a+X;
                    heat = 0;
                } else {
                    ret += T-heat+X+a;
                    heat = a;
                }
            } else if (heat+a<T) {
                ret += a;
                heat += a;
            } else {
                ret += a+X;
                heat = 0;
            }
        } else {
            heat = 0;
            ret += a;
        }
    }
    cout << ret << endl;
}
