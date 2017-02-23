from PIL import Image, ImageDraw
from numpy import array

maxLenSimb = 10
maxLenPX = 19*maxLenSimb

def encode(encStrLst):
    maxLnght = 0
    yWrap = 0
    for elem in encStrLst:
        if len(elem) > maxLnght:
            maxLnght = len(elem)

    img = Image.new('RGB', (maxLnght*19, len(rows)*28), (253, 246, 230))
    draw = ImageDraw.Draw(img)

    for row in rows:
        xWrap = 0
        for letter in row:
            ltr = array(Image.open('daedric/letters/%s.jpg' % letter))
            for i in range(len(ltr)):
                for j in range(len(ltr[i])):
                    px0 = ltr[i][j][0]
                    px1 = ltr[i][j][1]
                    px2 = ltr[i][j][2]
                    draw.point((xWrap + j, yWrap + i), (px0, px1, px2)) # Add wrap
            xWrap += 19
        yWrap += 28
    #img.show()
    img.save('daedric/res.jpg', 'JPEG')

def lenght(fragment, maxLenSimb):
    new = ''
    while len(new) <= maxLenSimb:
        if len(fragment) != 0:
            new += fragment[0] + ' '
            fragment.pop(0)
        else:
            return (fragment, new)
    return (fragment, new)

while 1:
    # Split to words
    encStr = [x for x in str(input('>>')).split(' ')]
    rows = []
    # Fill rows with words without overflow
    while encStr != []:
        encStr, row = lenght(encStr, maxLenSimb)
        rows.append(row)
    encode(rows)