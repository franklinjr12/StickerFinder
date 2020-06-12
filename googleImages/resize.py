
def resizeImage(path, imageName, w, h):

    from PIL import Image

    im = Image.open(path+imageName)
    newIm = im.resize((w, h))
    newIm.save(path+'resized_'+imageName)

    # with open(imageName, 'r+b') as f:
    #     with Image.open(f) as image:
    #         cover = resizeimage.resize_cover(image, [w, h])
    #         cover.save(imageName+'Resized', image.format)
