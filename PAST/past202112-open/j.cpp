#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;

pair<int,int> calc(int N, vector<vector<int>> A, int x, int y) {
    if (A[0][0]==0&&A[0][1]==1&&A[1][0]==2) {
        return make_pair(x,y);
    } else if (A[0][0]==0&&A[1][0]==1&&A[0][1]==2) {
        return make_pair(y,x);
    } else if (A[0][1]==0&&A[1][1]==1&&A[0][0]==2) {
        return make_pair(y,N-1-x);
    } else if (A[0][1]==0&&A[0][0]==1&&A[1][1]==2) {
        return make_pair(x,N-1-y);
    } else if (A[1][0]==0&&A[0][0]==1&&A[1][1]==2) {
        return make_pair(N-1-y,x);
    } else if (A[1][0]==0&&A[1][1]==1&&A[0][0]==2) {
        return make_pair(N-1-x,y);
    } else if (A[1][1]==0&&A[1][0]==1&&A[0][1]==2) {
        return make_pair(N-1-x,N-1-y);
    } else {
        return make_pair(N-1-y,N-1-x);
    }
}

int main() {
    int N,Q;
    cin >> N >> Q;
    int t;
    vector<vector<int>> G(N,vector<int>(N));
    vector<vector<int>> A(2,vector<int>(2));
    A[0][0] = 0;
    A[0][1] = 1;
    A[1][0] = 2;
    A[1][1] = 3;
    int type2 = 0;
    int type3 = 0;
    for (int i=0;i<Q;i++) {
        cin >> t;
        if (t==1) {
            int x,y;
            cin >> x >> y;
            x--; y--;
            auto [a,b] = calc(N,A,x,y);
            G[a][b]^=1;
        } else if (t==2) {
            string c;
            cin >> c;
            if ((c=="A"&&type3==0)||(c=="B"&&type3==1)) {
                int t = A[0][0];
                A[0][0] = A[0][1];
                A[0][1] = A[1][1];
                A[1][1] = A[1][0];
                A[1][0] = t;
            } else {
                int t = A[0][0];
                A[0][0] = A[1][0];
                A[1][0] = A[1][1];
                A[1][1] = A[0][1];
                A[0][1] = t;
            }
            type2^=1;
        } else {
            string c;
            cin >> c;
            if ((c=="A"&&type2==0)||(c=="B"&&type2==1)) {
                swap(A[0][0],A[1][0]);
                swap(A[0][1],A[1][1]);
            } else {
                swap(A[0][0],A[0][1]);
                swap(A[1][0],A[1][1]);
            }
            type3^=1;
        }
    }
    for (int i=0;i<N;i++) {
        for (int j=0;j<N;j++) {
            auto [a,b] = calc(N,A,i,j);
            cout << G[a][b];
        }
        cout << endl;
    }
}
