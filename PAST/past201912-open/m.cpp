#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;

int main() {
    int N,M;
    cin >> N >> M;
    vector<pair<int,int>> AB(N);
    for (int i=0;i<N;i++) {
        cin >> AB[i].first >> AB[i].second;
    }
    vector<pair<int,int>> CD(M);
    for (int i=0;i<M;i++) {
        cin >> CD[i].first >> CD[i].second;
    }
    double ok=0;
    double ng=1000000000;
    while (abs(ok-ng)>0.0000001) {
        double mid=(ok+ng)/2;
        vector<double> E(N);
        for (int i=0;i<N;i++) {
            E[i]=AB[i].second-mid*AB[i].first;
        }
        sort(E.begin(),E.end());
        vector<double> F(M);
        for (int i=0;i<M;i++) {
            F[i]=CD[i].second-mid*CD[i].first;
        }
        sort(F.begin(),F.end());
        double total0=E[N-1]+E[N-2]+E[N-3]+E[N-4]+E[N-5];
        double total1=E[N-1]+E[N-2]+E[N-3]+E[N-4]+F[M-1];
        if (max(total0,total1)>=0) {
            ok=mid;
        } else {
            ng=mid;
        }
    }
    cout << fixed << setprecision(10);
    cout << ok << endl;
}
