from PIL import Image
from gDownloadImages import *
import os
import subprocess
from time import sleep

query = 'omg meme'
folderName = 'images/'+query+'/'
stickerFolder = folderName+'sticker'
number = 3

# creating folders for each img
try:
    os.mkdir('images')
except:
    print('folder images exists')

try:
    os.mkdir(folderName)
except:
    print('folder ' + folderName + 'exists')
    # fix later
    print('program terminated')
    exit()


# downloading images
downloaded = False
# while downloaded == False:
try:
    downloadImages(query, number)
    downloaded = True
except:
    downloaded = False
    print('failed to download images')
    exit()

STICKERSIZE = 512
STICKERTHUMBNAILSIZE = 96
# imageName = str(os.listdir(folderName)[0])
imagesNames = os.listdir(folderName)
print(imagesNames)

# path = folderName

# im = Image.open(path+imageName)

# # resizing imgs and saving
# newIm = im.resize((STICKERSIZE, STICKERSIZE))
# newIm.save(path+'resized'+str(STICKERSIZE)+'_'+imageName)

# newIm = im.resize((STICKERTHUMBNAILSIZE, STICKERTHUMBNAILSIZE))
# newIm.save(path+'resized'+str(STICKERTHUMBNAILSIZE)+'_'+imageName)

# try:
#     os.mkdir(stickerFolder)
# except:
#     print('folder' + stickerFolder + 'exists')

# # transforming to sticker format
# callCommand = './stickerFormater/cwebp'

# imgInput = path+'resized'+str(STICKERSIZE)+'_'+imageName
# imgOutput = stickerFolder+'/resized'+str(STICKERSIZE)+'_'+imageName
# subprocess.call([callCommand, '-o', imgOutput, imgInput])

# imgInput = path+'resized'+str(STICKERTHUMBNAILSIZE)+'_'+imageName
# imgOutput = stickerFolder+'/resized'+str(STICKERTHUMBNAILSIZE)+'_'+imageName
# subprocess.call([callCommand, '-o', imgOutput, imgInput])
