import os

one = os.listdir("../arc/arc")
two = os.listdir("equilux")

excluded = [
    "arrow-down-small-insens.png",
    "arrow-down-small-prelight.png",
    "arrow-down-small.png",
    "arrow-up-small-insens.png",
    "arrow-up-small-prelight.png",
    "arrow-up-small.png",
    "button-focus.png"
]

for file in sorted([file for file in one if file not in two and file not in excluded]):
    print(file)


