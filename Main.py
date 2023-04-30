from PIL import Image, ImageFilter
import os


def menu():
    print(
        """\n          M E N U
_____________________________
Choice    --->       Function
--------  --->      ----------
1         --->     To modify only one file
_______________________________________________
2         --->     To modify more than one file
_______________________________________________
3         --->     Exit"""
    )


def menu2():
    print(
        """\n          M E N U
_____________________________
Choice    --->       Function
--------  --->      ----------
1         --->     To resize the images
__________________________________________________________________
2         --->     To reduce the images
__________________________________________________________________
3         --->     To rotate the images
__________________________________________________________________
4         --->     To the change images to grayscale
____________________________________________________________
5         --->     To change resolution of the images
__________________________________________________________________
6         --->     To blur the images
__________________________________________________________________
7         --->     To sharpen all the images
__________________________________________________________________
8         --->     To smooth all the images
__________________________________________________________________
9         --->     Exit"""
    )


def resize(x):#definign resize funtion
    while True:
        fin = Image.open(x)
        print(f"\nThe Current image size is: {fin.size}")
        width = int(input("\nEnter the new width of the file"))
        height = int(input("\nEnter the new height of the file"))
        resized = fin.resize((width, height))
        resized.show()
        still = input("\nDo you want to save the file? (Y/N): ").lower().strip()
        if still == "Yes" or still == "y":
            name = input("\nEnter the name of resized file: ")
            resized.save(f"{name}.jpg")
            break
        else:
            retest = input("\nDo you make changes again? (y/n): ").lower().strip()
            if retest == "yes" or retest == "y":
                continue
            else:
                break


def reduce(x):#definign reduce funtion
    while True:
        fin = Image.open(x)
        print(f"\nThe Current image size is: {fin.size}")
        size = int(
            input("\nEnter number by which you want file size to be reduced to: ")
        )
        reduced = fin.reduce(size)
        reduced.show()
        still = input("\nDo you want to save the file? (Y/N): ").lower().strip()
        if still == "Yes" or still == "y":
            name = input("\nEnter the name of resized file: ")
            reduced.save(f"{name}.jpg")
            break
        else:
            retest = input("\nDo you make changes again? (y/n): ").lower().strip()
            if retest == "yes" or retest == "y":
                continue
            else:
                break


def rotated(x):#definign rotate funtion
    while True:
        fin = Image.open(x)
        angle = int(
            input(
                "\nEnter the angle in degrees by which you want the image to be rotated by: "
            )
        )
        rotated = fin.rotate(angle, expand=True)
        rotated.show()
        still = input("\nDo you want to save the file? (Y/N): ").lower().strip()
        if still == "Yes" or still == "y":
            name = input("\nEnter the name of resized file: ")
            rotated.save(f"{name}.jpg")
            break
        else:
            retest = input("\nDo you make changes again? (y/n): ").lower().strip()
            if retest == "yes" or retest == "y":
                continue
            else:
                break


def grayscale(x):#definign grayscale funtion
    while True:
        fin = Image.open(x)
        changed = fin.convert("L")
        changed.show()
        still = input("\nDo you want to save the file? (Y/N): ").lower().strip()
        if still == "Yes" or still == "y":
            name = input("\nEnter the name of resized file: ")
            changed.save(f"{name}.jpg")
            break
        else:
            break


def resolution(x):#definign resolution funtion
    while True:
        fin = Image.open(x)
        print(f"\nThe Current image size is: {fin.size}")
        width = int(input("\nEnter the new x of the file"))
        height = int(input("\nEnter the new y of the file"))
        fin.thumbnail((width, height))
        fin.show()
        still = input("\nDo you want to save the file? (Y/N): ").lower().strip()
        if still == "Yes" or still == "y":
            name = input("\nEnter the name of resized file: ")
            fin.save(f"{name}.jpg")
            break
        else:
            retest = input("\nDo you make changes again? (y/n): ").lower().strip()
            if retest == "yes" or retest == "y":
                continue
            else:
                break


def bluring(x):#definign blur funtion
    while True:
        fin = Image.open(x)
        intensity = int(input("\nEnter the level of blurness of the file"))
        blured = fin.filter(ImageFilter.BoxBlur(intensity))
        blured.show()
        still = input("\nDo you want to save the file? (Y/N): ").lower().strip()
        if still == "Yes" or still == "y":
            name = input("\nEnter the name of resized file: ")
            blured.save(f"{name}.jpg")
            break
        else:
            retest = input("\nDo you make changes again? (y/n): ").lower().strip()
            if retest == "yes" or retest == "y":
                continue
            else:
                break


def sharpening(x):#definign sharpening funtion
    while True:
        fin = Image.open(x)
        sharpened = fin.filter(ImageFilter.SHARPEN)
        sharpened.show()
        still = input("\nDo you want to save the file? (Y/N): ").lower().strip()
        if still == "Yes" or still == "y":
            name = input("\nEnter the name of resized file: ")
            sharpened.save(f"{name}.jpg")
            break
        else:
            break


def smooth(x):#definign smooth funtion
    while True:
        fin = Image.open(x)
        smoothed = fin.filter(ImageFilter.SMOOTH)
        smoothed.show()
        still = input("\nDo you want to save the file? (Y/N): ").lower().strip()
        if still == "Yes" or still == "y":
            name = input("\nEnter the name of resized file: ")
            smoothed.save(f"{name}.jpg")
            break
        else:
            break


def mass():#definign funtion to access all contents of a folder 
    x = input("Enter the folder's directory in which files are contained: ").strip()
    os.chdir(x)
    l = os.listdir()
    return l

#main
try:
    repeat2 = "y"
    while repeat2=="yes" or repeat2=="y":
        menu()
        choice = int(input("\nEnter choice: "))
        if choice == 1:
            repeat = "y"
            while repeat2 == "yes" or repeat2 == "y":
                menu2()
                choice2 = int(input("\nEnter choice: "))
                

                if choice2 == 1:
                    name = input("\nEnter the directory of the image: ")
                    resize(name)
                elif choice2 == 2:
                    name = input("\nEnter the directory of the image: ")
                    reduce(name)
                elif choice2 == 3:
                    name = input("\nEnter the directory of the image: ")
                    rotated(name)
                elif choice2 == 4:
                    name = input("\nEnter the directory of the image: ")
                    grayscale(name)
                elif choice2 == 5:
                    name = input("\nEnter the directory of the image: ")
                    resolution(name)
                elif choice2 == 6:
                    name = input("\nEnter the directory of the image: ")
                    bluring(name)
                elif choice2 == 7:
                    name = input("\nEnter the directory of the image: ")
                    sharpening(name)
                elif choice2 == 8:
                    name = input("\nEnter the directory of the image: ")
                    smooth(name)
                elif choice2 == 9:
                    exit()
                else:
                    print("\nEnter a valid choice!!!! ")
                    continue
                repeat = input(("\nDo you want to continue again ? (y/n):"))
        elif choice == 2:
            repeat = "y"
            while repeat == "yes" or repeat == "y":
                menu2()
                choice2 = int(input("\n enter choice: "))
                if choice2 == 1:
                    i = mass()
                    for j in i:
                        resize(j)
                elif choice2 == 2:
                    i = mass()
                    for j in i:
                        reduce(j)
                elif choice2 == 3:
                    i = mass()
                    for j in i:
                        rotated(j)
                elif choice2 == 4:
                    i = mass()
                    for j in i:
                        grayscale(j)
                elif choice2 == 5:
                    i = mass()
                    for j in i:
                        resolution(j)
                elif choice2 == 6:
                    i = mass()
                    for j in i:
                        bluring(j)
                elif choice2 == 7:
                    i = mass()
                    for j in i:
                        sharpening(j)
                elif choice2 == 8:
                    i = mass()
                    for j in i:
                        smooth(j)
                elif choice2 == 9:
                    exit()
                else:
                    print("\nEnter a valid choice!!!! ")
                    continue
                repeat = input(("\nDo you want to continue again ? (y/n):"))
        else:
            print("\nEnter a valid choice!!!! ")
            continue
        repeat2 = input(("\nDo you want to continue again ? (y/n):"))
except Exception:
    print("Something went wrong!!!! ")