#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;

int main() {
    int N;
    string S;
    cin >> N >> S;
    deque<int> q;
    for (int i=0;i<N;i++) {
        if (S[i] == 'L') {
            q.push_front(i+1);
        } else if (S[i] == 'R') {
            q.push_back(i+1);
        } else if (S[i] == 'A') {
            if (q.size() == 0) {
                cout << "ERROR" << endl;
            } else {
                cout << q.front() << endl;
                q.pop_front();
            }
        } else if (S[i] == 'B') {
            if (q.size() <= 1) {
                cout << "ERROR" << endl;
            } else {
                int t0 = q.front();
                q.pop_front();
                cout << q.front() << endl;
                q.pop_front();
                q.push_front(t0);
            }
        } else if (S[i] == 'C') {
            if (q.size() <= 2) {
                cout << "ERROR" << endl;
            } else {
                int t0 = q.front();
                q.pop_front();
                int t1 = q.front();
                q.pop_front();
                cout << q.front() << endl;
                q.pop_front();
                q.push_front(t1);
                q.push_front(t0);
            }
        } else if (S[i] == 'D') {
            if (q.size() == 0) {
                cout << "ERROR" << endl;
            } else {
                cout << q.back() << endl;
                q.pop_back();
            }
        } else if (S[i] == 'E') {
            if (q.size() <= 1) {
                cout << "ERROR" << endl;
            } else {
                int t0 = q.back();
                q.pop_back();
                cout << q.back() << endl;
                q.pop_back();
                q.push_back(t0);
            }
        } else if (S[i] == 'F') {
            if (q.size() <= 2) {
                cout << "ERROR" << endl;
            } else {
                int t0 = q.back();
                q.pop_back();
                int t1 = q.back();
                q.pop_back();
                cout << q.back() << endl;
                q.pop_back();
                q.push_back(t1);
                q.push_back(t0);
            }
        }
    }
}
