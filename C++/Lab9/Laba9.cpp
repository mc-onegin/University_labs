#include <iostream>
using namespace std;

int main()
{
    unsigned short n;
    cin>> n;
    unsigned short* p = &n;
    unsigned char* c= reinterpret_cast<unsigned char*>(p);
    for (int i=0; i<sizeof(n); i++)
        cout<<static_cast<unsigned short>(*(c+i)) << endl;

    return 0;
}