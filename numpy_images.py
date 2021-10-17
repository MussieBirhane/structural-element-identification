
import numpy as np
from PIL import Image

img_arrays = np.load('task2_X_test.npy', allow_pickle=False)
print(type(img_arrays), img_arrays.shape, img_arrays.size)
filename = 0
for img_array in img_arrays:
    img = Image.fromarray(img_array.astype(np.uint8))
    filename += 1
    img_name = "Images/" + str(filename) + ".png"
    img.save(img_name)
    # img.show()

print("Conversion completed.")