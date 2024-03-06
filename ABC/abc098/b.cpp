#include <bits/stdc++.h>
using namespace std;

int main() {
    int N;
    string S;
    cin >> N >> S;
    vector<int> mins(26,-1);
    vector<int> maxs(26,-1);
    for (int i=0;i<N;i++) {
        int c = S[i] - 'a';
        if (mins[c] == -1) {
            mins[c] = i;
        }
        maxs[c] = i;
    }
    int ret = 0;
    for (int i=1;i<N;i++) {
        int tmp=0;
        for (int j=0;j<26;j++) {
            if (mins[j] != -1 && mins[j]<i && i<=maxs[j]) {
                tmp++;
            }
        }
        ret = max(ret,tmp);
    }
    cout << ret << endl;
}
