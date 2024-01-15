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
```
[1 1 1]
[1 1 1]
[1 1 1] (1/9)  -> 3x3 matrix
```
> If you use NxN matrix, you must divide elements of matrix by 1/N

![Averaging Filter](https://github.com/Nursimaasilturk/ImageProcessing/blob/master/assets/averaging-filter.png)

### Guassian Filter
```
[1 4  6  4  1]
[4 16 24 16 4]
[6 24 36 24 6]
[4 16 24 16 4]
[1 4  6  4  1] (1/256) -> 5X5 matrix
```
> The elements of the Gaussian filter matrix must be divided by a `normalization coefficient` determined depending on the filter size. This normalization ensures that the total weights are 1.

![Guassian Filter](https://github.com/Nursimaasilturk/ImageProcessing/blob/master/assets/guassian-filter.png)

### Sobel Filter
```
[-1 0 1]         [ 1  2  1]         [p1 p2 p3]
[-2 0 2]         [ 0  0  0]         [p4 p5 p6]
[-1 0 1] -> Gx   [-1 -2 -1] -> Gy   [p7 p8 p9] -> Original Image
```
> G = |Gx| + |Gy|
> If G greater than 255, set equal to 255

![Sobel Filter](https://github.com/Nursimaasilturk/ImageProcessing/blob/master/assets/sobel-filter.png)

### Laplacian Filter
```
[0  -1  0]
[-1 -4 -1]
[0  -1  0]
```
![Laplacian Filter](https://github.com/Nursimaasilturk/ImageProcessing/blob/master/assets/laplacian-filter.png)

### Salt and Pepper
![Salt and Pepper](https://github.com/Nursimaasilturk/ImageProcessing/blob/master/assets/salt-and-pepper.png)