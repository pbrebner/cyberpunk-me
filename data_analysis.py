import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

rock_data = pd.read_csv("hand_gesture_0.csv", header=None)
scissors_data = pd.read_csv("hand_gesture_1.csv", header=None)
paper_data = pd.read_csv("hand_gesture_2.csv", header=None)
ok_data = pd.read_csv("hand_gesture_3.csv", header=None)

print(rock_data.head(5))
print(scissors_data.head(5))
print(paper_data.head(5))
print(ok_data.head(5))