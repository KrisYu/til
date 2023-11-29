# C++ reverse vector

[How do I reverse a C++ vector?](https://stackoverflow.com/questions/8877448/how-do-i-reverse-a-c-vector)

```
#include <vector>
#include <algorithm>

int main() {
  std::vector<int> a;
  std::reverse(a.begin(), a.end());
  return 0;
}
```