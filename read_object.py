import classes

def create_Image(file_name):
    """Create list of object Image from text file"""
    # Read file
    f = open(file_name, "r")

    images = []
    counter = 0
    # Loop over lines
    for line in f.readlines():
        line = line.replace("\n", "").split(" ")
        # Append Image objects to images
        new_img =  classes.Image(counter, line[0], line[2:])
        images.append(new_img)
        counter += 1

    return images

if __name__ == '__main__':

    file_name = "data/e_shiny_selfies.txt"
    imgs = create_Image(file_name)
    print(imgs[2].id, imgs[2].tags, imgs[2].tags)
    print(len(imgs))

    # Create slides
    slides = [classes.slide() for i in range(len(imgs))]

    count = 0
    lonely = False
    # Iterate over images to put them in the slides list
    for i in range(len(imgs)):
        # Insert horizontal image
        if imgs[i].orientation == "H":
            slides[count].insert(imgs[i])
            count += 1
        # Insert two verticals if a lonely index is present
        elif lonely is not False:
            slides[count].insert(imgs[lonely])
            slides[count].insert(imgs[i])
            count += 1
        # Store this lonely vertical image
        else:
            lonely = i

    # Delete empty slides
    del slides[count:]

