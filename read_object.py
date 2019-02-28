import classes
import random

def create_Image(file_name):
    """Create list of object Image from text file"""
    # Read file
    f = open(file_name, "r")

    images = []
    counter = 0
    # Loop over lines
    for line in f.readlines()[1:]:
        line = line.replace("\n", "").split(" ")
        # Append Image objects to images
        new_img =  classes.Image(counter, line[0], line[2:])
        images.append(new_img)
        counter += 1

    return images


def create_slides(imgs):
    """Create list of slides from a list of images"""
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
        elif lonely:
            slides[count].insert(imgs[lonely])
            slides[count].insert(imgs[i])
            count += 1
            lonely = False
        # Store this lonely vertical image
        else:
            lonely = i

    # Delete empty slides
    del slides[count:]

    return slides


def create_random_slides(imgs):
    """Create list of slides from a list of images"""
    # Create slides
    slides = [classes.slide() for i in range(len(imgs))]

    order = [i for i in range(len(slides))]
    random.shuffle(order)

    count = 0
    lonely = False
    # Iterate over images to put them in the slides list
    for i in order:
        # Insert horizontal image
        if imgs[i].orientation == "H":
            slides[count].insert(imgs[i])
            count += 1
        # Insert two verticals if a lonely index is present
        elif lonely is not False:
            slides[count].insert(imgs[lonely])
            slides[count].insert(imgs[i])
            count += 1
            lonely = False
        # Store this lonely vertical image
        else:
            lonely = i

    # Delete empty slides
    del slides[count:]

    return slides


def create_file(slides, file_name_output):
    """Write an output file from the slides"""
    with open(file_name_output, "w") as f:
        # Write the number of slides
        f.write(str(len(slides))+"\n")

        # Write per slide the photo id
        for slide in slides:
            line = ""
            for i in range(len(slide.images)):
                if i > 0:
                    line += " "
                line += str(slide.images[i].id)
            line += "\n"
            # Write line
            f.write(line)

def score_slidelist(slidelist):
    return sum([slidelist[i-1].score(elem) for i, elem in enumerate(slidelist)])



def get_nums(file_name):
    """Create list of object Image from text file"""
    # Read file
    f = open(file_name, "r")

    ids = []
    nums = []
    counter = 0
    # Loop over lines
    for line in f.readlines()[1:]:
        line = line.replace("\n", "").split(" ")
        # Append Image objects to images
        new_img =  classes.Image(counter, line[0], line[2:])
        ids.append(counter)
        nums.append(len(new_img.tags))
        counter += 1

    return ids, nums


def create_tryout_slides(imgs):
    """Create list of slides from a list of images"""
    # Create slides
    slides = [classes.slide() for i in range(len(imgs))]

    ids, nums = get_nums(imgs)

    order = [i for i in range(len(slides))]
    random.shuffle(order)

    count = 0
    lonely = False
    # Iterate over images to put them in the slides list
    for i in order:
        # Insert horizontal image
        if imgs[i].orientation == "H":
            slides[count].insert(imgs[i])
            count += 1
        # Insert two verticals if a lonely index is present
        elif lonely is not False:
            slides[count].insert(imgs[lonely])
            slides[count].insert(imgs[i])
            count += 1
            lonely = False
        # Store this lonely vertical image
        else:
            lonely = i

    # Delete empty slides
    del slides[count:]

    return slides



if __name__ == '__main__':
    file_names = ["data/a_example.txt", "data/b_lovely_landscapes.txt", "data/c_memorable_moments.txt", "data/d_pet_pictures.txt", "data/e_shiny_selfies.txt"]
    # file_name = "data/d_pet_pictures.txt"
    for file_name in file_names:
        # Create list of images
        imgs = create_Image(file_name)
        # Create list of slides in order of the file
        slides = create_slides(imgs)

        # Create output file
        create_file(slides, "results/"+file_name[5:-4]+"order_output.txt")
