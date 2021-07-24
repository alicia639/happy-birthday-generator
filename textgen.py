import PIL, random, sys
from PIL import Image, ImageDraw

width = 35
height = 17

r = lambda: random.randint(50,255)
rc = lambda: ('#%02X%02X%02X' % (r(),r(),r()))
color = [(8,2), (8,3), (8, 4), (8, 5), (8,6), (8,7),
         (9, 5),
         (10,2), (10,3), (10, 4), (10, 5), (10,6), (10,7),
         (12,3), (12, 4), (12, 5), (12,6), (12,7),
         (13, 2), (13,5),
         (14,3), (14, 4), (14, 5), (14,6), (14,7),
         (16,2), (16,3), (16, 4), (16, 5), (16,6), (16,7),
         (17,2), (17,5),
         (18,3), (18, 4),
         (20,2), (20,3), (20, 4), (20, 5), (20,6), (20,7),
         (21,2), (21,5),
         (22,3), (22, 4),
         (24,2), (24,3), (24, 4), (24,7),
         (25, 5), (25,7),
         (26,2), (26,3), (26, 4), (26, 5), (26,6),
         (2,9), (2,10), (2, 11), (2, 12), (2,13), (2,14),
         (3,9), (3,12), (3,14),
         (4,10), (4,11), (4,13),
         (6,9), (6,10), (6, 11), (6, 12), (6,13), (6,14),
         (8,9), (8,10), (8, 11), (8, 12), (8,13), (8,14),
         (9,9), (9,12),
         (10,10), (10,11), (10,13), (10,14),
         (12,9),
         (13,9), (13,10), (13, 11), (13, 12), (13,13), (13,14),
         (14,9),
         (16,9), (16,10), (16, 11), (16, 12), (16,13), (16,14),
         (17,12),
         (18,9), (18,10), (18, 11), (18, 12), (18,13), (18,14),
         (20,9), (20,10), (20, 11), (20, 12), (20,13), (20,14),
         (21,9), (21,14),
         (22,10), (22, 11), (22, 12), (22,13),
         (24,10), (24, 11), (24, 12), (24,13), (24,14),
         (25,9), (25, 12),
         (26,10), (26, 11), (26, 12), (26,13), (26,14),
         (28,9), (28,10), (28, 11), (28,14),
         (29,12), (29, 14),
         (30,9), (30,10), (30, 11), (30,12),
         (32,9), (32,10), (32, 11), (32, 12), (32,14)
        ]

def create_square(border, draw, color):
    draw.rectangle(border, color)

def write_text(border, draw):
  x0, y0, x1, y1 = border
  widthSize = (x1-x0)/width
  heightSize = (y1-y0)/height

  for x in range(0, width):
    for y in range(0, height):
      topLeftX = x*widthSize + x0
      topLeftY = y*heightSize + y0
      botRightX = topLeftX + widthSize
      botRightY = topLeftY + heightSize

      if (x, y) in color:
        create_square((topLeftX, topLeftY, botRightX, botRightY), draw, rc())
      else:
        create_square((topLeftX, topLeftY, botRightX, botRightY), draw, (0,0,0))


def main(row, col, imgWidth):
    origDimension = imgWidth

    invaderWidth = origDimension/row
    invaderHeight = invaderWidth*height/width

    origImage = Image.new('RGB', (origDimension, int(invaderHeight*col)))
    draw = ImageDraw.Draw(origImage)

    for x in range(0, row):
        for y in range(0, col):
            topLeftX = x*invaderWidth
            topLeftY = y*invaderHeight
            botRightX = topLeftX + invaderWidth
            botRightY = topLeftY + invaderHeight

            write_text((topLeftX, topLeftY, botRightX, botRightY), draw)


    origImage.save("Examples/Example-"+str(row)+"x"+str(col)+"-"+str(imgWidth)+".jpg")

if __name__ == "__main__":
    main(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))
