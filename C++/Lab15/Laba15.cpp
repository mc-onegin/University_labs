#include <iostream>
#define NOMINMAX
template <typename vec>

class Vector{
    private:
        size_t len;
        size_t capc;
        vec* array;
    public:
        Vector(){
            len = 0;
            capc = 0;
            array = nullptr;
        }
        Vector(int length, vec value = vec()){
            array = new vec[length];
            len = length;
            capc = length;
            for(size_t i = 0; i < length; i++)
                array[i] = value;
        }
        Vector(const Vector& other){
            len = other.len;
            capc = other.capc;
            array = new vec[capc];
            for (size_t i = 0; i < len; i++) {
                array[i] = other.array[i];
            }
        }

        Vector& operator=(const Vector& other) {
            if (this == &other)
                return *this;
    
            delete[] array;
            len = other.len;
            capc = other.capc;
            array = new vec[capc];
    
            for (size_t i = 0; i < len; i++) {
                array[i] = other.array[i];
            }
    
            return *this;
        }
    
        ~Vector(){
            delete[] array;
        }

        vec& operator[](size_t i){
            return array[i];
        }

        Vector& reserve(int n){
            if (n <= capc)
                return *this;
    
            vec* newArray = new vec[n];
            size_t mini;
            if(len <= n)
                mini = len;
            else
                mini = n;
            for (int i = 0; i < mini; i++) {
                newArray[i] = array[i];
            }
    
            delete[] array;
            array = newArray;
            len = mini;
            capc = n;
            return *this;
        }

        Vector& resize(int n){
            if(n <= capc){
                len = n;
                return *this;
            }
            vec* newArray = new vec[2 * n];
    
            for (size_t i = 0; i < n; i++) {
                newArray[i] = array[i];
            }
    
            delete[] array;
            array = newArray;
            capc = 2 * n;
            len = n;
            return *this;
        }

        

        Vector& shrink_to_fit(){
            if (len == capc)
                return *this;

            vec* newArray = new vec[len];
            for (size_t i = 0; i < len; i++) {
                newArray[i] = array[i];
            }

            delete[] array;
            array = newArray;
            capc = len;
            return *this;
        }

        vec* front(){
            if(len == 0)
                return nullptr;
            return &array[0];
        }

        vec* back(){
            if(len == 0)
                return nullptr;
            return &array[len - 1];
        }

        size_t size(){
            return len;
        }

        bool empty(){
            return len == 0;
        }

        size_t capacity(){
            return capc;
        }

        Vector& push_back(const vec& elem){
            if (len + 1 > capc)
                this->reserve(2*(len + 1));
            array[len] = elem;
            len++;
            return *this;
        }

        Vector& insert(int index, const vec& elem){
            if (len + 1 > capc)
                this->reserve(len + 1);
            
            for (size_t i = len; i > index; i--)
                array[i] = array[i - 1];

            array[index] = elem;
            len++;
            return *this;
        }

        Vector& erase(size_t index){
            for (size_t i = index; i < len - 1; i++) {
                array[i] = array[i + 1];
            }
            len--;
            return *this;
        }

        

        friend std::ostream& operator<<(std::ostream& out, const Vector& array); // Позволяет обратиться к private переменным
        friend std::istream& operator>>(std::istream& in, Vector<int>& mas);
};

std::ostream& operator<<(std::ostream& out, const Vector<int>& mas){
        for (size_t i = 0; i < mas.len; i++){
            out << mas.array[i] << " ";
        }
        return out;
    }
    
std::istream& operator>>(std::istream& in, Vector<int>& mas){
    int tmp;
    in >> tmp;
    mas.push_back(tmp);
    return in;
}

int main(){
    Vector<int> vec(4, 3);
    Vector<int> array = vec;
    Vector<int> vec2(5);
    for(int i = 0; i < vec2.size(); i++)
        std::cin >> vec2[i];
    std::cout << vec2 << std::endl;
    /*array.insert(1, 15);
    array.erase(2);
    array.push_back(10);
    std::cout << array << std::endl;
    std::cout << array.size() << std::endl;
    array.resize(20);
    std::cout << array.size() << std::endl;
    std::cout << array.capacity() << std::endl;
    array.reserve(50);
    std::cout << array.capacity() << std::endl;
    */
    /*std::cout << array << std::endl;
    array.shrink_to_fit();
    std::cout << array.capacity() << std::endl;
    std::cout << array[1] << std::endl;
    Vector<int> vec2(array);
    std::cout << vec2 << std::endl;
    std::cout << vec2.size() << std::endl;
    std::cout << *array.front() << std::endl;
    std::cout << *array.back() << std::endl;
    */


    return 0;
}