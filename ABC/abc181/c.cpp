#include <bits/stdc++.h>
using namespace std;

int main() {
    int N;
    cin >> N;
    vector<pair<int,int>> points(N);
    int x,y;
    for (int i=0;i<N;i++) {
        cin >> x >> y;
        points[i] = make_pair(x,y);
    }
    for (int i=0;i<N-2;i++) {
        int xi=points[i].first;
        int yi=points[i].second;
        for (int j=i+1;j<N-1;j++) {
            int xj=points[j].first;
            int yj=points[j].second;
            for (int k=j+1;k<N;k++) {
                int xk=points[k].first;
                int yk=points[k].second;
                if (xi==xj) {
                    if (xi==xk) {
                        cout << "Yes" << endl;
                        return 0;
                    }
                } else if (yi==yj) {
                    if (yi==yk) {
                        cout << "Yes" << endl;
                        return 0;
                    }
                } else if ((xj-xi)*(yk-yi)==(xk-xi)*(yj-yi)) {
                    cout << "Yes" << endl;
                    return 0;
                }
            }
        }
    }
    cout << "No" << endl;
}
