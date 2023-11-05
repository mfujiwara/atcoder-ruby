#include <bits/stdc++.h>
using namespace std;

int main() {
    string s;
    cin >> s;
    int a = s.find('A');
    int z = s.rfind('Z');
    cout << z - a + 1 << endl;
}
