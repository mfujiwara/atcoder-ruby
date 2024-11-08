#include <bits/stdc++.h>
#include <bits/extc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;
using namespace __gnu_pbds;

int main() {
    int X,Y,R,N;
    cin >> X >> Y >> R >> N;
    for (int i=-N;i<=N;i++) {
        for (int j=-N;j<=N;j++) {
            if ((X-i)*(X-i)+(Y-j)*(Y-j)<=R*R) {
                cout << "#";
            } else {
                cout << ".";
            }
            if (j==N) {
                cout << endl;
            } else {
                cout << " ";
            }
        }
    }
}
