#include <iostream>
#include <Windows.h>
using namespace std;
/*
Вариант 4.
1) Ввести натуральные числа A, B и C. Если A+B кратно C и C кратно B, то вывести (A+B)/C-C/B,
если A+B кратно C и C не кратно B, то вывести (A+B)/С+B*C, в остальных случаях вывести A-B+C.
2) Ввести число N, которое обозначает некоторую ошибку. При помощи оператора switch расшифровать значение ошибки.
Список ошибок:
0 – все хорошо, 1 – ошибка чтения файла, 2 – ошибка записи файла, 3 – не все поля определены.
Предусмотреть обработку ошибочного ввода N.
3)Переменная x может принимать 2 значения: -1 и 1. Если -1, то вывести в консоль “Negative number”,
если положительное - “Positive number”. Предложить вариант программы и объяснить свой выбор.
*/
int main()
{
    SetConsoleCP(65001);
    SetConsoleOutputCP(65001);
    int a, b, c;
    cout << "1) Enter natural numbers a, b and c" << "\n";
    cin >> a >> b >> c;
    if (a < 1 || b < 1 || c < 1)
    {
        cout <<"Not natural numbers" << "\n";
    }
    else
    {
        if ((a + b) % c == 0){
        if (c % b == 0) {
            cout << ((a + b) / c) - (c / b) << "\n";
        } else {
            cout << ((a + b) / c) + (b * c) << "\n";
        }
    } else {
        cout << a - b + c << "\n";
    }
    }
    
    cout << "2) Введите код ошибки" << "\n";
    int n;
    cin >> n;
    switch(n)
    {
        case 0:
            cout << "Всё хорошо" << "\n";
            break;
        case 1:
            cout << "ошибка чтения файла" << "\n";
            break;
        case 2:
            cout << "ошибка записи файла" << "\n";
            break;
        case 3:
            cout << "не все поля определены" << "\n";
            break;
        default:
            cout << "Неверное значение n" << "\n";
    }
    cout << "3) Введите значение x = 1 или -1" << "\n";
    int x;
    cin >> x;
    cout << (x == 1 ? "Positive number" : "Negative number") << "\n";
}