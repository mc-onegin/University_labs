#include <iostream>
#include <cmath>
class  Parallelepiped {
    private:
        int length;
        int width;
        int height;
    public: 
        Parallelepiped(int a, int b, int c){
            length = a;
            width = b;
            height = c;}
        int area(){ 
            return 2*(length*width + length*height + width*height);}
        int volume(){
            return length * width * height;}
        float diagonal_length(){
            return sqrt(length * length + width * width + height * height);}
};
int main(){
    Parallelepiped one(3, 5, 6);
    Parallelepiped two(3, 4, 12);
    std::cout << one.area() << " " << one.volume() << " " << one.diagonal_length() << std::endl;
    std::cout << two.area() << " " << two.volume() << " " << two.diagonal_length() << std::endl;
    return 0;
}