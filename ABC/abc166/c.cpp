#include <bits/stdc++.h>
using namespace std;

int main() {
    int N,M;
    cin >> N >> M;
    vector<int> H(N);
    for (int i=0;i<N;i++) {
        cin >> H[i];
    }
    vector<bool> memo(N,true);
    int A,B;
    for (int i=0;i<M;i++) {
        cin >> A >> B;
        A--;
        B--;
        if (H[A] > H[B]) {
            memo[B] = false;
        } else if (H[A] < H[B]) {
            memo[A] = false;
        } else {
            memo[A] = false;
            memo[B] = false;
        }
    }
    int ret = 0;
    for (int i=0;i<N;i++) {
        if (memo[i]) {
            ret++;
        }
    }
    cout << ret << endl;
}
