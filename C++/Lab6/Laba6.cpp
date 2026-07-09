#include <iostream>
#include <cmath>
using namespace std;

bool Pali(int x)
{
    int n = x;
    int m = 0;
    while(n)
    {
        m = m * 10 + n % 10;
        n /= 10;
    }
    return x==m;
}

bool isPrime(int x)
{
    if (x < 2)
        return false;
    for (int d = 2; d <= sqrt(x); d++)
        if(x % d == 0)
            return false;
    return true;
}

int main()
{
    cout << "1)" << "\n";
    int mas[100];
    int n;
    cin >> n;
    bool flag = true;
    for(int i = 0;i < n; i++)
    {
        cin >> mas[i];
    }
    for(int i = 0;i < n; i++)
    {
        if(isPrime(mas[i])){
            flag = false;
            break;
        }
    }
    if(flag)
    {
        for(int i = 0; i < n - 1; i++)
                for(int j = i + 1; j < n; j++)
                {
                    if(mas[i] < mas[j])
                    {
                        int tmp = mas[i];
                        mas[i] = mas[j];
                        mas[j] = tmp;
                    }
                }
    }
    for(int i = 0;i < n; i++)
        cout << mas[i] << " ";
    cout << "\n" << "2)" << "\n";

    int mas2[100];
    int mas_first[100];
    int mas_numeral[100];
    int n2;
    cin >> n2;
    for(int i = 0;i < n2; i++){
        cin >> mas2[i];
        int x = mas2[i];
        while (x > 9)
        {
        x/=10;
        }
        mas_first[i] = x;
        int y = mas2[i];
        int mini = 10;
        while (y > 0)
        {
            if(y % 10 < mini)
                mini = y % 10;
            y /= 10;
        }
        mas_numeral[i] = mini;
    }
    for(int i = 0; i < n2 - 1; i++)
        for(int j = i + 1; j < n2; j++)
        {

            if (
                (mas_first[i] > mas_first[j]) ||
                ((mas_first[i] == mas_first[j]) && (mas_numeral[i] > mas_numeral[j])) ||
                (((mas_first[i] == mas_first[j]) && (mas_numeral[i] == mas_numeral[j])) && 
                (mas2[i] > mas2[j]))
            )
            {
                int tmp = mas2[i];
                mas2[i] = mas2[j];
                mas2[j] = tmp;

                int tmp_first = mas_first[i]; //#################
                mas_first[i] = mas_first[j];
                mas_first[j] = tmp_first;

                int tmp_numeral = mas_numeral[i];
                mas_numeral[i] = mas_numeral[j];
                mas_numeral[j] = tmp_numeral;
            
            }   
        }           
    for(int i = 0;i < n2; i++)
        cout << mas2[i] << " ";
    cout << "\n" << "3)" << "\n";

    int matrix[100][100];
    int n3, m;
    cin >> n3 >> m;
    for(int i = 0; i < n3; i++)
        for(int j = 0; j < m; j++)
            cin >> matrix[i][j];

    int summa = 0;
    int min_summa = INT_MAX;
    int number = 0;
    for(int i = 0; i < n3; i++)
    {
        for(int j = 0; j < m; j++)
        {
            summa += matrix[i][j];
        }
        if(summa < min_summa)
        {
            min_summa = summa;
            number = i;
        }
        summa = 0;
    }

    for(int k = 0; k < n3; k++)
        matrix[number][k] = min_summa;
    cout << "\n";

    for(int i = 0; i < n3; i++)
    {
        for(int j = 0; j < m; j++)
            cout << matrix[i][j] << " ";
        cout << "\n";
    }
    cout << "4)" << "\n";

    int mas4[100];
    int n4;
    cin >> n4;
    for(int i = 0;i < n4; i++)
        cin >> mas4[i];

    int j = 0;
    for(int i = 0; i < n4; i++)
    {
        if(!Pali(mas4[i])){
            mas4[j] = mas4[i];
            j++;
        }
    }
    n4 = j;

    for(int i = 0; i < n4; i++)
        if(isPrime(mas4[i]))
        {
            for(int j = n4; j > i; j--)
                mas4[j] = mas4[j-1];
            i++;
            n4++;
        }

    for(int i = 0;i < n4; i++)
        cout << mas4[i] << " ";

    return 0;
}