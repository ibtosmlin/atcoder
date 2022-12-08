#include <bits/stdc++.h>
using namespace std;
using ll = long long;

ll INF = 1LL << 60;

int main() {
    int n;
    cin >> n;
    ll A[n];

    for (int i = 0; i < n - 1; ++i) {
        cin >> A[i];
    }
    A[n-1] = 0

    ll DP[n / 2 + 1][2];
    for (int i = 0; i < n / 2 + 1; ++i) {
        for (int j = 0; j < 2; ++j) {
            DP[i][j] = INF;
        }
    }
    DP[1][0] = 0;
    for (int i = 0; i < n - 1; ++i) {
        for (int j = n / 2; j > 0; --j) {
            DP[j][1] = min(DP[j][1], DP[j][0] + X[i]);
            DP[j][0] = min(DP[j - 1][0], DP[j - 1][1] + X[i]);
        }
    }

    ll ans;
    ans = min(DP[n / 2][0], DP[n / 2][1]);
    cout << ans << endl;

    return 0;

}

# dpA[i] 右端がAでA-B = i である時の最低コスト
of = n+1
dpA = [INF] * (2*of)
dpB = [INF] * (2*of)
dpA[of] = 0

for i, ai in enumerate(A):
    ndpA = [INF] * (2*of)
    ndpB = [INF] * (2*of)
    for j in range(of-i, of+i+1, 2):
        ndpA[j+1] = min(ndpA[j+1], dpA[j], dpB[j]+ai)
        ndpB[j-1] = min(ndpB[j-1], dpA[j]+ai, dpB[j])
    dpA, dpB = ndpA, ndpB
print(dpA[of])
