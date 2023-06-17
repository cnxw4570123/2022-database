#include <algorithm>
#include <cstring>
#include <iostream>

using namespace std;

#define DIV 1000000
#define MAX 100000
#define endl '\n'
#define f first
#define s second
typedef long long ll;

int N, M, ans;
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    cin >> N >> M;

    if (N == 1) cout << 1;
    else if(N == 2)
        cout << min(4, (M + 1) / 2);
    else if(M < 7)
        cout << min(4,M);
    else
        cout << M - 2;
    return 0;
}
