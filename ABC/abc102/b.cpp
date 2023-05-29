#include <bits/stdc++.h>
using namespace std;

int main() {
    int N;
    cin >> N;
    int maxi=0;
    int mini=pow(10,9);
    int a;
    for (int i=0;i<N;i++) {
        cin>>a;
        if (a>maxi) {
            maxi=a;
        }
        if (a<mini) {
            mini=a;
        }
    }
    cout << maxi-mini << endl;    
}
