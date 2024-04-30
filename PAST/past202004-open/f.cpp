#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;

int main() {
    int N;
    cin >> N;
    vector<vector<int>> array(N, vector<int>(0));
    for (int i=0;i<N;i++) {
        int A,B;
        cin >> A >> B;
        array[A-1].push_back(B);
    }
    priority_queue<int> pq;
    int ret = 0;
    for (int i=0;i<N;i++) {
        for (int j=0;j<array[i].size();j++) {
            pq.push(array[i][j]);
        }
        ret += pq.top();
        pq.pop();
        cout << ret << endl;
    }
}
