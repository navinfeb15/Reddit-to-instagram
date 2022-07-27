import os
from PIL import Image
from time import sleep
import moviepy.editor as mp
from rscrapy import log_in, down_imgs
from insta_bot import upload_post, readcsv, clean_up


# Renaming images to .JPEG extension
def change_extsn():
    for file in os.listdir():

        if os.path.splitext(file)[1] == ".jpg" or os.path.splitext(file)[1] == ".png":

            im = Image.open(file)
            rgb_im = im.convert("RGB")
            # change both png to jpeg
            rgb_im.save(f'{file.split(".")[0]}.jpeg', "JPEG")

            if os.path.isfile(f'{file.split(".")[0]}.jpg'):
                os.remove(f'{file.split(".")[0]}.jpg')
            elif os.path.isfile(
                f'{file.split(".")[0]}.png'
            ):  # Uncomment these two lines
                os.remove(f'{file.split(".")[0]}.png')
            im.close()


def conv_to_vid():
    try:
        for file in os.listdir():
            if file.endswith(".gif"):
                clip = mp.VideoFileClip(file)
                fn = file.split(".")[0] + ".mp4"
                clip.write_videofile(fn)
                clip.close()
                sleep(5)
    except Exception as e:
        print("Error during Converting ", file, " to mp4: ", e)
        pass
    try:
        for file in os.listdir():
            if file.endswith(".gif"):
                os.remove(os.path.join(os.getcwd(), file))
    except Exception as e:
        print("Error during Deleting ", file, ": ", e)
        pass


# Making images square...
def change_ratio():
    for file in os.listdir():
        if file.endswith("jpeg"):

            try:
                file_path = os.path.join(os.getcwd(), file)
                if not file.endswith(".gif"):
                    image = Image.open(file_path, "r")
                    image_size = image.size
                    width = image_size[0]
                    height = image_size[1]
                    if width != height:
                        bigside = width if width > height else height

                        background = Image.new(
                            "RGB", (bigside, bigside), (255, 255, 255, 255)
                        )
                        offset = (
                            int(round(((bigside - width) / 2), 0)),
                            int(round(((bigside - height) / 2), 0)),
                        )

                        background.paste(image, offset)
                        background.save(file_path.split("/")[-1])
                        print(
                            file_path.split("/")[-1], " ====>  Image has been resized !"
                        )
                        image.close()

                    else:
                        print(
                            file_path.split("/")[-1],
                            " ====>  Image is already a square, it has not been resized !",
                        )

            except Exception as e:
                print("Error during image reformatting: ", e)
                pass


clean_up()
log_in()
down_imgs()

readcsv()
change_extsn()
change_ratio()
conv_to_vid()


upload_post()
