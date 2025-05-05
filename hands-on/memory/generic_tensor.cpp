#include <iostream>


/// @brief  complie-time function to calculate the size of tensor at compliation 
/// @tparam ...Args  a set of integers
/// @return size of tensor
template<class... Args>
constexpr int getSize(Args... args)
{
    int res = 1;
    for (auto arg: {args...})
    {
        res *= arg;
    }
    return res;
}

/// @brief           generic tensor with known size at compile-time consuming non-dynamic memory
/// @tparam    T     element type
/// @tparam ...U     set of integers defining the dimension of tensor
template<class T, int... U>
struct Tensor{
    static constexpr int nameSize = 10;
    const int size = getSize(U...);
    int dims[sizeof...(U)] = {U...};
    T data[getSize(U...)];
    char name[nameSize] = {' ', ' ', ' ', ' ',' ', ' ',' ', ' ',' ', ' '};
};


int main()
{
    Tensor<float, 4, 3, 2, 2> tensor;
    tensor.name[0] = 'i';
    tensor.name[1] ='n';
    tensor.name[2] = 'p';
    tensor.name[3] ='u';
    tensor.name[4] = 't';

    std::cout<<"tensor size: "<< tensor.size<<"\n";
    std::cout<<"tensor name: "<< tensor.name<<"\n";
    std::cout<<"batch size: "<< tensor.dims[0]<<"\n";
    std::cout<<"channel size: "<< tensor.dims[1]<<"\n";
    std::cout<<"height: "<< tensor.dims[2]<<"\n";
    std::cout<<"width: "<< tensor.dims[3]<<"\n";
}
