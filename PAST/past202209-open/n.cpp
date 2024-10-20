#include <bits/stdc++.h>
#include <bits/extc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;
using namespace __gnu_pbds;

int main() {
    int H,W,Q;
    cin >> H >> W >> Q;
    int T;
    vector<string> A(H);
    for (int i=0;i<H;i++) {
        cin >> A[i];
    }
    vector<deque<char>> que;
    if (H<W) {
        T = 1;
        que = vector<deque<char>>(H);
        for (int i=0;i<H;i++) {
            for (int j=0;j<W;j++) {
                que[i].push_back(A[i][j]);
            }
        }
    } else {
        T = 2;
        que = vector<deque<char>>(W);
        for (int i=0;i<H;i++) {
            for (int j=0;j<W;j++) {
                que[j].push_back(A[i][j]);
            }
        }
    }
    string S = "";
    for (int i=0;i<Q;i++) {
        int t,p;
        string c;
        cin >> t >> p >> c;
        p--;
        if (t==T) {
            S += que[p].back();
            que[p].push_front(c[0]);
            que[p].pop_back();
        } else {
            S += que[que.size()-1][p];
            for (int i=que.size()-1;i>0;i--) {
                que[i][p] = que[i-1][p];
            }
            que[0][p] = c[0];
        }
    }
    cout << S << endl;
}
