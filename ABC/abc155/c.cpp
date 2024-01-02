#include <bits/stdc++.h>
using namespace std;

int main() {
    int N;
    cin >> N;
    map<string, int> counts;
    int maxi = 0;
    for (int i=0;i<N;i++) {
        string s;
        cin >> s;
        counts[s]++;
        maxi = max(maxi, counts[s]);
    }
    vector<string> ans;
    for (auto p: counts) {
        if (p.second == maxi) {
            ans.push_back(p.first);
        }
    }
    sort(ans.begin(), ans.end());
    for (auto s: ans) {
        cout << s << endl;
    }
}
