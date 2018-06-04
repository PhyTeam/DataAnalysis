import numpy as np
import pandas as pd
import tensorflow as tf
import seaborn as sns
import matplotlib.pyplot as plt
import keras
import json
def load_json_file():
    file_path = 'pydata-book/datasets/bitly_usagov/example.txt'
    dataset = []
    with open(file_path) as f:
        dataset = [json.loads(line) for line in f]

    print("Total records :" , len(dataset))
    return dataset

if __name__ == '__main__':
    d = pd.Series(np.random.randn(9), index=
              [['a','a', 'a', 'b','b','c','c','c', 'c'],
               [1,2,3,4,5,6,7,8,9]])

    fd = pd.DataFrame(load_json_file())
    clean_data = fd['tz'].fillna('Missing');
    clean_data[clean_data == ''] = 'Unknow'
    stat = clean_data.value_counts()[:10]
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    sns.barplot(y=stat.index, x=stat.values, ax=ax)
    plt.show()