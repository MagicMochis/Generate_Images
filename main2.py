import turtle
from PIL import Image
import random
import json

Total_images = 4000
myPen = turtle.Turtle()
myPen.speed(0)
myPen.color("#000000")
top_choices = ["Beanie", "Cook", "Sprout", "Swirly", "Bunny", "Original"]
top_weights = [27,23,11,15,19,5]
eye_choices = ["Ninja", "Shocked","Angry", "Sunglasses", "Original"]
eye_weights = [30,25,20,15,10]
nose_choices = ["Original", "Twirly", "Smirk", "Straight"]
nose_weights = [50,25,15,10]
background_choices = ["SeaGreen2", "DeepSkyBlue4", "Gold", "PaleVioletRed", "Purple"]
background_weights = [40,5,15,23,17]
facecolor_choices = ["Thistle", "Orchid", "PaleGreen2", "Cyan"]
facecolor_weights = [30,35,15,20]
underbelly_choices = ["Chartreuse3", "DarkViolet", "NavajoWhite", "LightPink"]
underbelly_weights = [15,25,27,33]
all_images = []



def create_new_image():
    new_image = {}
    new_image["Background"] = random.choices(background_choices, background_weights)[0]
    new_image["Top"] = random.choices(top_choices, top_weights)[0]
    new_image["Eyes"] = random.choices(eye_choices, eye_weights)[0]
    new_image["Facecolor"] = random.choices(facecolor_choices, facecolor_weights)[0]
    new_image["Underbelly"] = random.choices(underbelly_choices, underbelly_weights)[0]
    new_image["Nose"] = random.choices(nose_choices, nose_weights)[0]

    if new_image in all_images:
        return create_new_image()
    else:
        return new_image


for i in range(Total_images):
    new_trait_image = create_new_image()
    all_images.append(new_trait_image)

def all_images_unique(all_images):
    seen = list()
    return not any(i in seen or seen.append(i) for i in all_images)

print("Are all images unique?", all_images_unique(all_images))

# add the tokens!
i = 0
for item in all_images:
    item["tokenId"] = i
    i = i + 1

background_count = {}
for item in background_choices:
    background_count[item] = 0

top_count = {}
for item in top_choices:
    top_count[item] = 0

facecolor_count = {}
for item in facecolor_choices:
    facecolor_count[item] = 0

underbelly_count = {}
for item in underbelly_choices:
    underbelly_count[item] = 0

eye_count = {}
for item in eye_choices:
    eye_count[item] = 0

nose_count = {}
for item in nose_choices:
    nose_count[item] = 0

for image in all_images:
    background_count[image["Background"]] += 1
    top_count[image["Top"]] += 1
    facecolor_count[image["Facecolor"]] += 1
    underbelly_count[image["Underbelly"]] += 1
    eye_count[image["Eyes"]] += 1
    nose_count[image["Nose"]] += 1

print(background_count)
print(top_count)
print(facecolor_count)
print(underbelly_count)
print(eye_count)
print(nose_count)

METADATA_FILE_NAME = './metadata/all-traits.json';
with open(METADATA_FILE_NAME, 'w') as outfile:
    json.dump(all_images, outfile, indent=4)

f = open('./metadata/all-traits.json',)
data = json.load(f)


PROJECT_NAME = "Mochi"

def getData(type, value):
    return {
        "trait_type": type,
        "value": value
    }
for i in data:
    token_id = i['tokenId']
    token = {
        "image": IMAGES_URI + str(token_id) + '.png',
        "tokenId": token_id,
        "name": PROJECT_NAME + ' ' + str(token_id),
        "attributes": []
    }
    token["attributes"].append(getData("Background", i["Background"]))
    token["attributes"].append(getData("Top", i["Top"]))
    token["attributes"].append(getData("Facecolor", i["Facecolor"]))
    token["attributes"].append(getData("Underbelly", i["Underbelly"]))
    token["attributes"].append(getData("Eyes", i["Eyes"]))
    token["attributes"].append(getData("Nose", i["Nose"]))

    with open('./metadata/' + str(token_id), 'w') as outfile:
        json.dump(token, outfile, indent=4)
f.close()

def box(intDim):
    myPen.begin_fill()
    # 0 deg.
    myPen.forward(intDim)
    myPen.left(90)
    # 90 deg.
    myPen.forward(intDim)
    myPen.left(90)
    # 180 deg.
    myPen.forward(intDim)
    myPen.left(90)
    # 270 deg.
    myPen.forward(intDim)
    myPen.end_fill()
    myPen.setheading(0)

# time to generate the images
for item in all_images:
    background = item["Background"]
    top = item["Top"]
    eyes = item["Eyes"]
    nose = item["Nose"]
    underbelly = item["Underbelly"]
    facecolor = item["Facecolor"]
    body = ["Original"]
    eyebottom = "MistyRose"
    eyetop = "tan"
    topaccessory_1 = "red"
    topaccessory_2 = "LightGrey"
    topaccessory_3 = "green"
    topaccessory_4 = "LightGreen"
    ninjaband = "blue"

    turtle.setup()
    turtle.hideturtle()
    myPen = turtle.Turtle()
    myPen.speed(0)
    myPen.color("#000000")
    boxSize = 10
    # Position myPen in top left area of the screen
    myPen.penup()
    myPen.forward(-178)
    myPen.setheading(90)
    myPen.forward(165)
    myPen.setheading(0)


    # Here is how your PixelArt is stored (using a "list of lists")
    colourPalette = [background, "black", eyebottom, ninjaband, facecolor, underbelly, eyetop, topaccessory_1, topaccessory_2, topaccessory_3, topaccessory_4, "white"]
    pixels = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    pixels.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

    if top == "Beanie":
        pixels.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        pixels.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 7, 7, 7, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        pixels.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 7, 7, 7, 7, 7, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        pixels.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 7, 7, 7, 7, 7, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        pixels.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        pixels.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        pixels.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        pixels.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    elif top == "Cook":
        pixels.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 8, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        pixels.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 8, 8, 8, 8, 8, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        pixels.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        pixels.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        pixels.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        pixels.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        pixels.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        pixels.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    elif top == "Sprout":
        pixels.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        pixels.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 10, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        pixels.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 10, 9, 10, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        pixels.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 9, 10, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        pixels.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        pixels.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        pixels.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        pixels.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    elif top == "Swirly":
        pixels.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        pixels.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        pixels.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        pixels.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        pixels.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        pixels.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        pixels.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        pixels.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 7, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    elif top == "Bunny":
        pixels.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        pixels.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 9, 8, 0, 0, 0, 0, 0, 0, 0, 8, 9, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        pixels.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 9, 8, 0, 0, 0, 0, 0, 0, 0, 8, 9, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        pixels.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 9, 8, 0, 0, 0, 0, 0, 0, 0, 8, 9, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        pixels.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 9, 8, 0, 0, 0, 0, 0, 0, 0, 8, 9, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        pixels.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 9, 8, 0, 0, 0, 0, 0, 0, 0, 8, 9, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        pixels.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 9, 8, 0, 0, 0, 0, 0, 0, 0, 8, 9, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        pixels.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 8, 0, 0, 0, 0, 0, 0, 0, 8, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    elif top == "Original":
        pixels.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        pixels.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        pixels.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        pixels.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        pixels.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        pixels.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        pixels.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        pixels.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    ######################################
    # Now do the eyes
    ######################################
    if eyes == "Original":
        pixels.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        pixels.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        pixels.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        pixels.append([0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0])
        pixels.append([0, 0, 0, 0, 0, 0, 0, 0, 1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 1, 0, 0, 0, 0, 0, 0, 0, 0])
        pixels.append([0, 0, 0, 0, 0, 0, 1, 1, 1, 4, 4, 4, 6, 6, 6, 4, 4, 4, 4, 4, 6, 6, 6, 4, 4, 4, 1, 1, 1, 0, 0, 0, 0, 0, 0])
        pixels.append([0, 0, 0, 0, 0, 0, 1, 4, 4, 4, 4, 4, 6, 6, 6, 4, 4, 4, 4, 4, 6, 6, 6, 4, 4, 4, 4, 4, 1, 0, 0, 0, 0, 0, 0])
        pixels.append([0, 0, 0, 0, 0, 1, 1, 4, 4, 4, 4, 4, 2, 1, 2, 4, 4, 4, 4, 4, 2, 1, 2, 4, 4, 4, 4, 4, 1, 1, 0, 0, 0, 0, 0])
        pixels.append([0, 0, 0, 0, 0, 1, 4, 4, 4, 4, 4, 4, 2, 1, 1, 4, 4, 4, 4, 4, 2, 1, 1, 4, 4, 4, 4, 4, 4, 1, 0, 0, 0, 0, 0])
    elif eyes == "Ninja":
        pixels.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        pixels.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        pixels.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 1, 0, 0, 0, 3, 3, 0, 0, 0, 0])
        pixels.append([0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 1, 1, 0, 3, 3, 3, 0, 0, 0, 0])
        pixels.append([0, 0, 0, 0, 0, 0, 0, 0, 1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 1, 0, 3, 3, 0, 0, 0, 0, 0])
        pixels.append([0, 0, 0, 0, 0, 0, 1, 1, 1, 3, 3, 3, 6, 6, 6, 3, 3, 3, 3, 3, 6, 6, 6, 3, 3, 3, 1, 1, 1, 0, 0, 0, 0, 0, 0])
        pixels.append([0, 0, 0, 0, 0, 0, 1, 3, 3, 3, 3, 3, 6, 6, 6, 3, 3, 3, 3, 3, 6, 6, 6, 3, 3, 3, 3, 3, 1, 3, 3, 0, 0, 0, 0])
        pixels.append([0, 0, 0, 0, 0, 1, 1, 3, 3, 3, 3, 3, 2, 1, 2, 3, 3, 3, 3, 3, 2, 1, 2, 3, 3, 3, 3, 3, 1, 1, 3, 3, 0, 0, 0])
        pixels.append([0, 0, 0, 0, 0, 1, 3, 3, 3, 3, 3, 3, 2, 1, 1, 3, 3, 3, 3, 3, 2, 1, 1, 3, 3, 3, 3, 3, 3, 1, 3, 3, 0, 0, 0])
    elif eyes == "Shocked":
        pixels.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        pixels.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        pixels.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        pixels.append([0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0])
        pixels.append([0, 0, 0, 0, 0, 0, 0, 0, 1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 1, 0, 0, 0, 0, 0, 0, 0, 0])
        pixels.append([0, 0, 0, 0, 0, 0, 1, 1, 1, 4, 4, 4, 11, 11, 11, 4, 4, 4, 4, 4, 11, 11, 11, 4, 4, 4, 1, 1, 1, 0, 0, 0, 0, 0, 0])
        pixels.append([0, 0, 0, 0, 0, 0, 1, 4, 4, 4, 4, 4, 11, 11, 11, 4, 4, 4, 4, 4, 11, 11, 11, 4, 4, 4, 4, 4, 1, 0, 0, 0, 0, 0, 0])
        pixels.append([0, 0, 0, 0, 0, 1, 1, 4, 4, 4, 4, 4, 11, 1, 11, 4, 4, 4, 4, 4, 11, 1, 11, 4, 4, 4, 4, 4, 1, 1, 0, 0, 0, 0, 0])
        pixels.append([0, 0, 0, 0, 0, 1, 4, 4, 4, 4, 4, 4, 11, 11, 11, 4, 4, 4, 4, 4, 11, 11, 11, 4, 4, 4, 4, 4, 4, 1, 0, 0, 0, 0, 0])
    elif eyes == "Angry":
        pixels.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        pixels.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        pixels.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        pixels.append([0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0])
        pixels.append([0, 0, 0, 0, 0, 0, 0, 0, 1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 1, 0, 0, 0, 0, 0, 0, 0, 0])
        pixels.append([0, 0, 0, 0, 0, 0, 1, 1, 1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 1, 1, 1, 0, 0, 0, 0, 0, 0])
        pixels.append([0, 0, 0, 0, 0, 0, 1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 1, 0, 0, 0, 0, 0, 0])
        pixels.append([0, 0, 0, 0, 0, 1, 1, 4, 4, 4, 4, 4, 1, 1, 1, 4, 4, 4, 4, 4, 1, 1, 1, 4, 4, 4, 4, 4, 1, 1, 0, 0, 0, 0, 0])
        pixels.append([0, 0, 0, 0, 0, 1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 1, 0, 0, 0, 0, 0])
    elif eyes == "Sunglasses":
        pixels.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        pixels.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        pixels.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        pixels.append([0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0])
        pixels.append([0, 0, 0, 0, 0, 0, 0, 0, 1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 1, 0, 0, 0, 0, 0, 0, 0, 0])
        pixels.append([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0])
        pixels.append([0, 0, 0, 0, 0, 0, 1, 4, 4, 4, 4, 1, 1, 1, 1, 1, 4, 4, 4, 1, 1, 1, 1, 1, 4, 4, 4, 4, 1, 0, 0, 0, 0, 0, 0])
        pixels.append([0, 0, 0, 0, 0, 1, 1, 4, 4, 4, 4, 1, 1, 1, 1, 1, 4, 4, 4, 1, 1, 1, 1, 1, 4, 4, 4, 4, 1, 1, 0, 0, 0, 0, 0])
        pixels.append([0, 0, 0, 0, 0, 1, 4, 4, 4, 4, 4, 1, 1, 1, 1, 1, 4, 4, 4, 1, 1, 1, 1, 1, 4, 4, 4, 4, 4, 1, 0, 0, 0, 0, 0])
    if nose == "Original":
        pixels.append([0, 0, 0, 0, 1, 1, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 1, 1, 0, 0, 0, 0])
        pixels.append([0, 0, 0, 0, 1, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 1, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 1, 0, 0, 0, 0])
        pixels.append([0, 0, 0, 1, 1, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 1, 1, 0, 0, 0])
    elif nose == "Twirly":
        pixels.append([0, 0, 0, 0, 1, 1, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 1, 1, 0, 0, 0, 0])
        pixels.append([0, 0, 0, 0, 1, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 1, 5, 1, 5, 1, 5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 1, 0, 0, 0, 0])
        pixels.append([0, 0, 0, 1, 1, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 1, 5, 1, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 1, 1, 0, 0, 0])
    elif nose == "Smirk":
        pixels.append([0, 0, 0, 0, 1, 1, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 1, 1, 0, 0, 0, 0])
        pixels.append([0, 0, 0, 0, 1, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 1, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 1, 0, 0, 0, 0])
        pixels.append([0, 0, 0, 1, 1, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 1, 1, 1, 1, 5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 1, 1, 0, 0, 0])
    elif nose == "Straight":
        pixels.append([0, 0, 0, 0, 1, 1, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 1, 1, 0, 0, 0, 0])
        pixels.append([0, 0, 0, 0, 1, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 1, 1, 1, 5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 1, 0, 0, 0, 0])
        pixels.append([0, 0, 0, 1, 1, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 1, 1, 0, 0, 0])
    if body == ["Original"]:
        pixels.append([0, 0, 1, 1, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 1, 1, 0, 0])
        pixels.append([0, 1, 1, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 1, 1, 0])
        pixels.append([0, 1, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 1, 0])
        pixels.append([0, 1, 5, 5, 5, 5, 5, 5, 1, 1, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 1, 1, 5, 5, 5, 5, 5, 5, 1, 0])
        pixels.append([0, 1, 5, 5, 5, 5, 5, 5, 1, 0, 1, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 1, 0, 1, 5, 5, 5, 5, 5, 5, 1, 0])
        pixels.append([0, 1, 5, 5, 5, 5, 5, 5, 5, 1, 0, 1, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 1, 0, 1, 5, 5, 5, 5, 5, 5, 5, 1, 0])
        pixels.append([0, 1, 5, 5, 5, 5, 5, 5, 5, 5, 1, 1, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 1, 1, 5, 5, 5, 5, 5, 5, 5, 5, 1, 0])
        pixels.append([0, 1, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 1, 0])
        pixels.append([0, 1, 1, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 1, 1, 0])
        pixels.append([0, 0, 1, 1, 1, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 1, 1, 1, 0, 0])
        pixels.append([0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0])
        pixels.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        pixels.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

    for i in range(0, len(pixels)):
        for j in range(0, len(pixels[i])):
            myPen.color(colourPalette[pixels[i][j]])
            box(boxSize)
            myPen.penup()
            myPen.forward(boxSize)
            myPen.pendown()
        myPen.setheading(270)
        myPen.penup()
        myPen.forward(boxSize)
        myPen.setheading(180)
        myPen.forward(boxSize * len(pixels[i]))
        myPen.setheading(0)
        myPen.pendown()

    myPen.getscreen().update()
    turtle.getscreen().getcanvas().postscript(file='outputname.ps')
    psimage = Image.open('outputname.ps')
    file_name = str(item["tokenId"]) + ".png"
    psimage.save("./images/" + file_name)
    turtle.clear()
    turtle.clearscreen()
    turtle.reset()

#top = random.choices(top_choices, top_weights)
#top = ["Beanie"]
#print(top)
#eyes = random.choices(eye_choices, eye_weights)
#print(eyes)
#nose = random.choices(nose_choices, nose_weights)

#background = random.choices(background_choices, background_weights)
#underbelly = random.choices(underbelly_choices, underbelly_weights)
#facecolor = random.choices(facecolor_choices, facecolor_weights)
# selects colors


