#include <iostream>
template <typename T, int N, int M>

class Matrix{
    private:
        T matrix[N][M];
    public:
        Matrix(){
            for(size_t i = 0; i < N; i++)
                for(size_t j = 0; j < M; j++)
                    matrix[i][j] = T();

        }
        /*Matrix(){
            matrix = new T*[N];
            for(int i = 0; i < N; i++)
                matrix[i] = new T[M];
            n = N;
            m = M;
        }
        */

        Matrix(const Matrix& other){
            for(size_t i = 0; i < N; i++)
                for(size_t j = 0; j < M; j++)
                    matrix[i][j] = other.matrix[i][j];
        }

        Matrix& operator=(const Matrix& other){
            if(this == &other)
                return *this;
            for(size_t i = 0; i < N; i++)
                for(size_t j = 0; j < M; j++)
                    matrix[i][j] = other.matrix[i][j];
            return *this;
            
        }

        ~Matrix() = default;

        T get(size_t row, size_t column) {
            return matrix[row][column];
        }

        void set(size_t row, size_t column, T data){
            matrix[row][column] = data;
        }
        
        Matrix& operator++(){
            for(int i = 0; i < N; i++)
                for(int j = 0; j < M; j++)
                    ++matrix[i][j];
            return *this;
        }

        Matrix<T, N, M> operator+(const Matrix<T, N, M>& other) const {
            Matrix<T, N, M> result;
            for (int i = 0; i < N; ++i){
                for (int j = 0; j < M; ++j){
                    result.matrix[i][j] = matrix[i][j] + other.matrix[i][j];
                }
            }
            return result;
        }

        Matrix& operator+=(const Matrix& other){
            *this = *this + other;
            return  *this;
        }

        template<int new_M>
        Matrix<T, N, new_M> operator*(Matrix<T, M, new_M>& other){
            Matrix<T, N, new_M> arr;
            for(int i = 0; i < N; i++){
                for(int j = 0; j < new_M; j++){
                    T a = T();
                    for(int k = 0; k < M; k++)
                        a += get(i, k) * other.get(k, j);
                    arr.set(i, j, a);
                }             
            }
            return arr;
        }

        Matrix& operator*=(Matrix& other){
            *this = *this * other;
            return  *this;
        }

        T det(){
            if(N == M){
                if(N == 1)
                    return matrix[0][0];
                if(N == 2)
                    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0];
                return ((matrix[0][0] * matrix[1][1] * matrix[2][2]) + (matrix[1][0] * matrix[2][1] * matrix[0][2]) +
                    (matrix[0][1] * matrix[1][2] * matrix[2][0])) - ((matrix[0][2] * matrix[1][1] * matrix[2][0]) +
                    (matrix[0][0] * matrix[1][2] * matrix[2][1]) + (matrix[1][0] * matrix[0][1] * matrix[2][2]));
            }
            else return -1;
        }

        friend std::ostream& operator<<(std::ostream& out, const Matrix<T, N, M>& arr){
            for(int i = 0; i < N; i++){
                for(int j = 0; j < M; j++){
                    out << arr.matrix[i][j] << " ";
                }
                out << std::endl;
            }
            return out;
        }

        friend std::istream& operator>>(std::istream& in, Matrix<T, N, M>& arr){
            for(int i = 0; i < N; ++i){
                for(int j = 0; j < M; ++j){
                    in >> arr.matrix[i][j];
                }
            }
            return in;
        }
};


int main(){
    Matrix<int, 2, 2> arr;
    std::cout << "input matrix arr: " << std::endl;;
    std::cin >> arr;
    std::cout << std::endl;

    Matrix<int, 2, 2> mas;
    std::cout << "input matrix mas: " << std::endl;
    std::cin >> mas;
    std::cout << std::endl;

    Matrix<int, 2, 2> A = arr * mas;
    
    std::cout << "matrix A: " << std::endl;
    std::cout << A << std::endl;;

    ++arr;
    arr.set(0, 1, 100);
    std::cout << "matrix arr after ++ and set: " << std::endl;
    std::cout << arr << std::endl;
    std::cout << "det A: " <<  A.det();

    return 0;
}