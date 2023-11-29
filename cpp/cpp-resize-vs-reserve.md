# resize vs reserve

## ChatGPT explain

Person: 
- what is the difference between resize and reserve

ChatGPT: 

- `resize` and `reserve` are both methods used with C++ containers (like vectors) to manage their capacity, but they serve different purposes: 
1. **resize** : This function is used to change the size of a container. When you resize a container, you are either expanding or shrinking it. If you expand it, new elements are added, and they might be initialized to a default value. If you shrink it, elements are removed from the end.

Example:

```cpp
std::vector<int> v = {1, 2, 3};
v.resize(5);  // Increase size to 5, new elements are default-initialized (int's default value, 0 in this case)
``` 
2. **reserve** : This function is used to allocate memory for the container without changing its size. It does not change the number of elements in the container; it only reserves space to accommodate a specified number of elements. This can be useful when you know in advance that you will be adding a certain number of elements to the container, as it can prevent reallocation and improve performance.

Example:

```cpp
std::vector<int> v;
v.reserve(100);  // Reserve memory for at least 100 elements, but the size of the vector is still 0
```

In summary: 
- `resize` is for changing the size of a container. 
- `reserve` is for pre-allocating memory without changing the size of a container.

It's worth noting that `resize` may implicitly invoke default constructors or value initialization for new elements (depending on the container and the element type), while `reserve` does not add any elements; it just ensures that enough memory is allocated.


## example

```
#include <iostream>

using namespace std;
int main(int argc, char *argv[]) {
    
    vector<int> b = {1,2,3};
    vector<int> c = {3,4,5};
    
    cout << b.size() << '\n';
    cout << c.size() << '\n';
    
    
    std::vector<int> b_c;
    
    
    b_c.resize(b.size() + c.size() - 1);
    
    cout << b_c.size() << '\n';
    
    b_c.insert(b_c.end(), b.begin(), b.end());
    b_c.insert(b_c.end(), c.begin() + 1, c.end());
    
    cout << b_c.size() << '\n';


    // Print the concatenated vector
    std::cout << "Concatenated vector: ";
    for (const auto& element : b_c) {
        // Assuming vec3 has an appropriate way to print its elements
        std::cout << element << " ";
    }
}
```

output:

```
3
3
5
10
Concatenated vector: 0 0 0 0 0 1 2 3 4 5 
```

change to `b_c.reserve(b.size() + c.size() - 1);`, output:


```
3
3
0
5
Concatenated vector: 1 2 3 4 5 
```

So, to concatenat use reserve.