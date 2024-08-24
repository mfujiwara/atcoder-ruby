#include <bits/stdc++.h>
#include <bits/extc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;
using namespace __gnu_pbds;

int main() {
    int A,B,C;
    cin >> A >> B >> C;
    int mini=10000;
    int maxi=-10000;
    mini = min(mini, A*B);
    mini = min(mini, A*C);
    mini = min(mini, B*C);
    maxi = max(maxi, A*B);
    maxi = max(maxi, A*C);
    maxi = max(maxi, B*C);
    cout << mini << " " << maxi << endl;
}
