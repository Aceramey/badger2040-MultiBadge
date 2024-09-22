#import launcher #uncomment to use launcher instead
import badger2040
import jpegdec

display=badger2040.Badger2040()
jpeg = jpegdec.JPEG(display.display)

#format: text1, text2, text1-x, text1-y, text2-x, text2-y, line1fontsize, line2fontsize, imagepath, is there extra text?? (just doesn't do display.update() so it can be done in the button() function
def draw(line1, line2, line1x, line1y, line2x, line2y, line1size, line2size, image, extra):
    display.set_pen(15)
    display.clear()
    display.set_pen(0)
    jpeg.open_file(image)
    jpeg.decode(200, 0)
    display.line(0, 65, 200, 65)
    display.set_font("bitmap8") #only not bad font on the badger
    display.text(line1, line1x, line1y, -1, line1size)
    display.text(line2, line2x, line2y, -1, line2size)
    if extra == False:
        display.update()

#this one draws on boot (when you plug it in)
draw("Toni Rigatoni", "Cat Enthusiast", 5, 40, 5, 75, 3, 2, "/cat.jpg", True)
display.text("My cat --->", 110, 120, -1, 1)
display.update()

def button(pin):
    if pin == badger2040.BUTTON_A: #this one has extra text line, can also have more than 1, or whatever else you want, just dont forget display.update()
        draw("Toni Rigatoni", "Cat Enthusiast", 5, 40, 5, 75, 3, 2, "/cat.jpg", True)
        display.text("My cat Gracie --->", 110, 120, -1, 1)
        display.update()
    elif pin == badger2040.BUTTON_B: #this one is the basic one, that only uses the function and nothing extra
        draw("Toni Rigatoni", "Shark Enthusiast", 5, 40, 5, 75, 3, 2, "/shark.jpg", True)
    elif pin == badger2040.BUTTON_C:
        #button C
    elif pin == badger2040.BUTTON_UP:
        #button UP
    elif pin == badger2040.BUTTON_DOWN:
        #button DOWN
    elif pin == 69420: # A+B
        #custom (button combos)
            
while True:
    display.keepalive()
    #keep key combos above the rest, or else it will end up meeting another if statement first and ignore the combo
    if display.pressed(badger2040.BUTTON_A) and display.pressed(badger2040.BUTTON_B):
        button(69420) #can be whatever number you want, just make sure it matches in the button() function
    elif display.pressed(badger2040.BUTTON_A):
        button(badger2040.BUTTON_A)
    elif display.pressed(badger2040.BUTTON_B):
        button(badger2040.BUTTON_B)
    elif display.pressed(badger2040.BUTTON_C):
        button(badger2040.BUTTON_C)
    elif display.pressed(badger2040.BUTTON_UP):
        button(badger2040.BUTTON_UP)
    elif display.pressed(badger2040.BUTTON_DOWN):
        button(badger2040.BUTTON_DOWN)

