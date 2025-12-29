# filters.py
from PIL import Image
import numpy as np

def grayscale_conversion(image):
    """Convert RGB to grayscale using luminance formula"""
    img_array = np.array(image)
    
    # Luminance formula: 0.299*R + 0.587*G + 0.114*B
    gray = np.dot(img_array[...,:3], [0.299, 0.587, 0.114])
    
    return Image.fromarray(gray.astype(np.uint8))


def gaussian_blur(image):
    """Apply 3x3 Gaussian kernel for smoothing"""
    img_array = np.array(image)
    
    # 3x3 Gaussian kernel
    kernel = np.array([
        [1, 2, 1],
        [2, 4, 2],
        [1, 2, 1]
    ]) / 16.0
    
    # Apply convolution
    if len(img_array.shape) == 3:  # Color image
        blurred = np.zeros_like(img_array, dtype=np.float32)
        for channel in range(img_array.shape[2]):
            blurred[:,:,channel] = convolve2d(
                img_array[:,:,channel], kernel
            )
    else:  # Grayscale
        blurred = convolve2d(img_array, kernel)
    
    return Image.fromarray(np.clip(blurred, 0, 255).astype(np.uint8))


def convolve2d(image, kernel):
    """Helper function for 2D convolution"""
    h, w = image.shape
    kh, kw = kernel.shape
    pad_h, pad_w = kh // 2, kw // 2
    
    # Pad image
    padded = np.pad(image, ((pad_h, pad_h), (pad_w, pad_w)), mode='edge')
    output = np.zeros_like(image, dtype=np.float32)
    
    for i in range(h):
        for j in range(w):
            output[i, j] = np.sum(
                padded[i:i+kh, j:j+kw] * kernel
            )
    
    return output


def edge_detection(image):
    """Sobel filter for edge detection"""
    img_array = np.array(image.convert('L'))  # Convert to grayscale first
    
    # Sobel kernels
    sobel_x = np.array([
        [-1, 0, 1],
        [-2, 0, 2],
        [-1, 0, 1]
    ])
    
    sobel_y = np.array([
        [-1, -2, -1],
        [0,  0,  0],
        [1,  2,  1]
    ])
    
    # Apply Sobel operators
    grad_x = convolve2d(img_array.astype(np.float32), sobel_x)
    grad_y = convolve2d(img_array.astype(np.float32), sobel_y)
    
    # Compute gradient magnitude
    gradient = np.sqrt(grad_x**2 + grad_y**2)
    
    return Image.fromarray(np.clip(gradient, 0, 255).astype(np.uint8))


def image_sharpening(image):
    """Enhance edges and details"""
    img_array = np.array(image)
    
    # Sharpening kernel
    kernel = np.array([
        [0, -1, 0],
        [-1, 5, -1],
        [0, -1, 0]
    ])
    
    # Apply convolution
    if len(img_array.shape) == 3:  # Color image
        sharpened = np.zeros_like(img_array, dtype=np.float32)
        for channel in range(img_array.shape[2]):
            sharpened[:,:,channel] = convolve2d(
                img_array[:,:,channel].astype(np.float32), kernel
            )
    else:  # Grayscale
        sharpened = convolve2d(img_array.astype(np.float32), kernel)
    
    return Image.fromarray(np.clip(sharpened, 0, 255).astype(np.uint8))


def brightness_adjustment(image, factor=1.3):
    """Adjust image brightness (factor > 1 increases, < 1 decreases)"""
    img_array = np.array(image)
    
    # Multiply by factor and clip to valid range
    adjusted = img_array * factor
    
    return Image.fromarray(np.clip(adjusted, 0, 255).astype(np.uint8))


def apply_all_filters(image_path, output_dir):
    """
    Apply all 5 filters to an image and save results
    Returns: dict with processing time and success status
    """
    import time
    import os
    
    start_time = time.time()
    
    try:
        # Load image
        image = Image.open(image_path)
        basename = os.path.basename(image_path)
        name_without_ext = os.path.splitext(basename)[0]
        
        # Apply each filter and save
        filters_to_apply = [
            ('grayscale', grayscale_conversion(image)),
            ('blur', gaussian_blur(image)),
            ('edges', edge_detection(image)),
            ('sharpen', image_sharpening(image)),
            ('brightness', brightness_adjustment(image, 1.3))
        ]
        
        for filter_name, filtered_img in filters_to_apply:
            output_path = os.path.join(
                output_dir, 
                f"{name_without_ext}_{filter_name}.jpg"
            )
            filtered_img.save(output_path)
        
        duration = time.time() - start_time
        
        return {
            'image': basename,
            'duration': duration,
            'success': True
        }
        
    except Exception as e:
        return {
            'image': os.path.basename(image_path),
            'duration': time.time() - start_time,
            'success': False,
            'error': str(e)
        }
        