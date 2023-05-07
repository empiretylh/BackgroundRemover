from PIL import Image
import math


class GeneratePhoto:
    def __init__(self,paper_size,gap,images,img_max_width,img_max_height):
        self.paper_size = paper_size
        self.gap = gap 
        self.images = images 
        self.img_max_width = img_max_width
        self.img_max_height =img_max_height
    
    def export(self):
        paper_size = self.paper_size
        gap = self.gap

        images = self.images
        img_max_width = self.img_max_width
        img_max_height = self.img_max_height

        #Calculate the images that how much fit inside the paper
        limited_img_xaxis = int(paper_size[0] / (img_max_width + gap))
        limited_img_yaxis = int(paper_size[1] / (img_max_height + gap))

        
        limited_paper_images =  limited_img_xaxis * limited_img_yaxis
        img_qty = 0;


        for (a,b) in images:
            img_qty += b 

        print(math.ceil(img_qty/limited_paper_images))

        print('limited image',limited_paper_images)
        print(img_qty)

        paper_qty = math.ceil(img_qty/limited_paper_images)

        sets = []  # Initialize an empty list of sets
        current_set = []  # Initialize an empty list to hold the images for the current set

        # Iterate over the images
        for image in images:
            name, count = image
            
            # Add the current image to the current set count times
            for i in range(count):
                # If adding the current image would exceed the limit, add the current set to the list of sets and start a new set
                if len(current_set) == limited_paper_images:
                    sets.append(current_set)
                    current_set = []
                current_set.append(name)

        # Add the last set to the list of sets
        if current_set:
            sets.append(current_set)
            
        # Count the duplicate image names in each set and print the sets
        count_set = []

        for i, set in enumerate(sets):
            name_counts = {}
            for name in set:
                if name in name_counts:
                    name_counts[name] += 1
                else:
                    name_counts[name] = 1
            print(f"Name counts: {name_counts}")
            count_set.append(name_counts)


        print(count_set)

        pname = 0;

        for p in count_set:
            a4_image = Image.new('RGB', paper_size, color='white')
        
            values_list = list(p.values()) 
            key_list = list(p.keys())
        

            imgs_sum = sum(values_list)
            index = 0;

            img = Image.open(key_list[index])
            #Change pictures to Thumbnail
            img.thumbnail((img_max_width,img_max_height))

            for a in range(imgs_sum):            
                x_pos = a % limited_img_xaxis
                y_pos = a // limited_img_xaxis
                print(f"({x_pos}, {y_pos})")

                position = (int(x_pos*img_max_width)+(gap*x_pos)+gap), int((y_pos*img_max_height)+(gap*y_pos)+gap) 

                print(position)
                a4_image.paste(img,position)
                
                if a == sum(values_list[:index+1])-1:
                        print("Next Image", index)
                        index += 1
                        try:
                            img = Image.open(key_list[index])
                            img.thumbnail((img_max_width,img_max_height))
                        except IndexError:
                            print(IndexError)
                    
                pname += 1 
            a4_image.save('a4_image_with_pasted_image'+str(pname)+'.png')



paper_size = (2480,3508)
gap = 50; # gap between images;

images = {('crop.jpg',6)}
img_max_width = 1.1 * 300
img_max_height = 1.3 * 300
a = GeneratePhoto(paper_size,gap,images,img_max_width,img_max_height)
a.export()