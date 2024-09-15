#include <bits/stdc++.h>
#include <bits/extc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;
using namespace __gnu_pbds;

int main() {
    vector<int> P1(6);
    vector<int> P2(6);
    vector<int> P3(6);
    for (int i=0;i<6;i++) {
        cin >> P1[i];
    }
    for (int i=0;i<6;i++) {
        cin >> P2[i];
    }
    for (int i=0;i<6;i++) {
        cin >> P3[i];
    }
    vector<int> rets(18,0);
    for (int i=0;i<6;i++) {
        for (int j=0;j<6;j++) {
            for (int k=0;k<6;k++) {
                rets[i+j+k+2] += P1[i]*P2[j]*P3[k];
            }
        }
    }
    cout << fixed << setprecision(10);
    for (int i=0;i<18;i++) {
        cout << (double)rets[i]/(1000000) << endl;
    }
}
