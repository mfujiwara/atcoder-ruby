#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;

int main() {
    int N;
    cin >> N;
    map<string,int> memo;
    for (int i=0;i<N;i++) {
        string P,V;
        cin >> P >> V;
        if (V == "AC" && memo[P] == 0) {
            memo[P] = i+1;
        }
    }
    cout << memo["A"] << endl;
    cout << memo["B"] << endl;
    cout << memo["C"] << endl;
    cout << memo["D"] << endl;
    cout << memo["E"] << endl;
    cout << memo["F"] << endl;
}
