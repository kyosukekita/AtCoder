//https://drken1215.hatenablog.com/entry/2019/06/15/135300
#include <bits/stdc++.h>
using namespace std;

int main() {
    int N, M; cin >> N >> M;
    vector<vector<int> > s(M);
    for (int i = 0; i < M; ++i) {
        int k; cin >> k;
        for (int j = 0; j < k; ++j) {
            int a; cin >> a; --a;
            s[i].push_back(a);
        }
    }
    vector<int> p(M);
    for (int i = 0; i < M; ++i) cin >> p[i];
    
    long long res = 0;
    for (int bit = 0; bit < (1<<N); ++bit) {
        bitset<10> bitt(bit);
        bool ok = true;
        for (int i = 0; i < M; ++i) {
            int con = 0;
            for (auto v : s[i]) {
                if (bitt.test(v)) ++con;
            }
            if (con % 2 != p[i]) ok = false;
        }
        if (ok) ++res;
    }
    cout << res << endl;
}
