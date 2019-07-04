import sys
import numpy as np
import pandas as pd
from PIL import Image


def fill_stars(percentage, name):
    stars = Image.open("../media/stars_template.png")
    w, h = stars.width, stars.height

    background = Image.new("RGB", (int(w * percentage), int(h)), (255, 203, 0))

    combinedImage = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    combinedImage.paste(background, (0, 0))
    combinedImage.paste(stars, (0, 0), mask=stars)
    combinedImage.save(f"../media/ratings/{name}.png", format="png")


file_name = sys.argv[1]

data = pd.read_csv(file_name)

average_score = round(data.ratings.mean(), 1)
percentage_score = average_score / 5

cry_o_meter = round(data.cry.mean() * 100)

print(f"Average rating: {percentage_score}")

fill_stars(percentage_score, file_name.split("/")[-1][:-4])

