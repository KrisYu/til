# image background transparent <-> white



## transparent -> white

single image:


```
mogrify -background white -flatten image.png
```

pngs:

```
mogrify -background white -flatten *.png
```



## white -> transparent

```
convert 11.png -fuzz 32% -transparent #ffffff out.png
```



ref:

- [ImageMagick](https://imagemagick.org)
- [Replace transparency in PNG image with white background](https://stackoverflow.com/questions/2322750/replace-transparency-in-png-image-with-white-background)
- [Making white background transparent using ImageMagick](https://stackoverflow.com/questions/46730399/making-white-background-transparent-using-imagemagick)