import tensorflow as tf
import scipy.misc
import argparse
import os
import numpy as np
from glob import glob
from helper import loadimage, saveimages

from model_quantize import ModelQuantize

parser = argparse.ArgumentParser()
parser.add_argument('--model_file', type=str, help="Pretrained GAN model")
parser.add_argument('--lr', type=float, default=0.0001)
parser.add_argument('--momentum', type=float, default=0.9)
parser.add_argument('--nIter', type=int, default=1000)
parser.add_argument('--imgSize', type=int, default=64)
parser.add_argument('--batch_size', type=int, default=64)
parser.add_argument('--lambda_p', type=float, default=0.001)
parser.add_argument('--checkpointDir', type=str, default='checkpoint')
parser.add_argument('--outDir', type=str, default='quantize')
parser.add_argument('--blend', action='store_true', default=False,
                    help="Blend predicted image to original image")
parser.add_argument('--in_image', type=str, default=None,
                    help='Input Image (ignored if inDir is specified')
parser.add_argument('--inDir', type=str, default=None,
                    help='Path to input images')
parser.add_argument('--imgExt', type=str, default='png',
                    help='input images file extension')
parser.add_argument('-c', action='store_true', help='corrupt image on the fly')

args = parser.parse_args()


def corrupt_image(img, quantize_factor=4):
    img /= 255.0
    img *= (255.0 / quantize_factor)
    images = img
    images = np.floor(images)
    images /= (255.0 / quantize_factor)
    images *= 255.0
    images = images.astype(int)
    return images

def main():
    m = ModelQuantize(args.model_file, args)
    dd = 50
    m.quantize_factor = dd
    #m.levels = 4

    # Generate some samples from the model as a test
    #imout = m.sample()
    #saveimages(imout)

    if args.inDir is not None:
        imgfilenames = glob( args.inDir + '/*.' + args.imgExt )
        print('{} images found'.format(len(imgfilenames)))
        in_img = np.array([loadimage(f) for f in imgfilenames])
        if args.c:
            in_corrupt_img = np.array([corrupt_image(loadimage(f), dd) for f in imgfilenames])
        else:
            in_corrupt_img = np.copy(in_img)

    elif args.in_image is not None:
        in_img = in_corrupt_img #loadimage(args.in_image)
    else:
        print('Input image needs to be specified')
        exit(1)
    #saveimages(in_corrupt_img, prefix='input')
    inpaint_out, g_out = m.restore_image(in_img)
    saveimages(g_out, 'quantize_gen', imgfilenames, args.outDir)
    saveimages(inpaint_out, 'quantize', imgfilenames, args.outDir)


if __name__ == '__main__':
    main()
