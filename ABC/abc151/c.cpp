#include <bits/stdc++.h>
using namespace std;

int main() {
    int N,M;
    cin >> N >> M;
    vector<int> memo(N, 0);
    int c_ac = 0;
    int c_wa = 0;
    int p;
    string S;
    for (int i=0;i<M;i++) {
        cin >> p >> S;
        p--;
        if (memo[p]==-1) {
            continue;
        }
        if (S == "AC") {
            c_ac++;
            c_wa += memo[p];
            memo[p] = -1;
        } else {
            memo[p]++;
        }
    }
    cout << c_ac << " " << c_wa << endl;
}
