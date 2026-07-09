#include <iostream>
#include <string>
#include <fstream>

int stringLength(const std::string& str)
{
    if (str.empty())
        return 0;
    return 1 + stringLength(str.substr(1));
}

void QuickSort(int a, int b, int* arr)
{
    if(a >= b)
        return;
    int m = arr[(a + b) / 2];
    int left = a - 1;
    int right = b + 1;
    while(1)
    {
        do left++; while(arr[left] < m);
        do right--; while(arr[right] > m);
        if(left >= right)
            break;
        std::swap(arr[left], arr[right]);
    }
    left = right;
    right++;
    QuickSort(a, left, arr);
    QuickSort(right, b, arr);
}

void Search(int i, int j, int step, int n, int m,
            char field[100][100], int table[100][100])
{
    if (step >= table[i][j])
        return;

    table[i][j]=step;

    if (field[i][j] == 'E')
        return;

    if(i + 1 < n && field[i+1][j] != '#') 
        Search(i+1,j,step+1,n,m, field, table);
    if(i - 1 >= 0 && field[i-1][j] != '#') 
        Search(i-1,j,step+1,n,m, field, table); 
    if(j + 1 < m && field[i][j+1] != '#') 
        Search(i,j+1,step+1,n,m, field, table);
    if(j - 1 >= 0 && field[i][j-1] != '#') 
        Search(i,j-1,step+1,n,m, field, table);
    if(j + 1 < m && i + 1 < n && field[i+1][j+1] != '#') 
        Search(i+1,j+1,step+1,n,m, field, table);
    if(j - 1 >= 0 && i - 1 >= 0 && field[i-1][j-1] != '#') 
        Search(i-1,j-1,step+1,n,m, field, table);
    if(j - 1 >= 0 && i + 1 < n && field[i+1][j-1] != '#') 
        Search(i+1,j-1,step+1,n,m, field, table);
    if(j + 1 < m && i - 1 >= 0 && field[i-1][j+1] != '#') 
        Search(i-1,j+1,step+1,n,m, field, table);
}

int main()
{
    /*
    std::string s;
    std::getline(std::cin, s);
    int length = stringLength(s);
    std::cout << "Length is: " << length << std::endl;
    */

    /*
    int n;
    std::cin >> n;
    int arr[1000];
    for(int i = 0; i < n; i++)
        std::cin >> arr[i];
    QuickSort(0, n - 1, arr);
    for(int i = 0;i < n; i++)
        std::cout << arr[i] << " ";
        
    return 0;
    */
    



   
    char field [100][100];
    int table [100][100];
    std::ifstream in ("input.txt");
    int n, m;
    int is, js;
    int ie, je;
    in >> n >> m;
    for(int i=0; i<n;i++) 
        for(int j=0; j<m; j++)
        {
            table[i][j] = INT_MAX;
            in >> field[i][j];
            if (field[i][j] == 'S')
            {
                is=i;
                js=j;
            }
            else if (field[i][j] == 'E')
            {
                ie=i;
                je=j;
            }
        }
    Search(is, js, 0, n, m, field, table);

    if (table[ie][je] == INT_MAX) 
        std::cout << "No solutions" << std::endl; 
    else
        std::cout << table[ie][je] << std::endl; 
    return 0;
    
}