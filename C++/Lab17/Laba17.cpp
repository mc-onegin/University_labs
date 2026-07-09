#include <iostream>

class BoolVector{
    private:
        char* data;
        size_t bytes;
        size_t bits;
    public:
        BoolVector(){
            data = nullptr;
            bytes = 0;
            bits = 0;
        }
        ~BoolVector(){
            delete [] data;
        }
        void set_0(size_t index){
            size_t index_byte = index / 8;
            size_t index_bit = index % 8;
            data[index_byte] &= ~(1 << index_bit);
        }
        void set_1(size_t index){
            size_t index_byte = index / 8;
            size_t index_bit = index % 8;
            data[index_byte] |= (1 << index_bit);
        }
        bool get(size_t index){
            size_t index_byte = index / 8;
            size_t index_bit = index % 8;
            return (data[index_byte] >> index_bit) & 1;
        }
        bool operator[](size_t index){
            return get(index);
        }
        void set_bit(size_t index, bool value){
            size_t index_byte = index / 8;
            size_t index_bit = index % 8;
            if (value)
                data[index_byte] |= (1 << index_bit);
            else
                data[index_byte] &= ~(1 << index_bit);
        }
        void push_back(bool value){
            if(bits == bytes * 8){
                size_t new_bytes;
                if(bytes)
                    new_bytes = bytes * 2;
                else
                    new_bytes = 1;
                char* newdata = new char[new_bytes];

                for (size_t i = 0; i < bytes; i++) {
                    newdata[i] = data[i];
                }
        
                delete[] data;
                data = newdata;
                bytes = new_bytes;
            }
            set_bit(bits, value);
            bits++;
        }
        size_t size(){
            return bits;
        }
        void insert(size_t index, bool value){
            if(bits == bytes * 8){
                size_t new_bytes;
                if(bytes)
                    new_bytes = bytes * 2;
                else
                    new_bytes = 1;
                char* newdata = new char[new_bytes];

                for (size_t i = 0; i < bytes; i++) {
                    newdata[i] = data[i];
                }
            }

            for(size_t i = bits - 1; i > index; i--)
                set_bit(i, get(i - 1));
            set_bit(index, value);
            bits++;
        }
        void erase(size_t index){
            for(size_t i = index; i < bits - 1; i++)
                set_bit(i, get(i + 1));
            bits--;
        }
        
};

int main(){
    BoolVector a;
    a.push_back(true);
    a.push_back(true);
    a.push_back(false);
    a.push_back(false);
    a.push_back(false);


    //std::cout << a.size() << std::endl;
    //std::cout << a[11] << std::endl;
    //a.set_bit(11, true);
    //std::cout << a[11] << std::endl;

    //a.insert(3, true);
    //std::cout << a[3] << std::endl;
    //std::cout << a[4] << std::endl;
    for(int i = 0; i < a.size(); i++)
        std::cout << a[i] << " ";
    a.insert(3, true);
    std::cout << std::endl;
    //std::cout << a[3] << std::endl;
    for(int i = 0; i < a.size(); i++)
        std::cout << a[i] << " ";


    return 0;
}