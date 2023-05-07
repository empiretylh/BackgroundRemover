from PaperLayout import GeneratePhoto
from RemoveBackground import RemoveBackground


images = {('img.jpg',6),('img2.jpg',10),('img3.jpg',12)}
aspect_ratio = 1.1 / 1.3
bg_rgb = (255,0,0)
output_di = 'img/'
a = RemoveBackground(images,aspect_ratio,bg_rgb,output_di)
a.remove()

print('Finished........................... Removing')

paper_size = (2480,3508)
gap = 50; # gap between images;

img_max_width = 1.1 * 300
img_max_height = 1.3 * 300
a = GeneratePhoto(paper_size,gap,images,img_max_width,img_max_height,raw_export=output_di)

a.export()