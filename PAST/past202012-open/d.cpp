#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;

int main() {
    int N;
    cin >> N;
    vector<tuple<int,string,string>> A(N);
    for (int i=0;i<N;i++) {
        string s;
        cin >> s;
        string t = s;
        while (t[0] == '0') {
            t = t.substr(1);
        }
        A[i] = make_tuple(t.size(),t.size()==0 ? s+"1":t,s);
    }
    sort(A.begin(),A.end());
    for (int i=0;i<N;i++) {
        auto [_,__,s] = A[i];
        cout << s << endl;
    }
}
