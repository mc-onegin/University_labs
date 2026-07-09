#include <iostream>
using namespace std;

/*
Вариант 4.
Установить i-ый бит числа х (0<x<10^9) в 1.

*/
int main()
{
    int a, i;
    cout << "enter number and bit" << endl;
    cin >> a;
    cin >> i;
    if ((i >= 0) && (i < 32)) {
        cout << (a | (1 << i)) << endl;
    } else {
        cout << "incorrect i";
    }
    return 0;
}
