#include <bits/stdc++.h>
using namespace std;

int main() {
    int N;
    cin >> N;
    vector<pair<pair<string, int>, int>> v(N);
    for (int i=0;i<N;i++) {
        string s;
        int p;
        cin >> s >> p;
        v[i] = make_pair(make_pair(s, -p), i+1);
    }
    sort(v.begin(), v.end());
    for (int i=0;i<N;i++) {
        cout << v[i].second << endl;
    }
}
