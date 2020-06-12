from PIL import Image
from gDownloadImages import *
import os

query = 'damm meme'
folderName = 'images/'+query+'/'
number = 1

try:
    os.mkdir('images')
except:
    print('folder exists')

try:
    os.mkdir(folderName)
except:
    print('folder exists')

downloadImages(query, number)

STICKERSIZE = 512
STICKERTHUMBNAILSIZE = 96
imageName = str(os.listdir(folderName)[0])
path = folderName

im = Image.open(path+imageName)

newIm = im.resize((STICKERSIZE, STICKERSIZE))
newIm.save(path+'resized'+str(STICKERSIZE)+'_'+imageName)

newIm = im.resize((STICKERTHUMBNAILSIZE, STICKERTHUMBNAILSIZE))
newIm.save(path+'resized'+str(STICKERTHUMBNAILSIZE)+'_'+imageName)
