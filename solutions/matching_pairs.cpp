#include <bits/stdc++.h>

using namespace std;

int main(int argc, char const *argv[])
{
    int n;
    cin >> n;
    vector<string> p;
    for (size_t i = 0; i < n; i++)
    {
        string e;
        cin >> e;
        p.push_back(e);
    }

    int count = 0;

    for (size_t i = 0; i < n; i++)
    {
        string a = p[i];
        for (size_t j = 0; j < n; j++)
        {
            if (i != j)
            {
                bool isMatching = true;

                string b = p[j];
                if (a.size() != b.size())
                {
                    continue;
                }

                for (size_t x = 0; x < a.size(); x++)
                {
                    for (size_t y = 0; y < a.size(); y++)
                    {
                        if ((a.at(x) == a.at(y)) && (b.at(x) != b.at(y)) || (b.at(x) == b.at(y)) && (a.at(x) != a.at(y)))
                        {
                            isMatching = false;
                        }
                    }
                }

                
                if (isMatching) {
                    // cout << a << " " << b << endl;
                    count++;
                }
                
            }
        }
    }

    cout << count / 2;

    return 0;
}
