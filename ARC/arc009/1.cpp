#include <bits/stdc++.h>
using namespace std;

int main() {
    int N;
    cin >> N;
    int total=0;
    for (int i=0;i<N;i++) {
        int A,B;
        cin >> A >> B;
        total += A*B;
    }
    cout << (int)(total*1.05) << endl;
}
