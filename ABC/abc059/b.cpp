#include <bits/stdc++.h>
using namespace std;

int main() {
    string A,B;
    cin >> A >> B;
    if (A==B) {
        cout << "EQUAL" << endl;
        return 0;
    }
    if (A.size()>B.size()) {
        cout << "GREATER" << endl;
        return 0;
    } else if (A.size()<B.size()) {
        cout << "LESS" << endl;
        return 0;
    }
    int n=A.size();
    for (int i=0;i<n;i++) {
        if (A[i]>B[i]) {
            cout << "GREATER" << endl;
            return 0;
        } else if (A[i]<B[i]) {
            cout << "LESS" << endl;
            return 0;
        }
    }
}
