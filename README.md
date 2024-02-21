# PadSeeEw_best10.h5 Model Architecture

<code>
inputIm = Input(shape=(IMAGE_SIZE[0],IMAGE_SIZE[1],3,))
conv1 = Conv2D(32,3,activation='relu')(inputIm)
conv1 = Conv2D(64,3,activation='relu')(conv1)
conv1 = BatchNormalization()(conv1)
pool1 = MaxPool2D()(conv1)
conv2 = Conv2D(128,3,activation='relu')(pool1)
conv2 = Conv2D(128,3,activation='relu')(conv2)
conv2 = BatchNormalization()(conv2)
pool2 = MaxPool2D()(conv2)
conv3 = Conv2D(256,3,activation='relu')(pool2)
conv3 = Conv2D(256,3,activation='relu')(conv3)
conv3 = BatchNormalization()(conv3)
pool3 = MaxPool2D()(conv3)
conv4 = Conv2D(512,3,activation='relu')(pool3)
conv4 = BatchNormalization()(conv4)
pool5 = MaxPool2D()(conv4)
flat = Flatten()(pool3)
dense1 = Dense(512,activation='sigmoid')(flat)
dense1 = Dropout(0.5)(dense1)
dense1 = Dense(512,activation='sigmoid')(dense1)
dense1 = Dropout(0.5)(dense1)
dense1 = Dense(512,activation='sigmoid')(dense1)
dense1 = Dropout(0.5)(dense1)
predictedW = Dense(3,activation='sigmoid')(dense1)</code>

---

# PadSeeEw_best15.h5 Model Architecture

<code>
inputIm = Input(shape=(IMAGE_SIZE[0],IMAGE_SIZE[1],3,))
conv1 = Conv2D(32,3,activation='relu')(inputIm)
conv1 = BatchNormalization()(conv1)
pool1 = MaxPool2D()(conv1)
conv2 = Conv2D(64,3,activation='relu')(pool1)
conv2 = BatchNormalization()(conv2)
pool2 = MaxPool2D()(conv2)
conv3 = Conv2D(128,3,activation='relu')(pool2)
conv3 = BatchNormalization()(conv3)
pool3 = MaxPool2D()(conv3)
conv4 = Conv2D(256,3,activation='relu')(pool3)
conv4 = BatchNormalization()(conv4)
pool4 = MaxPool2D()(conv4)
flat = Flatten()(pool4)
dense1 = Dense(256,activation='sigmoid')(flat)
dense1 = Dropout(0.5)(dense1)
predictedW = Dense(3,activation='sigmoid')(dense1)</code>

---

# PadSeeEw_best100.h5 Model Architecture

<code>
inputIm = Input(shape=(IMAGE_SIZE[0],IMAGE_SIZE[1],3,))
conv1 = Conv2D(32,3,activation='relu')(inputIm)
conv1 = BatchNormalization()(conv1)
pool1 = MaxPool2D()(conv1)
conv2 = Conv2D(32,3,activation='relu')(pool1)
conv2 = BatchNormalization()(conv2)
pool2 = MaxPool2D()(conv2)
flat = Flatten()(pool2)
dense1 = Dense(256,activation='sigmoid')(flat)
dense1 = Dropout(0.5)(dense1)
predictedW = Dense(3,activation='sigmoid')(dense1)</code>

---

# PadSeeEw_best150.h5 Model Architecture

<code>
inputIm = Input(shape=(IMAGE_SIZE[0],IMAGE_SIZE[1],3,))
conv1 = Conv2D(64,3,activation='relu')(inputIm)
conv1 = BatchNormalization()(conv1)
pool1 = MaxPool2D()(conv1)
conv2 = Conv2D(128,3,activation='relu')(pool1)
conv2 = BatchNormalization()(conv2)
pool2 = MaxPool2D()(conv2)
conv3 = Conv2D(256,3,activation='relu')(pool2)
conv3 = BatchNormalization()(conv3)
pool3 = MaxPool2D((3,3))(conv3)
flat = Flatten()(pool3)
dense1 = Dense(256,activation='sigmoid')(flat)
dense1 = Dropout(0.5)(dense1)
dense1 = Dense(256,activation='sigmoid')(flat)
dense1 = Dropout(0.5)(dense1)
dense1 = Dense(256,activation='sigmoid')(flat)
dense1 = Dropout(0.5)(dense1)
predictedW = Dense(3,activation='sigmoid')(dense1)
</code>
