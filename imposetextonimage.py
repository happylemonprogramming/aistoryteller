from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import textwrap
import os

# Function to add text to an image
def imposetextonimage(text,imagepath,path,name):
    # Open the image
    image = Image.open(imagepath)

    # Create an ImageDraw object
    draw = ImageDraw.Draw(image)

    # Set the text color to white and the border color to black
    text_color = (255, 255, 255) # white
    border_color = (0, 0, 0) # black

    # Set the border thickness
    border_thickness = 3

    # Set the font and size
    size = 36

    # Confirm that directories have been set up, if not then create them
    # Check if the directory exists
    if not os.path.exists('Fonts'):
        # Create the directory
        os.makedirs('Fonts')

    # Set file paths relative to current directory
    current_dir = os.getcwd()
    font_path = os.path.join(current_dir, 'Fonts/calibri.ttf')

    font = ImageFont.truetype(font_path, size)

    # Set the text and position
    x, y = 10, 750

    # Set the width at which to wrap the text
    wrap_width = 55

    # Use the textwrap module to pre-format the text
    wrapped_text = textwrap.wrap(text, wrap_width)

    # Iterate over the lines of text
    for line in wrapped_text:
        # Draw the text with a border color
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            draw.text((x+dx*border_thickness, y+dy*border_thickness), line, font=font, fill=border_color)

        # Draw the text with a text color fill
        draw.text((x, y), line,font=font, fill=text_color)

        # Move the y-coordinate down for the next line of text
        y += size

    # Save the image
    image.save(str(path)+str(name)+'.png')