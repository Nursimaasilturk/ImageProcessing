import cv2
import numpy as np

def contraharmonic_mean_filter(image, window_size, Q):
    """
    image: Görüntü
    window_size: Filtre penceresi boyutu (örneğin, 3x3)
    Q: Kontraharmonik ortalama filtresinin derecesi (negatif, sıfır veya pozitif)
    """
    pad_size = window_size // 2
    height, width = image.shape

    # Görüntüyü kenar piksellerle genişletme
    padded_image = cv2.copyMakeBorder(image, pad_size, pad_size, pad_size, pad_size, cv2.BORDER_CONSTANT, value=0)

    # Filtrelenmiş görüntüyü saklamak için boş bir matris oluşturun
    filtered_image = np.zeros_like(image, dtype=np.float32)

    for i in range(pad_size, height + pad_size):
        for j in range(pad_size, width + pad_size):
            # Filtre penceresini al
            window = padded_image[i - pad_size:i + pad_size + 1, j - pad_size:j + pad_size + 1]

            # Contraharmonic Mean formülünü uygula
            numerator = np.sum(np.power(window, Q + 1))
            denominator = np.sum(np.power(window, Q))
            filtered_image[i - pad_size, j - pad_size] = numerator / max(denominator, 1e-10)  # sıfıra bölme hatasını önle

    # Görüntüyü [0, 255] aralığına getir
    filtered_image = np.clip(filtered_image, 0, 255).astype(np.uint8)

    return filtered_image

# Örnek olarak bir görüntüyü yükle
image_path = 'old-image.jpg'
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Contraharmonic Mean filtresini uygula
filtered_image = contraharmonic_mean_filter(image, window_size=3, Q=1.5)

# Sonuçları görselleştir
cv2.imshow('Original Image', image)
cv2.imshow('Contraharmonic Mean Filter Result', filtered_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
