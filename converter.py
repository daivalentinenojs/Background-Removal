from PIL import Image

def run_visualization():
    for i in range(1, 202600):
        name = ""
        
        if i < 10:
            name += "00000"
            name += str(i)
        elif i < 100:
            name += "0000"
            name+= str(i)
        elif i < 1000:
            name += "000"
            name+= str(i)
        elif i < 10000:
            name += "00"
            name+= str(i)
        elif i < 100000:
            name += "0"
            name+= str(i)
        else:
            name = str(i)
        
        print('Processing = '+name+'.jpg')
        fill_color = 'white'  # your background
        image = Image.open('E:/Daiva/Research/18. Sketch GAN/1. Background Removal/celeba_sketch_xception/'+name+'.png')
        if image.mode in ('RGBA', 'LA'):
            background = Image.new(image.mode[:-1], image.size, fill_color)
            background.paste(image, image.split()[-1])
            image = background
        image.save('E:/Daiva/Research/Dataset/CelebA_Removal_JPG/'+name+'.jpg', quality=95)

        # im1 = Image.open('E:/Daiva/Research/18. Sketch GAN/1. Background Removal/celeba_sketch_xception/'+name+'.png')
        # im1.save('E:/Daiva/Research/18. Sketch GAN/1. Background Removal/celeba_jpg/'+name+'.jpg')
        # print('Done')

run_visualization()