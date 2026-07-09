#include <iostream>
using namespace std;

/*
Вариант 4.
Написать программу, которая получает на вход вещественное число R (0 < R < 100) – радиус круга.
И рассчитывает площадь круга с точностью до 10^-9.
*/

int main()
{  
cout <<"Radius: ";
double R;
cin >> R;
printf("square %.9f", R * R * acos(-1.0));

return 0;
}