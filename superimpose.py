import cv2


def superimpose_images(big_image_path, small_image_path):
    # Load the big image and small image
    big_image = cv2.imread(big_image_path)
    small_image = cv2.imread(small_image_path)

    # Get the dimensions of the small image
    small_image_height, small_image_width, _ = small_image.shape

    # Define the margin
    margin = 10

    # Place the small image in the lower right corner of the big image with a margin
    big_image[-small_image_height-margin:-margin, -small_image_width-margin:-margin] = small_image

    # Save the result
    cv2.imwrite('superimposed_image.jpg', big_image)

if __name__ == '__main__':
    superimpose_images('isana.png', 'barcode.png')
