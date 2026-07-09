#pragma once
#include <iostream>
#include <cmath>
using namespace std;
const int N_MAX = 100;

bool abs_isPrime(int x);
void Read(int matrix[100][100], int n, int& count_mini, int& count_prime);
void Write(int matrix[100][100], int n);
void get_multi(int matrix[100][100], int n, int mas_multi[N_MAX]);
void Processing(int matrix[100][100], int n, int mas_multi[100]);
