# xmake


### simple xmake example  

```
add_requires("wxwidgets")
add_requires("boost")

target("Project")
    set_kind("binary")
    set_languages("cxx17")
    
    add_packages("wxwidgets")
    add_packages("boost")

    add_files("*.cpp")
```

### xmake -> Xcode

```
xmake project -k xcode 
```
or

```
xmake project -k xcode -m debug
```