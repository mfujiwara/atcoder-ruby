#include <bits/stdc++.h>
using namespace std;

int main() {
    int N;
    cin >> N;
    int mini=1000;
    int maxi=0;
    for (int i=0;i<N;i++) {
        int a;
        cin>>a;
        mini=min(mini,a);
        maxi=max(maxi,a);
    }
    cout << maxi-mini << endl;
}
