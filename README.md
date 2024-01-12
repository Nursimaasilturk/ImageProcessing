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

![negative image](https://github.com/Nursimaasilturk/ImageProcessing/blob/master/assets/negative-image.png)

### <font color="SpringGreen">Log Transformation</font>
```
s = clog(1 + r)
```

![log transformation](https://github.com/Nursimaasilturk/ImageProcessing/blob/master/assets/log-transformation.png)

### <font color="SpringGreen">Gamma Transformation</font>
```
s = cr^γ
```
![gamma transformation](https://github.com/Nursimaasilturk/ImageProcessing/blob/master/assets/gamma-transformation.png)

For Grayscale Image

![gamma transformation for grayscale image](https://github.com/Nursimaasilturk/ImageProcessing/blob/master/assets/gamma-transformation-grayscale.png)

### <font color="SpringGreen">Piecewise Linear Transformation</font>
 <font color="plum">Contrast Stretching</font>
```
Xnew= (Xi - Xmin) / (Xmax -Xmin) * 255
```
 0 - 255
![contrast  streching](https://github.com/Nursimaasilturk/ImageProcessing/blob/master/assets/contrast-stretching.png)

0 - 150

![contrast  streching](https://github.com/Nursimaasilturk/ImageProcessing/blob/master/assets/contrast-stretching-2.png)

 <font color="plum">Bit Plane Slicing</font>
 ![Bit plane Slicing](https://github.com/Nursimaasilturk/ImageProcessing/blob/master/assets/bit-plane-slicing.png)
 
### Histogram Equalization
![Histogram Equalization](https://github.com/Nursimaasilturk/ImageProcessing/blob/master/assets/histogram-equalization.png)

### Averaging Filter
```json
[1 1 1]
[1 1 1]
[1 1 1] (1/9)  -> 3x3 matrix
```
> If you use NxN matrix, you must divide elements of matrix by 1/N
![Averaging Filter](https://github.com/Nursimaasilturk/ImageProcessing/blob/master/assets/averaging-filter.png)