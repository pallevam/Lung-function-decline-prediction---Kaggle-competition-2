import pydicom as dicom
import os, cv2, glob


# there is a second method which is for .png files as jpegs are created by using lossy
# and pngs by lossless compression, advisable to use png for better picture quality
def dcm_to_jpg(filepath, jpgpath):
    PNG = False
    images_path = os.listdir(filepath)
    for n, image in enumerate(images_path):
        ds = dicom.dcmread(os.path.join(filepath, image))
        pixel_array_numpy = ds.pixel_array
        if PNG == False:
            image = image.replace('.dcm', '.jpg')
        else:
            image = image.replace('.dcm', '.png')
        cv2.imwrite(os.path.join(jpgpath, image), pixel_array_numpy)
        if n % 50 == 0:
            print('{} image converted'.format(n))


# working but have to convert again from .png to .jpg

def dcm_to_png(inputdir, outputdir):
    test_list = [os.path.basename(x) for x in glob.glob(inputdir + '*.dcm')]

    for f in test_list:
        ds = dicom.read_file(inputdir + f) # read dcom image
        img = ds.pixel_array # get pixel array
        cv2.imwrite(outputdir + f.replace('.dcm', '.png'), img) # writing png image

