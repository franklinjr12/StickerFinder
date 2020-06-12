from PIL import Image
from gDownloadImages import *
import os

query = 'wow meme'
number = 1

downloadImages(query, number)

STICKERSIZE = 512
STICKERTHUMBNAILSIZE = 96
imageName = str(os.listdir('images')[0])
path = 'images/'

im = Image.open(path+imageName)

newIm = im.resize((STICKERSIZE, STICKERSIZE))
newIm.save(path+'resized'+str(STICKERSIZE)+'_'+imageName)

newIm = im.resize((STICKERTHUMBNAILSIZE, STICKERTHUMBNAILSIZE))
newIm.save(path+'resized'+str(STICKERTHUMBNAILSIZE)+'_'+imageName)

# resizeImage('images/', imName, STICKERSIZE, STICKERSIZE)
# resizeImage('images/', imName, STICKERTHUMBNAILSIZE, STICKERTHUMBNAILSIZE)
