# Ignore everything except cpp and h

[https://stackoverflow.com/questions/52211619/how-can-i-ignore-everything-but-cpp-files](How can I ignore everything but *.cpp files)


vim `.gitignore`

```
# Ignore Everything
*

# But not .cpp
!*.cpp
!*.h
# Or directories
!*/
!.gitignore
!README.md
```