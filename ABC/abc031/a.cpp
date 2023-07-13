#include <bits/stdc++.h>
using namespace std;

int main() {
    int A,D;
    cin >> A >> D;
    int maxi=max(A,D);
    int mini=min(A,D);
    cout << (mini+1)*maxi << endl;
}
