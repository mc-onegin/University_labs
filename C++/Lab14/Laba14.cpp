#include <iostream>
#include <string>
#define N_MAX 1000
class BigInt {
    char m_value[N_MAX];
    short m_size = 0;
    public:
        BigInt() = default;
        BigInt(const std::string& value) {
            size_t len = value.length();
            for(int i = 0; i < len; i++)
                m_value[i] = value[len - i - 1] - '0';
            for(int i = len; i < N_MAX; i++)
                m_value[i] = 0;
            m_size = len;
        }
        

        BigInt& operator+=(const BigInt& other){
            for(int i = 0; i < std::max(m_size, other.m_size); i++){
                m_value[i] += other.m_value[i];
                if(m_value[i] > 9){
                    m_value[i] -= 10;
                    m_value[i+1]++;
                    if(i + 1 == m_size)
                        m_size++;
                }
            }
            m_size = std::max(m_size, other.m_size);
            return *this;
        }

        BigInt operator+(const BigInt& other){
            BigInt result(*this);
            result += other;
            return result;
        }

        BigInt& operator*=(const BigInt& other){
            *this = *this * other;
            return *this;
        }

        BigInt operator*(const BigInt& other) const{
            BigInt result("0");
            std::string s;
            
            for (int j=0; j<other.m_size; ++j) {
                int cnt = 0;
                s = "";
                char sub_result[N_MAX * 2 + 1];
                int num, el = 0;
                for(int i = 0; i < m_size; i++){
                    num = (m_value[i]) * (other.m_value[j]) + el;
                    if (num > 9){
                        el = num / 10;
                    }
                    cnt++;
                    sub_result[i] = num % 10;
                }
                if(el != 0){
                    sub_result[cnt] = el;
                    cnt++;
                }
                el = 0;
                for(int k = cnt + j - 1; k >= j; k--){
                    sub_result[k] = sub_result[k - j];
                    }

                cnt += j;
                for(int l = 0; l < j; l++) {
                    sub_result[l] = 0;
                }
                for(int m = 0; m < cnt; m++){
                    s.insert(0, std::to_string(sub_result[m]));
                }

                BigInt a = BigInt(s);
                
                result += a;
                }
            return result;
            }

        bool operator<(const BigInt& other){
            if(m_size < other.m_size)
                return true;
            else if(m_size > other.m_size)
                return false;
            else{
                for(int i = m_size - 1; i >= 0; i--){
                    if(m_value[i] < other.m_value[i])
                        return true;
                    else if(m_value[i] > other.m_value[i])
                        return false;
                }
                return false;
            }      
        }

        bool operator>(const BigInt& other){
            if(m_size > other.m_size)
                return true;
            else if(m_size < other.m_size)
                return false;
            else{
                for(int i = m_size - 1; i >= 0; i--){
                    if(m_value[i] > other.m_value[i])
                        return true;
                    else if(m_value[i] < other.m_value[i])
                        return false;
                }
                return false;
            }      
        }

        bool operator>=(const BigInt& other){
            return !(*this < other);   
        }

        bool operator==(const BigInt& other){
            bool flag = true;
            for(int i = m_size - 1; i >= 0; i--){
                if(m_value[i] != other.m_value[i])
                    flag = false;
            }
            if(flag)
                return true;
            else
                return false;
        }

        bool operator!=(const BigInt& other){
            return !(*this == other);
        } 
    
    friend std::ostream& operator<<(std::ostream& out, const BigInt& other);
    friend std::istream& operator>>(std::istream& in, BigInt& other);
};

std::istream& operator>>(std::istream& in, BigInt& other){
    std::string s;
    in >> s;
    other = BigInt(s);
    return in;
}

std::ostream& operator<<(std::ostream& out, const BigInt& other){
    for (int i=0; i < other.m_size; i++)
        out << static_cast<short>(other.m_value[other.m_size - i - 1]);
    return out;
}

int main(){
    BigInt x, y;
    std::cin >> x >> y;
    BigInt z = x * y;

    x += y;

    x == y ? std::cout << x << " == " << y << std::endl : std::cout << x << " != " << y << std::endl;

    if(x < y)
        std::cout << x << " < " << y << std::endl;
    if(x > y)
        std::cout << x << " > " << y << std::endl;

    std::cout << "x * y = " << z << std::endl;
    std::cout << "x += y = " << x << std::endl;

    return 0;
}