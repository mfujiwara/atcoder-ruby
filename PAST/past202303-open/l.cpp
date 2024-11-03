#include <bits/stdc++.h>
#include <bits/extc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;

int main() {
    int N,M;
    cin >> N >> M;
    vector<set<int>> win_to_lose(N);
    vector<set<int>> lose_to_win(N);
    for (int i=0;i<M;i++) {
        int A,B;
        cin >> A >> B;
        A--; B--;
        win_to_lose[A].insert(B);
        lose_to_win[B].insert(A);
    }
    priority_queue<int, vector<int>, greater<int>> que;
    for (int i=0;i<N;i++) {
        if (lose_to_win[i].empty()) {
            que.push(i);
        }
    }
    int c = 0;
    while (!que.empty()) {
        int v = que.top();
        que.pop();
        c++;
        for (int to:win_to_lose[v]) {
            lose_to_win[to].erase(v);
            if (lose_to_win[to].empty()) {
                que.push(to);
            }
        }
        cout << v+1;
        if (c < N) {
            cout << " ";
        } else {
            cout << endl;
        }
    }
}
