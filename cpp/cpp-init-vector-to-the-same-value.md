# c++ init vector to the same value

- [Can I initialize an STL vector with 10 of the same integer in an initializer list?](https://stackoverflow.com/questions/10237751/can-i-initialize-an-stl-vector-with-10-of-the-same-integer-in-an-initializer-lis)

```
int number_of_elements = 10;
int default_value = 1;
std::vector<int> vec(number_of_elements, default_value);
```

- [Fastest way to reset every value of std::vector<int> to 0](https://stackoverflow.com/questions/8848575/fastest-way-to-reset-every-value-of-stdvectorint-to-0)

```
std::fill(v.begin(), v.end(), 0);
```

