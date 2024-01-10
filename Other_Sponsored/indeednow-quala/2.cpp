#include <bits/stdc++.h>
using namespace std;

int main() {
    int N;
    cin >> N;
    string S;
    for (int i=0;i<N;i++) {
        cin >> S;
        if (S.size()!=9) {
            cout << "NO" << endl;
            continue;
        }
        int ci=0,cn=0,cd=0,ce=0,co=0,cw=0;
        for (int j=0;j<S.size();j++) {
            if (S[j]=='i') ci++;
            else if (S[j]=='n') cn++;
            else if (S[j]=='d') cd++;
            else if (S[j]=='e') ce++;
            else if (S[j]=='o') co++;
            else if (S[j]=='w') cw++;
        }
        if (ci==1 && cn==2 && cd==2 && ce==2 && co==1 && cw==1) {
            cout << "YES" << endl;
        } else {
            cout << "NO" << endl;
        }
    }
}
