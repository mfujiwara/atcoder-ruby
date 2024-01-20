#include <bits/stdc++.h>
using namespace std;

int main() {
    string S;
    cin >> S;
    int ret=0;
    for (int i=0;i<S.size();i++) {
        int num = S[i]-'0';
        if (i%2==0) {
            ret+=num;
        } else {
            ret-=num;
        }
    }
    cout << ret << endl;
}
