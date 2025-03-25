import numpy as np
from PIL import Image

def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9

f_temps = np.array([32, 68, 100, 212, 77])
vectorized_f_to_c = np.vectorize(fahrenheit_to_celsius)
c_temps = vectorized_f_to_c(f_temps)
print("Celsius temperatures:", c_temps)

def power_function(base, exponent):
    return base ** exponent

bases = np.array([2, 3, 4, 5])
exponents = np.array([1, 2, 3, 4])
vectorized_power = np.vectorize(power_function)
power_results = vectorized_power(bases, exponents)
print("Power results:", power_results)

A = np.array([[4, 5, 6], [3, -1, 1], [2, 1, -2]])
B = np.array([7, 4, 5])
solution = np.linalg.solve(A, B)
print("Solution for x, y, z:", solution)

A_circuit = np.array([[10, -2, 3], [-2, 8, -1], [3, -1, 6]])
B_circuit = np.array([12, -5, 15])
currents = np.linalg.solve(A_circuit, B_circuit)
print("Currents I1, I2, I3:", currents)

def process_image(image_path, output_path):
    img = Image.open(image_path)
    img_array = np.array(img, dtype=np.uint8)
    flipped_horizontally = np.fliplr(img_array)
    flipped_vertically = np.flipud(flipped_horizontally)
    
    noise = np.random.randint(0, 50, img_array.shape, dtype=np.uint8)
    noisy_image = np.clip(flipped_vertically + noise, 0, 255)
    
    brightened_image = noisy_image.copy()
    brightened_image[:, :, 0] = np.clip(brightened_image[:, :, 0] + 40, 0, 255)
    h, w, _ = brightened_image.shape
    x_start, y_start = w//2 - 50, h//2 - 50
    brightened_image[y_start:y_start+100, x_start:x_start+100] = [0, 0, 0]
    
    processed_img = Image.fromarray(brightened_image)
    processed_img.save(output_path)

process_image("images/birds.jpg", "images/processed_birds.jpg")
print("Image processing completed and saved.")
