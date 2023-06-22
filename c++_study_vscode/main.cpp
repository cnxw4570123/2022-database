#include <algorithm>
#include <cstring>
#include <iostream>
#include <queue>
#include <cmath>

using namespace std;
#define FastIO                                                                 \
    ios_base::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr)
#define MAX 10000
#define endl '\n'
bool isPrime[MAX];
typedef long long ll;
bool v[MAX];
void Era() {
    fill_n(isPrime, MAX, true);
    isPrime[0] = isPrime[1] = false;

    for (int i = 2; i <= sqrt(MAX); i++) {
        if (!isPrime[i]) continue;
        for (int j = 2; j * i <= MAX; j++) {
            isPrime[j * i] = false;
        }
    }
}

void BFS(int start, int end) {
    memset(v, false, sizeof(v));
    queue<pair<int, int>> q;
    q.push({start, 0});
    v[start] = true;
    while (!q.empty()) {
        int current = q.front().first, cnt = q.front().second;
        q.pop();
        if (current == end) {
            cout << cnt << endl;
            return;
        }
        for (int i = 0; i < 4; i++) {
            string temp = to_string(current);
            for (int j = 0; j < 10; j++) {
                temp[i] = j + '0';
                int candidate = stoi(temp);
                if (candidate > 10000 || candidate < 1000 || v[candidate] ||
                    !isPrime[candidate])
                    continue;
                v[candidate] = true;
                q.push({candidate, cnt + 1});
            }
        }
    }
    cout << "Impossible" << endl;
}
int T, s, e;
int main() {
    FastIO;
    Era();
    cin >> T;
    while (T-- > 0) {
        cin >> s >> e;
        BFS(s, e);
    }

    return 0;
}
