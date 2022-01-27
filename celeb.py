import pandas as pd
import enum

"""
goal:
* celebrity 20 question game
* python to work through basic logic
* react / typescript /tailwind to actually build
* goal - actually deploy and get people besides myself playing and providing feedback
    - could use as way for friends to learn to code (basic PR's like adding q's, adding celebs)


how this works

- random celebrity chosen from list
- user presented list of questions to choose from
- user selects question
    - game answers yes or no
- user can guess is it ... at any point
    - if they guess correctly they win
    - if they guess incorrectly they lose


python code just to test the logic

"""


df = pd.read_csv("celebs.csv", index_col=0)

celebs = df.index.tolist()

qlist = list(df.columns)[1:]


count = 0
while count < 3:
    count += 1

print("you lose")
