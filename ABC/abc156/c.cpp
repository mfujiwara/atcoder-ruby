#include <bits/stdc++.h>
using namespace std;

int main() {
    int N;
    cin >> N;
    int a=0,b=0,c=0;
    for (int i=0;i<N;i++) {
        int X;
        cin >> X;
        a+=1;
        b+=2*X;
        c+=X*X;
    }
    int ret=1000000000;
    for (int i=1;i<=100;i++) {
        int tmp=a*i*i-b*i+c;
        ret=min(ret,tmp);
    }
    cout << ret << endl;
}
