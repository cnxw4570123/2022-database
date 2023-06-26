#include <algorithm>
#include <cmath>
#include <cstring>
#include <iostream>
#include <queue>

using namespace std;
#define FastIO                                                                 \
    ios_base::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr)
#define MAX 21
#define endl '\n'
#define All(v) v.begin(), v.end()

typedef pair<pair<int, int>, int> piii;

int R, C, dy[] = {-1, 1, 0, 0}, dx[] = {0, 0, -1, 1}, ans = 0;
char Map[MAX][MAX];
bool alphabet[26];
void DFS(int y, int x, int dist) {
    for (int i = 0; i < 4; i++) {
        int ny = y + dy[i], nx = x + dx[i];
        if (ny > R || nx > C || ny < 1 || nx < 1 || alphabet[Map[ny][nx] - 'A'])
            continue;
        alphabet[Map[ny][nx] - 'A'] = true;
        DFS(ny, nx, dist + 1);
        alphabet[Map[ny][nx] - 'A'] = false;
    }
    ans = max(ans, dist);
}

int main() {
    FastIO;
    cin >> R >> C;

    for (int i = 1; i < R + 1; i++) {
        for (int j = 1; j < C + 1; j++) {
            cin >> Map[i][j];
        }
    }
    alphabet[Map[1][1] - 'A'] = true;
    DFS(1, 1, 1);
    cout << ans;
    return 0;
}
