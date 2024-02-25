#include <bits/stdc++.h>
using namespace std;

int main() {
    int N;
    cin >> N;
    vector<pair<int, int>> xy(N);
    int x,y;
    for (int i=0;i<N;i++) {
        cin >> x >> y;
        xy[i] = make_pair(x, y);
    }
    double sum = 0;
    int count = 0;
    for (int i=0;i<N-1;i++) {
        for (int j=i+1;j<N;j++) {
            sum += sqrt(pow(xy[i].first-xy[j].first, 2) + pow(xy[i].second-xy[j].second, 2));
            count++;
        }
    }
    cout << fixed << setprecision(10);
    cout << sum*(N-1)/count << endl;
}
