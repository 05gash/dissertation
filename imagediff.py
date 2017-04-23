from PIL import Image, ImageChops, ImageDraw
import sys
point_table = ([0] + ([255] * 255))

def new_gray(size, color):
    img = Image.new('L',size)
    dr = ImageDraw.Draw(img)
    dr.rectangle((0,0) + size, color)
    return img

def black_or_b(a, b, opacity=0.85):
    diff = ImageChops.difference(a, b)
    diff = diff.convert('L')
    # Hack: there is no threshold in PILL,
    # so we add the difference with itself to do
    # a poor man's thresholding of the mask: 
    #(the values for equal pixels-  0 - don't add up)
    thresholded_diff = diff
    for repeat in range(3):
        thresholded_diff  = ImageChops.add(thresholded_diff, thresholded_diff)
    h,w = size = diff.size
    mask = new_gray(size, int(255 * (opacity)))
    shade = new_gray(size, 0)
    new = a.copy()
    new.paste(shade, mask=mask)
    # To have the original image show partially
    # on the final result, simply put "diff" instead of thresholded_diff bellow
    new.paste(b, mask=thresholded_diff)
    return thresholded_diff 


a = Image.open(sys.argv[1])
b = Image.open(sys.argv[2])
c = black_or_b(a, b)
c.save(sys.argv[3])
