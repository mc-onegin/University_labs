#include "func.hpp"

int main()
{
    int n;
    int count_mini = 1;
    int count_prime = 0;
    int matrix[N_MAX][N_MAX];
    int mas_multi[N_MAX];
    cin >> n;
    Read(matrix, n, count_mini, count_prime);
    if((count_mini == 2) && (count_prime >= 2))
        {
            get_multi(matrix, n, mas_multi);
            Processing(matrix, n, mas_multi);         
        }
    Write(matrix, n);
    return 0;
}