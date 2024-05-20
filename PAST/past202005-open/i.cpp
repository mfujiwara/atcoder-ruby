#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;

int main() {
    int N,Q;
    cin >> N >> Q;
    vector<long long> row(N);
    vector<long long> col(N);
    for (int i=0;i<N;i++) {
        row[i] = i;
        col[i] = i;
    }
    bool isRow = true;
    for (int i=0;i<Q;i++) {
        int T;
        cin >> T;
        if (T == 1) {
            int A,B;
            cin >> A >> B;
            A--; B--;
            if (isRow) {
                swap(row[A], row[B]);
            } else {
                swap(col[A], col[B]);
            }
        } else if (T == 2) {
            int A,B;
            cin >> A >> B;
            A--; B--;
            if (isRow) {
                swap(col[A], col[B]);
            } else {
                swap(row[A], row[B]);
            }
        } else if (T == 3) {
            isRow = !isRow;
        } else {
            int A,B;
            cin >> A >> B;
            A--; B--;
            if (isRow) {
                cout << row[A]*N+col[B] << endl;
            } else {
                cout << row[B]*N+col[A] << endl;
            }
        }
    }
}
