#include <bits/stdc++.h>
using namespace std;

int main() {
    int N;
    cin >> N;
    int h = N / 3600;
    int m = (N - h * 3600) / 60;
    int s = N - h * 3600 - m * 60;
    cout << setfill('0') << right << setw(2) << h << ":" << setw(2) << m << ":" << setw(2) << s << endl;
}
