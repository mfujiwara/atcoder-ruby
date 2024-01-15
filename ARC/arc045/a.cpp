#include <bits/stdc++.h>
using namespace std;

string calc() {
    string s;
    cin >> s;
    if (s == "Left") {
        return "<";
    } else if (s == "Right") {
        return ">";
    } else if (s == "AtCoder") {
        return "A";
    } else {
        return "";
    }
}

int main() {
    cout << calc();
    while (true) {
        string s = calc();
        if (s == "") {
            break;
        } else {
            cout << " " << s;
        }
    }
    cout << endl;
}
