#include <iostream>
#include <cmath>
using namespace std;
/*
Лаборатораня работа №1
1) Дать определение переменной, понять, что это такое.
2) Перечислить основные типы данных в С++: целочисленные (знаковые и беззнаковые), вещественные, символьные, логические.
3) Указать для каждого типа размер в байтах.
4) Указать минимальное и максимальное значение для каждого типа.
5) Составить программу, которая выводит название типа, размер, мин. и макс. значения.
6) Привести пример выполнения арифметической операции с каждым типом данных.
7) Программу желательно оформить с использованием CMake и загрузить на удаленное хранилище репозиториев*.

Решение:

1) Переменная - это именованная ячейка памяти устройства, предназначенная для хранения информации.
2) Целочисленные: short, unsigned short, int, unsigned int, long, unsigned long, long long, unsigned long long
   Вещественные: float, double, long double
   Символьные: unsigned char, char
   Логические: bool
3, 4) Переменная ------- Размер в байтах ------- min/max size
      short              2                      -32_768 / 32_768
      unsigned short     2                       0 / 65_535
      int                2/4  (16/32 разрядов)   -32_768 / 32_767    /    -2_147_483_648 / 2_147_483_647 
      unsigned int       2/4  (16/32 разрядов)   0 / 65_535   /   0 / 4_294_967_295
      long               4                       -2_147_483_648 / 2_147_483_647
      unsigned long      4                       0 / 4_294_967_295
      long long          8                       -1 * 2^63 / 2^63 - 1
      unsigned long long 8                       0 / 2^64 - 1
      ---------------------
      float              4                       1.2e-38 / 3.4e + 38
      double             8                       2.2e-308 / 1.7e+308
      long double        10                      1.7e-4932 / 1.7e + 4932
      ---------------------
      unsigned char      1                       0 / 255
      char               1                       -128 / 127
      ---------------------
      bool               1                       0 / 1

*/
int main()
{

// 5)
cout << 
  " short              2                      -32_768 / 32_768" << endl << 
  " unsigned short     2                       0 / 65_535 " << endl << 
  " int                2/4  (16/32 razrydov)   -32_768 / 32_767    /    -2_147_483_648 / 2_147_483_647" << endl << 
  " unsigned int       2/4  (16/32 razrydov)   0 / 65_535   /   0 / 4_294_967_295" << endl << 
  " long               4                       -2_147_483_648 / 2_147_483_647" << endl << 
  " unsigned long      4                       0 / 4_294_967_295" << endl << 
  " long long          8                       -1 * 2^63 / 2^63 - 1" << endl << 
  " unsigned long long 8                       0 / 2^64 - 1" << endl << 
  " --------------------- " << endl << 
  " float              4                       1.2e-38 / 3.4e + 38" << endl << 
  " double             8                       2.2e-308 / 1.7e+308 " << endl << 
  " long double        10                      1.7e-4932 / 1.7e + 4932 " << endl << 
  " --------------------- " << endl << 
  " unsigned char      1                       0 / 255" << endl << 
  " char               1                       -128 / 127" << endl << 
  " --------------------- " << endl << 
  " bool               1                       0 / 1"  << endl;
  
// 6)

   cout << endl << endl;

   short as = -2, bs = 5;
   cout << "short: " << as <<" * "<< bs <<" = "<<(as * bs) << endl;

   unsigned short aus = 2, bus = 7;
   cout << "unsigned short: " << aus <<" + "<< bus <<" = "<<(aus + bus) << endl;

   int ai = -247, bi = 73656871;
   cout << "int: " << ai <<" + "<< bi <<" = "<<(int)(ai + bi) << endl;

   unsigned int aui = 30000, bui = 237867;
   cout << "unsigned int: " << aui <<" + "<< bui <<" = "<<(unsigned int)(aui + bui) << endl;

   long al = -27802783, bl = 536782235;
   cout << "long: " << al <<" * "<< bl <<" = "<<(al * bl) << endl;

   unsigned long aul = 575678765, bul = 823752889;
   cout << "unsigned long: " << aul <<" * "<< bul <<" = "<<(aul * bul) << endl;

   long long all = -27527, bll = 33874;
   cout << "long long: " << all <<" * "<< bll <<" = "<<(all * bll) << endl;

   unsigned long long aull = 247546, bull = 545298;
   cout << "unsigned long long: " << aull <<" * "<< bull <<" = "<<(aull * bull) << endl;

   float af = 2.5, bf = 4.9;
   cout << "float: " << af <<" + "<< bf <<" = "<<(float)(af + bf) << endl;

   double ad = pow(2.0, 20.0), bd = pow(3.0, 10.0);
   cout << "double: " << ad <<" + "<< bd <<" = "<<(ad + bd) << endl;

   long double ald = pow(2.0, 1000.0), bld = pow(5.0, 428.0);
   cout << "long double: " << ald <<" - "<< bld <<" = "<<(ald - bld) << endl;

   unsigned char auc = -20, buc = 36;
   cout << "unsigned char: " << auc <<" + "<< buc <<" = "<<(unsigned char)(auc + buc) << endl;

   char ac = -84, bc = 20;
   cout << "char: " << ac <<" + "<< bc <<" = "<< (char)(ac + bc) << endl;

   bool ab = 1, bb = 0;
   cout << "bool: " << ab <<" + "<< bb <<" = "<<(ab + bb) << endl;

   return 0;
}