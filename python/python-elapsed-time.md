# python elapsed time

[How do I measure elapsed time in Python?](https://stackoverflow.com/questions/7370801/how-do-i-measure-elapsed-time-in-python)

```
import time

start = time.time()
print("hello")
end = time.time()
print(end - start)
```