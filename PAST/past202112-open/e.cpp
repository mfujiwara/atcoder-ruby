#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;

int main() {
    string N;
    cin >> N;
    char pre;
    long long ret = 0;
    for (int i=0;i<N.size();i++) {
        if (i==0) {
            ret+=500;
        } else if (N[i] == pre) {
            ret+=301;
        } else if ((pre-'0'+9)%10/5==(N[i]-'0'+9)%10/5) {
            ret+=210;
        } else {
            ret+=100;
        }
        pre = N[i];
    }
    cout << ret << endl;
}
