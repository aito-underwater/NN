import random

from algorithms import NeuralNetwork as nn
import pandas as pd
import numpy as np

df = pd.read_csv('../datas/ExampleData.csv', index_col=0)

df = np.array(pd.DataFrame(df, columns = ["volt","rotate","pressure","vibration"]))


y = [] # test Data
k = 0

for i in df:
    y.append([])
    for j in range(len(i)):
        y[k].append(round(random.uniform(-10.0, 10.0),5))
    k = k +1





input_layer_size = 4
secret_layer_size = 4
secret_layer_count = 2
generation_count = 1


new_model = nn.AITONeuralNetwork(input_layer_size, secret_layer_size, secret_layer_count,
                                 generation_count)
new_model.set_up()

new_model.fit(input_x=df,
              output_y=y, iteration=2, genetic_iteration=1)

new_model.save_model()

y = new_model.predict([162.46283326, 346.14933504, 109.24856128, 41.12214409])


print(y)