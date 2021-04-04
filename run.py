# Python wind effect
import PIL
from PIL import Image, ImageEnhance
import random

percentages = []


def handlePercentage(percentage):
    """
    This function handles displaying of percentages
    """
    if percentage in percentages:
        pass
    else:
        print(f"{percentage}%")

    percentages.append(percentage)

def generate(imageObject, width, height, split_chance, splitIntensity, splitThreshold):
    img = Image.new('RGB', (width, height), "black")  # create a new empty black image
    pixels = img.load()
    for row in range(height):

        handlePercentage(int((row/height)*100))

        # The chances of a pixel being "torn"
        if random.random() <= split_chance:

            # Split this row and the according threshold
            for j in range(width):

                # Calculate which pixel to use
                # Deal with each row according to the threshold
                for k in range(1):
                    for z in range(splitThreshold):
                        pixelToUse = splitIntensity + j
                        if pixelToUse > width:
                            pixelToUse = int(width / ( pixelToUse / width ))
                        Ur, Ug, Ub = imageObject.getpixel((pixelToUse-1, row))

                        if k == 0:
                            # Paint onto black image
                            pixels[j,row-z] = (Ur,Ug,Ub)

                        elif k == 1:
                            # Paint onto black image
                            pixels[j,row+z] = (Ur,Ug,Ub)

        else:
            for j in range(width):
                r, g, b = imageObject.getpixel((j, row))

                # Paint onto black image
                pixels[j,row] = (r,g,b)


    saveOrShow = input("Do you want to save the new image? y/n")
    if saveOrShow.lower() == "y":
        # Handles saving
        fileSaveTo = input("Save directory: ")
        img.save(fileSaveTo)

    else:
        pass

    img.show()



# Import image
def importImage(image_path, split_chance, splitIntensity, splitThreshold):
    imageObject = Image.open(image_path)
    width, height = imageObject.size
    rgb_im = imageObject.convert('RGB')
    generate(rgb_im, width, height, split_chance, splitIntensity, splitThreshold)

# Handle menu
def menu():
    file_path = input("File path: ")
    split_chance = float(input("Split chance (0.0 - 1.0): "))
    splitIntensity = int(input("Split intensity: "))
    splitThreshold = int(input("Split threshold: "))

    importImage(file_path, split_chance, splitIntensity, splitThreshold)

menu()
