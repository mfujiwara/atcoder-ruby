#include <bits/stdc++.h>
using namespace std;

int main() {
    string S;
    cin >> S;
    int N=S.size();
    string ret  = S.substr(0,5);
    for (int i=5;i<N;i++) {
        ret += S[i];
        int n=ret.size();
        if (ret.substr(n-6,n)=="HAGIYA") {
            ret = ret.substr(0,n-2);
            ret += "XILE";
        }
    }
    cout << ret << endl;
}
