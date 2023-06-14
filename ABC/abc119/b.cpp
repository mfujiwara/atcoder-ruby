#include <bits/stdc++.h>
using namespace std;

int main() {
    int N;
    cin >> N;
    double ret=0.0;
    for (int i=0;i<N;i++) {
        double x;
        string u;
        cin >> x >> u;
        if (u == "JPY") {
            ret+=x;
        } else {
            ret+=x*380000.0;
        }
    }
    cout << ret << endl;
}
