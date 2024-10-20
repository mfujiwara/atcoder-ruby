#include <bits/stdc++.h>
#include <bits/extc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;
using namespace __gnu_pbds;

int main() {
    int D;
    string A,B;
    cin >> D >> A >> B;
    string str_a = "";
    string float_a = "";
    string str_b = "";
    string float_b = "";
    for (int i=0;i<A.size();i++) {
        if (A[i] == '.') {
            float_a = A.substr(i+1);
            break;
        }
        str_a += A[i];
    }
    for (int i=0;i<B.size();i++) {
        if (B[i] == '.') {
            float_b = B.substr(i+1);
            break;
        }
        str_b += B[i];
    }
    int a = stoi(str_a);
    int b = stoi(str_b);
    string float_sum = "";
    int carry = 0;
    for (int i=D-1;i>=0;i--) {
        int sum = carry;
        sum += float_a[i] - '0';
        sum += float_b[i] - '0';
        carry = sum / 10;
        sum %= 10;
        float_sum += to_string(sum);
    }
    reverse(float_sum.begin(), float_sum.end());
    cout << a+b+carry << "." << float_sum << endl;
}
