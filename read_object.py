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
