import scipy
import os
import numpy as np
#added by Meg
import imageio

def loadimage(filename):
    #changed by Meg
    #img = scipy.misc.imread(filename).astype(np.float)
    img = imageio.imread(filename).astype(np.float)
    return img

def loadimage_gray(filename):
    #chnaged by Meg
    #img = scipy.misc.imread(filename, mode='L').astype(np.float)[:,:,np.newaxis]
    img = imageio.imread(filename, mode='L').astype(np.float)[:,:,np.newaxis]
    return img

def saveimages(outimages, prefix='samples', filenames=None, outdir='out'):
    numimages = len(outimages)
    print("Array shape {}".format(outimages.shape))

    if not os.path.exists(outdir):
        os.mkdir(outdir)

    for i in range(numimages):
        if filenames is None:
            filename = '{}_{}.png'.format(prefix, i)
        else:
            filename = '{}_{}'.format(prefix, os.path.basename(filenames[i]))
        filename = os.path.join(outdir, filename)
        scipy.misc.imsave(filename, np.squeeze(outimages[i, :, :, :]))


