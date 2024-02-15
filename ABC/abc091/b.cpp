#include <bits/stdc++.h>
using namespace std;

int main() {
    int N;
    cin >> N;
    map<string, int> m;
    for (int i=0;i<N;i++) {
        string s;
        cin >> s;
        m[s]++;
    }
    int M;
    cin >> M;
    for (int i=0;i<M;i++) {
        string s;
        cin >> s;
        m[s]--;
    }
    int ret = 0;
    for (auto p : m) {
        ret = max(ret, p.second);
    }
    cout << ret << endl;
}
