/*
Вариант-4
1) Дана последовательность натуральных чисел {Aj}. Найти сумму чисел, оканчивающихся цифрой 0 или 7,
наибольшее из таких чисел и номер этого числа в последовательности.
2) Дано натуральное число N (N<10^9). Найти сумму нечетных цифр числа N.
*/

#include <iostream>
using namespace std;
int main()
{
    int j;
    int res = 0;
    int max = -1;
    int max_start = max;
    int index = 0;
    cout << "1) enter number" << endl;
    cin >> j;
    for (int i = 0; i < j; i++)
    {
        int current;
        cin >> current;
        if (current % 10 == 7 || current % 10 == 0)
        {
            res += current;
            if (current > max)
            {
            max = current;
            index = i + 1;
            }
        }
        
    }
    cout << "Summa = " << res << endl;
    if (max == max_start)
    {
        cout << "Error: not good number for max and index" << "\n";
    }
    else
    {
        cout << "Max = " << max << endl;
        cout << "Index = " << index << endl;
    }
    
    cout << "2) enter n" << "\n";
    int n;
    int sum = 0;
    cin >> n;
    while (n > 0)
    {
        int digit = n % 10;
        if (digit % 2 ==1)
        {
            sum += digit;
        }
        n /= 10;
    }
    cout << "Result = " << sum;
}