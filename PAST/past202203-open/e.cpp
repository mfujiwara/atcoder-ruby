#include <bits/stdc++.h>
#include <bits/extc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;
using namespace __gnu_pbds;

int main() {
    vector<string> memo;
    vector<string> year02{"2002","2020","2022","2200","2202","2220","2222"};
    vector<string> date02{"02/02","02/22","02/20"};
    for (int i=0;i<year02.size();i++) {
        for (int j=0;j<date02.size();j++) {
            memo.push_back(year02[i]+"/"+date02[j]);
        }
    }
    vector<string> year12{"2111","2112","2121","2122","2211","2212","2221","2222"};
    vector<string> date12{"11/11","11/12","11/21","11/22","12/11","12/12","12/21","12/22"};
    for (int i=0;i<year12.size();i++) {
        for (int j=0;j<date12.size();j++) {
            memo.push_back(year12[i]+"/"+date12[j]);
        }
    }
    memo.push_back("3000/03/03");
    sort(memo.begin(),memo.end());
    string S;
    cin >> S;
    for (int i=0;i<memo.size();i++) {
        if (S<=memo[i]) {
            cout << memo[i] << endl;
            return 0;
        }
    }
}
