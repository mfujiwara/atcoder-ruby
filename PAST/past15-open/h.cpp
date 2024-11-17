#include <bits/stdc++.h>
#include <bits/extc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;
using namespace __gnu_pbds;

int main() {
    unsigned long long N;
    cin >> N;
    unsigned long long ok=0;
    unsigned long long ng=3000000000;
    while (ng-ok>1){
        unsigned long long mid=(ok+ng)/2;
        unsigned long long v;
        if (mid%2==0) {
            v=mid/2*(mid+1);
        } else {
            v=(mid+1)/2*mid;
        }
        if (v<=N){
            ok=mid;
        }else{
            ng=mid;
        }
    }
    cout << ok << endl;
}
