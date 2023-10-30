# <font color="cyan">Image Processing</font>

## <font color="MediumSlateBlue">Spatial Domain Processing</font>
* <font color="MediumVioletRed">Intensity Transformation</font>
    * <font color="MediumOrchid">Contrast Enhancement</font>
    * <font color="MediumOrchid">Image Thresholding</font>
* <font color="MediumVioletRed">Spatial Filtering</font>
    * <font color="MediumOrchid">Sparpening</font>


##  <font color="Turquoise">Intensity Transformation Function</font>
<font color="SpringGreen">Basic Function</font>

```
s = T(r)
```
Some Intensity Transformation Functions
### <font color="SpringGreen">Image Negative</font>
```
s = T(r) = L - 1 - r 
```
> L-1 ; Max-intensity value - 255 for 8-bit image -
> r ; pixel value

![alt text](https://github.com/Nursimaasilturk/ImageProcessing/blob/master/assets/negative-image.png)