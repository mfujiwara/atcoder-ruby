#include <bits/stdc++.h>
using namespace std;

int main() {
    long X;
    cin >> X;
    long money = 100;
    int year = 0;
    while (money < X) {
        money = money + money / 100;
        year++;
    }
    cout << year << endl;
}
