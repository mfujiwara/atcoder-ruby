#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;

int main() {
    int Q;
    cin >> Q;
    queue<pair<string,int>> que;
    for (int i=0;i<Q;i++) {
        int t;
        cin >> t;
        if (t==1) {
            string c;
            int x;
            cin >> c >> x;
            que.push(make_pair(c,x));
        } else if (t==2) {
            int d;
            cin >> d;
            vector<int> counts(26,0);
            while (d>0 && !que.empty()) {
                if (d>=que.front().second) {
                    d-=que.front().second;
                    int t = que.front().first[0]-'a';
                    counts[t]+=que.front().second;
                    que.pop();
                } else {
                    que.front().second-=d;
                    int t = que.front().first[0]-'a';
                    counts[t]+=d;
                    d=0;
                }
            }
            long long ret = 0;
            for (int j=0;j<26;j++) {
                ret+=(long long)counts[j]*counts[j];
            }
            cout << ret << endl;
        }
    }
}
