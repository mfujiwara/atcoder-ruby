#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;

int main() {
    int N;
    string S;
    cin >> N >> S;
    for (int i=0;i<N-2;i++) {
        if (S[i+1]=='x') {
            if (S[i]=='a' && S[i+2]=='a') {
                S[i]='.';
                S[i+1]='.';
                S[i+2]='.';
            } else if (S[i]=='i' && S[i+2]=='i') {
                S[i]='.';
                S[i+1]='.';
                S[i+2]='.';
            } else if (S[i]=='u' && S[i+2]=='u') {
                S[i]='.';
                S[i+1]='.';
                S[i+2]='.';
            } else if (S[i]=='e' && S[i+2]=='e') {
                S[i]='.';
                S[i+1]='.';
                S[i+2]='.';
            } else if (S[i]=='o' && S[i+2]=='o') {
                S[i]='.';
                S[i+1]='.';
                S[i+2]='.';
            }
        }
    }
    cout << S << endl;
}
