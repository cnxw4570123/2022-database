#include <algorithm>
#include <cmath>
#include <cstring>
#include <iostream>
#include <queue>

using namespace std;
#define FastIO                                                                 \
    ios_base::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr)
#define MAX 1000001
#define endl '\n'
#define All(v) v.begin(), v.end()

int L, C;
string letters;
char letter;
bool v[15];
vector<string> ans;
void make_per(int idx, int cnt) {
    if (cnt == L) {
        string temp;
        for (int i = 0; i < C; i++) {
            if (v[i]) temp += letters[i];
        }
        ans.push_back(temp);
        return;
    }
    for (int i = idx; i < C; i++) {
        if (v[i]) continue;
        v[i] = true;
        make_per(i, cnt + 1);
        v[i] = false;
    }
}

int main() {
    FastIO;
    cin >> L >> C;
    for (int i = 0; i < C; i++) {
        cin >> letter;
        letters += letter;
    }
    sort(All(letters));
    make_per(0, 0);

    int pos;
    for (auto s : ans) {
        // **최소 두 개의 자음으로 구성되어 있다고 알려져 있다**
        int vCount = 0, cCount = 0;
        for (int i = 0; i < L; i++) {
            if(s[i] == 'a' || s[i] == 'e' || s[i] == 'i' || s[i] == 'o' || s[i] == 'u')
                vCount++;
            else
                cCount++;
        }
        if (vCount > 0 && cCount > 1) cout << s << endl;
    }
    return 0;
}
