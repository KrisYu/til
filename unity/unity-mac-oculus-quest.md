# Unity Mac Oculus Quest



- List devices

```
adb devices
```


- Read Debug.Log

```
adb logcat -s Unity
```



- Record time


```
private float fire_start_time;

void Update() {
    if(Input.GetButtonDown("Fire1")) {
        fire_start_time = Time.time;
    }
}

void OnTriggerEnter(Collider other) {
    Debug.Log("elapsed time: " + (Time.time - fire_start_time));
}
```