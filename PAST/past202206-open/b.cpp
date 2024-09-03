#include <bits/stdc++.h>
#include <bits/extc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;
using namespace __gnu_pbds;

int main() {
    string S;
    cin >> S;
    map<string,int> count;
    pair<int,string> mini = make_pair(0,"");
    for (int i=0;i<S.size()-1;i++) {
        string s = S.substr(i,2);
        count[s]++;
        mini = min(mini,make_pair(-count[s],s));
    }
    cout << mini.second << endl;
}
