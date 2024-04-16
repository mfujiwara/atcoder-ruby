#include <bits/stdc++.h>
using namespace std;

int main() {
    int N;
    cin >> N;
    vector<vector<int>> A(N, vector<int>(N));
    for (int i=0;i<N;i++) {
        for (int j=i+1;j<N;j++) {
            cin >> A[i][j];
        }
    }
    int ret=-1001001001;
    for (int i=0;i<pow(3,N);i++) {
        int sum=0;
        vector<int> s;
        vector<int> t;
        vector<int> u;
        int T=i;
        for (int j=0;j<N;j++) {
            int tmp=T%3;
            if (tmp==0) {
                for (int k=0;k<s.size();k++) {
                    sum+=A[s[k]][j];
                }
                s.push_back(j);
            } else if (tmp==1) {
                for (int k=0;k<t.size();k++) {
                    sum+=A[t[k]][j];
                }
                t.push_back(j);
            } else {
                for (int k=0;k<u.size();k++) {
                    sum+=A[u[k]][j];
                }
                u.push_back(j);
            }
            T/=3;
        }
        ret=max(ret, sum);
    }
    cout << ret << endl;
}
