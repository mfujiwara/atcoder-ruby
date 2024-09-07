#include <bits/stdc++.h>
using namespace std;

using F = double;
constexpr F EPS = 1e-10;

struct Point {
    F x, y;
    Point() : x(), y() {}
    Point(const F& x_, const F& y_) : x(x_), y(y_) {}
    Point operator-(const Point& other) const { return Point(x - other.x, y - other.y); }
    Point operator*(const F& other) const { return Point(x * other, y * other); }
    friend F cross(const Point& p, const Point& q) { return p.x * q.y - p.y * q.x; }
};

int main() {
    int n, m;
    cin >> n >> m;
    vector<Point> s(n);
    for (auto& [x, y] : s) {
        int a, b;
        cin >> a >> b;
        x = a, y = b;
    }
    vector<Point> t(m);
    for (auto& [x, y] : t) {
        int a, b;
        cin >> a >> b;
        x = a, y = b;
    }
    for (int i = 0; i < m; ++i) {
        const Point pivot = t[i];
        const Point vect = t[i + 1 == m ? 0 : i + 1] - t[i];
        const int len = s.size();
        vector<Point> next;
        for (int j = 0; j < len; ++j) {
            const Point p = s[j], q = s[j + 1 == len ? 0 : j + 1];
            const F p_c = cross(vect, p - pivot), q_c = cross(vect, q - pivot);
            if (p_c + EPS > 0) {
                next.push_back(p);
            }
            if (((p_c > EPS) and (q_c < -EPS)) or ((p_c < -EPS) and (q_c > EPS))) {
                next.push_back(p - (q - p) * (p_c / (q_c - p_c)));
            }
        }
        s = move(next);
    }
    const int len = s.size();
    F ans = 0;
    for (int i = 0; i < len; ++i) {
        ans = ans + cross(s[i], s[i + 1 == len ? 0 : i + 1]);
    }
    cout << fixed << setprecision(20);
    cout << ans / 2 << '\n';
}
