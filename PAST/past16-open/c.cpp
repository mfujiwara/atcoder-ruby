#include <bits/stdc++.h>
#include <bits/extc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;
using namespace __gnu_pbds;

int main() {
    int N;
    cin >> N;
    vector<int> cnt(8);
    for (int i=0;i<N;i++) {
        int a;
        cin >> a;
        cnt[a-1]+=1;
    }
    cout << *min_element(begin(cnt), end(cnt)) << endl;
}
