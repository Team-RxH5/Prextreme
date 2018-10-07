#include <bits/stdc++.h>

using namespace std;

int counter(int n, int sum)
{
    if (n == 0)
        return sum == 0 ? 1 : 0;
    if (sum == 0)
        return 1;
    int count = 0;
    for (int i = 0; i <= 9; i++)
    {
        if (sum - i >= 0)
        {
            count += counter(n - 1, sum - i);
        }
    }

    return count;
}

int main()
{
    int N, sum;
    cin >> N >> sum;
    if (sum % 2 == 0)
    {
        int count = counter(N, sum / 2);
        cout << count * count;
    }
    else
    {
        cout << 0;
    }
    return 0;
}