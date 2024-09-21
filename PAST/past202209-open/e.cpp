#include <bits/stdc++.h>
#include <bits/extc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;
using namespace __gnu_pbds;

int main() {
    int R,N,M,L;
    cin >> R >> N >> M >> L;
    int r=0;
    int n=N;
    int m=0;
    for (int i=0;i<L;i++) {
        int s;
        cin >> s;
        n-=s;
        if (n<0) {
            cout << "No" << endl;
            return 0;
        }
        m+=1;
        if (n==0 || m==M) {
            r+=1;
            n=N;
            m=0;
        }
    }
    if (r==R && m==0) {
        cout << "Yes" << endl;
    } else {
        cout << "No" << endl;
    }
}
