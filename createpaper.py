from PIL import Image

# Define A4 size in pixels (300 dpi)
a4_size = (1749, 2481)

# Create a new A4-sized image
a4_image = Image.new('RGB', a4_size, color='white')

# Load the image to be pasted
image_to_paste = Image.open('crop.jpg')

s_position = (0,0)  # (x, y) in pixels
gap_between_images = 50  # gap between each pasted image in pixels

# Resize the pasted image to fit within the A4 paper
max_width = 1.1 * 300  # 1.1 inch in pixels (300 dpi)
max_height = 1.3 * 300  # 1.3 inch in pixels (300 dpi)
image_to_paste.thumbnail((max_width, max_height))


pagerange = int(a4_size[0] / (max_width + gap_between_images))

# Paste the image onto the A4 paper 6 times
for i in range(5):
   for j in range(pagerange):
        position = (int(s_position[0] + (j*max_width)+(50*j)+50),int(s_position[1]+ (i*max_height)+(50*i) + 50))
        print(position)
#    position = (int(s_position[0] + (i*max_width)+(50*i)+50),int(s_position[1]+50))
#    position = (2480,int(s_position[1]+50))
 
        a4_image.paste(image_to_paste, position)


# Save the image as a PNG file
a4_image.save('a4_image_with_pasted_image.png')
