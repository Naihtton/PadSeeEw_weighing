from keras.models import Model, load_model
from keras.preprocessing.image import ImageDataGenerator
import matplotlib.pyplot as plt
import pandas as pd

def normalize_columns(df, columns_to_normalize):
    for col in columns_to_normalize:
        df[col + "_norm"] = (df[col] - df[col].min()) / (df[col].max() - df[col].min())
    return df

def map_back(df, norm_value, col):
    min_val = df[col].min()
    max_val = df[col].max()
    return int(norm_value * (max_val - min_val) + min_val)

BATCH_SIZE = 20
IMAGE_SIZE = (256,384) # 2:3 ratio

dataframe = pd.read_csv('../fried_noodles_dataset.csv', delimiter=',', header=0)
og_df = dataframe.copy()  # Keep an unnormalized copy for mapping back
dataframe = normalize_columns(dataframe, ['meat', 'veggie', 'noodle'])
datagen = ImageDataGenerator(rescale=1./255)

test_generator = datagen.flow_from_dataframe(
    dataframe=dataframe.loc[1704:1856],
    directory='../images',
    x_col='filename',
    y_col=["meat_norm","veggie_norm","noodle_norm"],
    shuffle=False,
    target_size=IMAGE_SIZE,
    batch_size=BATCH_SIZE,
    class_mode='other')

model = load_model('PadSeeEw_best150.h5')

score = model.evaluate(
    test_generator,
    steps=len(test_generator))
print('score (mse, mae):\n',score)

test_generator.reset()
predict = model.predict(
    test_generator,
    steps=len(test_generator),
    workers = 1,
    use_multiprocessing=False)
print('prediction:\n',predict)

# Map predictions back to real values
df_result = pd.DataFrame(columns=['filename', 'meat', 'veggie', 'noodle'])

for i in range(len(predict)):
    meat_pred = map_back(og_df, predict[i][0], 'meat')
    veggie_pred = map_back(og_df, predict[i][1], 'veggie')
    noodle_pred = map_back(og_df, predict[i][2], 'noodle')

    df_result = df_result._append({
        'filename': dataframe.loc[1704:1856]['filename'].iloc[i], 
        'meat': meat_pred, 
        'veggie': veggie_pred, 
        'noodle': noodle_pred
    }, ignore_index=True) 

# Save to CSV
df_result.to_csv('result.csv', index=False) 