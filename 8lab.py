from PIL import Image, ImageFont, ImageDraw

def z1():
    f = "1.jpg"

    with Image.open(f) as img:
        img.load()

    img.show()
    obrez_img = img.crop((220, 50, 480, 220))
    obrez_img.show()

    obrez_img.save("obot.jpg")

def z2():
    lib = {1: "1.jpg", 2: "2.jpg", 3: "3.jpg", 4: "4.jpg"}

    print("1 - день картошки,", "2 - день яблока,", "3 - день микроволновки,", "4 - день мыши,", end='\n')
    quest = int(input("Какую открытку вы хотите получить?: "))

    f = lib[quest]
    with Image.open(f) as img:
        img.load()
    img.show()

def z3():
    name = input("Введите имя получателя: ")
    f = "2.jpg"

    with Image.open(f) as img:
        img.load()

    font = ImageFont.truetype("MultiroundPro.otf", 18)
    write_name = ImageDraw.Draw(img)

    write_name.text((img.width // 2 - 50, img.height - 30), name + ", поздравляю!", fill = ('red'), font = font, stroke_width = 1)

    img.show()
    img.save("otname.png")