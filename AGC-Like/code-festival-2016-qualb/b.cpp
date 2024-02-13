#include <bits/stdc++.h>
using namespace std;

int main() {
    int N,A,B;
    string S;
    cin >> N >> A >> B >> S;
    int count = 0;
    int count_b = 0;
    for (int i=0;i<N;i++) {
        if (S[i] == 'a') {
            if (count < A+B) {
                cout << "Yes" << endl;
                count++;
            } else {
                cout << "No" << endl;
            }
        } else if (S[i] == 'b') {
            count_b++;
            if (count < A+B && count_b <= B) {
                cout << "Yes" << endl;
                count++;
            } else {
                cout << "No" << endl;
            }
        } else {
            cout << "No" << endl;
        }
    }
}
