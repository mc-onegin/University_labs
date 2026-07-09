#include "func.hpp"

bool abs_isPrime(int x)
{
    if ((-2 < x) && (x < 2))
        return false;
    for (int d = 2; d <= sqrt(abs(x)); d++)
        if(x % d == 0)
            return false;
    return true;
}

void Read(int matrix[N_MAX][N_MAX], int n, int& count_mini, int& count_prime)
{
    int mini = INT_MAX;
    for(int i = 0; i < n; i++)
    {
        for(int j = 0; j < n; j++)
        {
            cin >> matrix[i][j];
            if(matrix[i][j] < mini)
            {
                mini = matrix[i][j];
                count_mini = 0;
            }
            if(matrix[i][j] == mini)
                count_mini += 1;
            
            if(abs_isPrime(matrix[i][j]))
                count_prime += 1;
        }
    }
}

void Write(int matrix[N_MAX][N_MAX], int n)
{
    cout << "\n";
    for(int i = 0; i < n; i++)
    {
        for(int j = 0; j < n; j++)
            cout << matrix[i][j] << " ";
        cout << "\n";
    }
}


void get_multi(int matrix[N_MAX][N_MAX], int n, int mas_multi[N_MAX])
{
    for(int i = 0; i < n; i++)
    {
        int multiplication = 1;
        for(int j = 0; j < n; j++)
        {
            multiplication *= matrix[i][j];
        }
        mas_multi[i] = multiplication;
    }
}


void Processing(int matrix[N_MAX][N_MAX], int n,
    int mas_multi[N_MAX])
{
    for(int i = 0; i < n - 1; i++)
    {
        for(int k = i+1; k < n;k++)
        {
            if(mas_multi[i] < mas_multi[k])
            {
                for(int j = 0; j < n; j++)
                    swap(matrix[i][j], matrix[k][j]);
                swap(mas_multi[i], mas_multi[k]);
            }
        }
    }
}
