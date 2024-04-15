#include <bits/stdc++.h>
using namespace std;

int main() {
    string S;
    cin >> S;
    vector<pair<string,string>> T;
    int start=0;
    int index=1;
    while (index<S.size()-1) {
        if ('A'<=S[index]&&S[index]<='Z' && 'A'<=S[index+1]&&S[index+1]<='Z') {
            string tmp1 = S.substr(start,index+1-start);
            string tmp2 = S.substr(start,index+1-start);
            tmp2[0] = tolower(tmp2[0]);
            tmp2[tmp2.size()-1] = tolower(tmp2[tmp2.size()-1]);
            T.push_back(make_pair(tmp2,tmp1));
            start=index+1;
            index+=2;
        } else {
            index++;
        }
    }
    string tmp1 = S.substr(start,S.size()-start);
    string tmp2 = S.substr(start,S.size()-start);
    tmp2[0] = tolower(tmp2[0]);
    tmp2[tmp2.size()-1] = tolower(tmp2[tmp2.size()-1]);
    T.push_back(make_pair(tmp2,tmp1));
    sort(T.begin(),T.end());
    for (int i=0;i<T.size();i++) {
        cout << T[i].second;
    }
    cout << endl;
}
