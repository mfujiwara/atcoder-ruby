#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;

int main() {
    string S;
    cin >> S;
    vector<string> all;
    for (int i=0;i<27;i++) {
        string s = ".";
        if (i<26) {
            s[0] = 'a'+i;
        }
        all.push_back(s);
    }
    for (int i=0;i<27;i++) {
        for (int j=0;j<27;j++) {
            string s = "..";
            if (i<26) {
                s[0] = 'a'+i;
            }
            if (j<26) {
                s[1] = 'a'+j;
            }
            all.push_back(s);
        }
    }
    for (int i=0;i<27;i++) {
        for (int j=0;j<27;j++) {
            for (int k=0;k<27;k++) {
                string s = "...";
                if (i<26) {
                    s[0] = 'a'+i;
                }
                if (j<26) {
                    s[1] = 'a'+j;
                }
                if (k<26) {
                    s[2] = 'a'+k;
                }
                all.push_back(s);
            }
        }
    }
    int ret = 0;
    for (int i=0;i<all.size();i++) {
        string s = all[i];
        bool ok = false;
        for (int j=0;j<S.size();j++) {
            string t = S.substr(j, s.size());
            if (t.size() == s.size()) {
                for (int k=0;k<s.size();k++) {
                    if (s[k] != '.' && s[k] != t[k]) {
                        break;
                    }
                    if (k == s.size()-1) {
                        ok = true;
                    }
                }
            }
            if (ok) {
                ret += 1;
                break;
            }
        }
    }
    cout << ret << endl;
}
