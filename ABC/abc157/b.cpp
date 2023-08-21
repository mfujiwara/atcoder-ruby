#include <bits/stdc++.h>
using namespace std;

int main() {
    vector<int> A(9);
    for (int i=0;i<9;i++) {
        cin >> A[i];
    }
    int N;
    cin >> N;
    vector<int> card(9, false);
    for (int i=0;i<N;i++) {
        int b;
        cin >> b;
        for (int j=0;j<9;j++) {
            if (A[j] == b) {
                card[j] = true;
            }
        }
    }
    for (int i=0;i<3;i++) {
        if (card[i*3]&&card[i*3+1]&&card[i*3+2]) {
            cout << "Yes" << endl;
            return 0;
        }
        if (card[i]&&card[i+3]&&card[i+6]) {
            cout << "Yes" << endl;
            return 0;
        }
    }
    if (card[0]&&card[4]&&card[8]) {
        cout << "Yes" << endl;
        return 0;
    }
    if (card[2]&&card[4]&&card[6]) {
        cout << "Yes" << endl;
        return 0;
    }
    cout << "No" << endl;
}
