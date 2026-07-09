#include <iostream>
#include <string>
#include <cmath>

int main(){
    std::string s;
    int res[5] = {1, 2, 3, 4, 5};
    int n = 0;
    for(int i = 0; i < 5; i++)
        n = res[i] + n * 10;
    s = std::to_string(n);
    std::cout << s;
    


}