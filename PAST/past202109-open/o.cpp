#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;

int main() {
    long long MOD = 998244353;
    int N,M;
    cin >> N >> M;
    vector<int> A(1<<N);
    for (int i=0;i<(1<<N);i++) {
        cin>>A[i];
        A[i]--;
    }
    vector<int> win(1<<N,0); // win count
    vector<int> lose(1<<N,-1); // lose to
    for (int i=0;i<M;i++) {
        int w,l;
        cin >> w >> l;
        w--;
        l--;
        if (lose[l] != -1) {
            cout << 0 << endl;
            return 0;
        }
        win[w] += 1;
        lose[l] = w;
    }
    vector<long long> red(1<<N, 1);
    vector<long long> blue(1<<N, 1);
    while (A.size()>1) {
        vector<int> nextA;
        vector<long long> nextRed;
        vector<long long> nextBlue;
        for (int i=0;i<(int)A.size();i+=2) {
            int a = A[i];
            int b = A[i+1];
            if (lose[b]==a) {
                win[a]--;
                M--;
            }
            if (lose[a]==b) {
                win[b]--;
                M--;
            }
            int judge;
            if (lose[a]==-1) {
                if (lose[b]==-1) {
                    if (win[a]>0) {
                        judge = a;
                    } else if (win[b]>0) {
                        judge = b;
                    } else {
                        judge = -1;
                    }
                } else if (lose[b]==a) {
                    judge = a;
                } else {
                    judge = b;
                }
            } else if (lose[a]==b) {
                if (lose[b]==-1) {
                    judge = b;
                } else if (lose[b]==a) {
                    cout << 0 << endl;
                    return 0;
                } else {
                    judge = b;
                }
            } else {
                if (lose[b]==-1) {
                    judge = a;
                } else if (lose[b]==a) {
                    judge = a;
                } else {
                    cout << 0 << endl;
                    return 0;
                }
            }
            if (judge==a) {
                nextA.push_back(a);
                if (a>b) {
                    nextRed.push_back(red[i]*blue[i+1]%MOD);
                    nextBlue.push_back(blue[i]*red[i+1]%MOD);
                } else {
                    nextRed.push_back(red[i]*red[i+1]%MOD);
                    nextBlue.push_back(blue[i]*blue[i+1]%MOD);
                }
            } else if (judge==b) {
                nextA.push_back(b);
                if (a>b) {
                    nextRed.push_back(red[i+1]*red[i]%MOD);
                    nextBlue.push_back(blue[i+1]*blue[i]%MOD);
                } else {
                    nextRed.push_back(red[i+1]*blue[i]%MOD);
                    nextBlue.push_back(blue[i+1]*red[i]%MOD);
                }
            } else {
                nextA.push_back(a);
                nextRed.push_back((red[i])*(red[i+1]+blue[i+1])%MOD);
                nextBlue.push_back((blue[i])*(red[i+1]+blue[i+1])%MOD);
            }
        }
        A = nextA;
        red = nextRed;
        blue = nextBlue;
    }
    if (M!=0) {
        cout << 0 << endl;
        return 0;
    }
    cout << (red[0]+blue[0])%MOD << endl;
}
