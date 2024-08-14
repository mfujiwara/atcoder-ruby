#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;

int main() {
    int N;
    cin >> N;
    vector<long long> A(N);
    for (int i=0;i<N;i++) {
        cin>>A[i];
    }
    vector<long long> B(N);
    for (int i=0;i<N;i++) {
        cin>>B[i];
    }
    vector<tuple<long long,long long,int>> score(N);
    for (int i=0;i<N;i++) {
        score[i] = make_tuple(-A[i]-B[i],-A[i],i);
    }
    sort(score.begin(),score.end());
    for (int i=0;i<N;i++) {
        cout << get<2>(score[i])+1;
        if (i<N-1) {
            cout << " ";
        } else {
            cout << endl;
        }
    }
}
