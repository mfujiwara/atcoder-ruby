#include <bits/stdc++.h>
#include <bits/extc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;
using namespace __gnu_pbds;

int main() {
    int A,B,C,D,R;
    cin >> A >> B >> C >> D >> R;
    int E=B/D*D;
    if (E<B) E+=D;

    if (E<=C) {
        cout << "Yes" << endl;
        return 0;
    }
    int CC = min(E, C+R);
    if (A<=C && CC<=A+R) {
        cout << "Yes" << endl;
    } else {
        cout << "No" << endl;
    }
}
