#include <bits/stdc++.h>
using namespace std;

int main() {
    int N;
    cin >> N;
    unsigned long long ret = 1;
    unsigned long long max = 1000000000000000000;
    unsigned long long tmp;
    for(int i=0;i<N;i++){
        cin >> tmp;
        if(tmp == 0){
            cout << 0 << endl;
            return 0;
        }
        if(ret > max/tmp){
            ret = 1000000000000000001;
        } else {
            ret *= tmp;
        }
    }
    if(ret > max){
        cout << -1 << endl;
    } else {
        cout << ret << endl;
    }
}
