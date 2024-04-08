#include <bits/stdc++.h>
using namespace std;

int main() {
    int N;
    string c;
    cin >> N >> c;
    vector<int> cnt(4);
    for (int i=0;i<N;i++) {
        cnt[c[i]-'1']++;
    }
    cout << *max_element(cnt.begin(), cnt.end()) << " " << *min_element(cnt.begin(), cnt.end()) << endl;
}
