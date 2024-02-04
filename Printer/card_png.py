from PIL import Image
import os
import math
import comtypes.client
from data_forge.file_handlers.file_handler import FileHandler

def pptx_to_png():
    powerpoint = comtypes.client.CreateObject("Powerpoint.Application")
    

    abs_project_path = FileHandler.gen_project_abs_path()
    pptx_path = abs_project_path + FileHandler.gen_slide_output_directory()
    pptx_path = pptx_path.replace("/", "\\")
    presentation = powerpoint.Presentations.Open(pptx_path)

    output_folder = abs_project_path + FileHandler.gen_slide_img_output_directory("Joined")
    output_folder = output_folder.replace("/", "\\")
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    presentation.SaveAs(output_folder, 17)  # 17 is the enum for PNG format
    presentation.Close()
    powerpoint.Quit()
    print(output_folder)

def count_files(source_dir):
    totalFilesNumber = 0
    for root_dir, cur_dir, files in os.walk(source_dir):
        totalFilesNumber += len(files)
    return totalFilesNumber

def paint_corners(source_dir):
    totalFilesNumber = count_files(source_dir)
    currentFileNumber = 0

    for dirpath, dirnames, filenames in os.walk(source_dir):
        for filename in filenames:
            if filename.endswith('.png') or filename.endswith('.JPG'):
                currentFileNumber += 1
                print(f"Painting {filename}, {currentFileNumber}/{totalFilesNumber}.")

                # Opens a image in RGB mode
                filepath = os.path.join(dirpath, filename)
                im = Image.open(filepath)
                
                # Size of the image in pixels (size of original image)
                # (This is not mandatory)
                width, height = im.size

                # Determine the width of the card side-border
                y = height/2
                corner_color_value = None
                for x in range (0,width):
                    current_color = im.getpixel( (x,y) )

                    if corner_color_value is None:
                        print(f"    Determined card side color value to be {current_color}")
                        corner_color_value = current_color

                    if current_color != corner_color_value:
                        #print(f"    Comparing current_color: {current_color} with corner_color_value: {corner_color_value}")
                        if math.fsum(current_color) - math.fsum(corner_color_value) < 50:
                            corner_color_value = current_color
                        else:
                            print(f"    Found top-edge at ({x},{y}) with color {current_color}")
                            card_side_border = x
                            break

                # Determine the width of the card side-border
                x = width/4
                corner_color_value = None
                for y in range (0,height):
                    current_color = im.getpixel( (x,y) )
                    if corner_color_value is None:
                        print(f"    Determined card top color value to be {current_color}")
                        corner_color_value = current_color

                    if current_color != corner_color_value:
                        #print(f"    Comparing current_color: {current_color} with corner_color_value: {corner_color_value}")
                        if math.fsum(current_color) - math.fsum(corner_color_value) < 50:
                            corner_color_value = current_color
                        else:
                            print(f"    Found side-edge at ({x},{y}) with color {current_color}")
                            card_top_border = y
                            break
                
                corner_color_value = (0,0,0)

                # Color top
                middle = int(card_top_border/2)
                for x in range(0,width):
                    if im.getpixel( (x,middle) ) :
                        pass # Something was supposed to happen here?

                    for y in range(0,card_top_border):
                        im.putpixel( (x,y), corner_color_value)

                # Color bottom
                for x in range(0,width):
                    for y in range(height-card_top_border,height):
                        im.putpixel( (x,y), corner_color_value)

                # Color left
                for x in range(0,card_side_border):
                    for y in range(0,height):
                        im.putpixel( (x,y), corner_color_value)
                
                # Color right
                for x in range(width-card_side_border,width):
                    for y in range(0,height):
                        im.putpixel( (x,y), corner_color_value)

                # Color middle
                for x in range(int(width/2)-card_side_border,int(width/2)+card_side_border):
                    for y in range(0,height):
                        im.putpixel( (x,y), corner_color_value)

                # Saves the image in image viewer
                im.save(filepath)
                im.close()


def crop_cards(source_dir):
    totalFilesNumber = count_files(source_dir)
    currentFileNumber = 0

    for dirpath, dirnames, filenames in os.walk(source_dir):
        for filename in filenames:
            if filename.endswith('.png') or filename.endswith('.JPG'):
                currentFileNumber += 1
                print(f"Cropping {filename}, {currentFileNumber}/{totalFilesNumber}.")
                filepath = os.path.join(dirpath, filename)
                im = Image.open(filepath)
                
                                # Size of the image in pixels (size of original image)
                # (This is not mandatory)
                width, height = im.size

                # Determine left
                print(f"   Cropping left of {filename}.")
                left = 0
                y = int(height/2)
                for x in range (0,width):
                    temp_result = find_crop_direction(im, x, y, True)
                    
                    if temp_result is not None:
                        left = temp_result
                        break
                
                # Determine right
                print(f"   Cropping right of {filename}.")
                right = width-1
                for x in range(width-1, 0, -1):
                    temp_result = find_crop_direction(im, x, y, True)
                    
                    if temp_result is not None:
                        right = temp_result
                        break

                # Determine top
                print(f"   Cropping top of {filename}.")
                top = 0
                x = int(width/4)
                for y in range (0,height):
                    temp_result = find_crop_direction(im, x, y, False)
                    
                    if temp_result is not None:
                        top = temp_result
                        break

                # Determine bottom
                print(f"   Cropping bottom of {filename}.")
                bottom = height-1
                for y in range (height-1, 0, -1):
                    temp_result = find_crop_direction(im, x, y, False)
                    
                    if temp_result is not None:
                        bottom = temp_result
                        break

                cropped = im.crop((left, top, right, bottom))
                cropped.save(filepath)
    

def check_color(color : (int, int, int)):
    color_list = [x for x in color]
     
    # Find the sum of the elements in the list using the built-in sum() function
    color_sum = sum(color_list)

    return color_sum > 500

def find_crop_direction(im, x : int, y : int, is_x : bool):
    result = None
    color = im.getpixel( (x,y) )

    if not check_color(color):
        result = x if is_x else y
    else:
        print(f"color {color} is not enough.")
    
    return result
    

def make_cards():
    pptx_to_png()
    crop_cards('Outputs\Images\Joined\cardCreator-test')
    paint_corners('Outputs\Images\Joined\cardCreator-test')
