#include <bits/stdc++.h>
#include <bits/extc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;
using namespace __gnu_pbds;

int main() {
    int N;
    cin >> N;
    string X;
    cin >> X;
    map<int,int> field;
    for (int i=0;i<5;i++) {
        field[X[i]-'A']+=1;
    }
    tuple<int,int,int> ret = {0,0,0};
    for (int i=0;i<N;i++) {
        string S;
        cin >> S;
        map<int,int> hand;
        for (int j=0;j<4;j++) {
            hand[S[j]-'A']+=1;
        }
        for (int j=0;j<26;j++) {
            ret = min(ret,{-min(hand[j],2)-min(field[j],3),j,i+1});
        }
    }
    cout << get<2>(ret) << endl;
}
