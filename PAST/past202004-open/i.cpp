#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;

int main() {
    int N;
    cin >> N;
    vector<pair<int,int>> A((int)pow(2,N));
    for (int i=0;i<(int)pow(2,N);i++) {
        cin >> A[i].first;
        A[i].second = i;
    }
    vector<int> ret((int)pow(2,N));
    for (int i=0;i<N;i++) {
        vector<pair<int,int>> B;
        for (int j=0;j<(int)pow(2,N-i);j+=2) {
            if (A[j].first > A[j+1].first) {
                B.push_back(A[j]);
                ret[A[j+1].second] = i+1;
            } else {
                B.push_back(A[j+1]);
                ret[A[j].second] = i+1;
            }
        }
        A = B;
    }
    ret[A[0].second] = N;
    for (int i=0;i<(int)pow(2,N);i++) {
        cout << ret[i] << endl;
    }
}
