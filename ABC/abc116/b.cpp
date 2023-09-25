#include <bits/stdc++.h>
using namespace std;

int main() {
    int s;
    cin >> s;
    map<int, int> memo;
    memo[s] = 1;
    int now=1;
    while (true) {
        if (s%2==0) {
            s = s/2;
        } else {
            s = 3*s+1;
        }
        now++;
        if (memo.count(s)) {
            cout << now << endl;
            return 0;
        } else {
            memo[s] = now;
        }
    }
}
