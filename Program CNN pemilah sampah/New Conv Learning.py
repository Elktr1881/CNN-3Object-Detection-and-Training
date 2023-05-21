import tensorflow as tf
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Dense, Conv2D, MaxPooling2D, Flatten
from keras.callbacks import EarlyStopping


# Set the batch size and number of epochs
batch_size = 3
epochs = 250

# Set the dimensions of the input image
input_shape = (150, 150, 3)

# Set the directory for the training and validation data
train_dir = r'D:\Project-project\Pemilah Sampah\Datasheet created\train'
val_dir = r'D:\Project-project\Pemilah Sampah\Datasheet created\validation'

# Create the data generators for the training and validation data
train_datagen = ImageDataGenerator(
    rescale=1./255,
      rotation_range=30,
    #   width_shift_range=0.2,
    #   height_shift_range=0.2,
    #   shear_range=0.2,
    #   zoom_range=0.2,
      horizontal_flip=True,
      fill_mode='nearest'
    )
train_generator = train_datagen.flow_from_directory(
        train_dir,
        target_size=input_shape[:2],
        batch_size=batch_size,
        class_mode='categorical',
        classes=['botol', 'kaleng', 'kertas'])

# val_datagen = ImageDataGenerator(rescale=1./255)
val_generator = val_datagen.flow_from_directory(
        val_dir,
        target_size=input_shape[:2],
        batch_size=batch_size,
        class_mode='categorical',
        classes=['botol', 'kaleng', 'kertas'])

# Build the model
model = Sequential()
model.add(Conv2D(32, (3, 3), activation='relu', input_shape=input_shape))
model.add(MaxPooling2D((2, 2)))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))
model.add(Conv2D(128, (3, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))
model.add(Conv2D(128, (3, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))
model.add(Flatten())
model.add(Dense(512, activation='relu'))
model.add(Dense(3, activation='softmax'))

# model = tf.keras.models.Sequential([
#   tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(150, 150, 3)),
#   tf.keras.layers.BatchNormalization(),
#   tf.keras.layers.MaxPooling2D((2, 2)),
#   tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
#   tf.keras.layers.BatchNormalization(),
#   tf.keras.layers.MaxPooling2D((2, 2)),
#   tf.keras.layers.Conv2D(128, (3, 3), activation='relu'),
#   tf.keras.layers.BatchNormalization(),
#   tf.keras.layers.MaxPooling2D((2, 2)),
#   tf.keras.layers.Conv2D(256, (3, 3), activation='relu'),
#   tf.keras.layers.BatchNormalization(),
#   tf.keras.layers.MaxPooling2D((2, 2)),
#   tf.keras.layers.Flatten(),
#   tf.keras.layers.Dense(512, activation='relu'),
#   tf.keras.layers.Dropout(0.5),
#   tf.keras.layers.Dense(3, activation='softmax')
# ])

# model = tf.keras.models.Sequential([
#           tf.keras.layers.Conv2D(32, (3, 3), activation = 'relu', input_shape = (150,150,3)),
#           tf.keras.layers.MaxPooling2D(2, 2),
#           tf.keras.layers.Conv2D(64, (3, 3), activation = 'relu'),
#           tf.keras.layers.MaxPooling2D(2, 2),
#           tf.keras.layers.Conv2D(32, (3, 3), activation = 'relu'),
#           tf.keras.layers.MaxPooling2D(2, 2),
#           tf.keras.layers.Flatten(),
#           tf.keras.layers.Dense(200, activation = 'relu'),
#           tf.keras.layers.Dropout(0.3,seed=112),
#           tf.keras.layers.Dense(500, activation = 'relu'),
#           tf.keras.layers.Dropout(0.5,seed=112),
#           tf.keras.layers.Dense(3, activation = 'softmax')
# ])

model.summary()

# Compile the model
# mengkompilasi model
model.compile(loss='categorical_crossentropy',
              optimizer=tf.optimizers.Adam(),
              metrics=['accuracy'])
# model.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['accuracy'])

# Set up the early stopping callback
class myCallback(tf.keras.callbacks.Callback):
    def on_epoch_end(self, epoch, logs={}):
        if logs.get('accuracy') > 0.98:
            print('\nAkurasi mencapai 98%')
            self.model.stop_training = True

callbacks = myCallback()

# Train the model
history = model.fit(
        train_generator,
        # steps_per_epoch=train_generator.samples // batch_size,
        steps_per_epoch=20,
        epochs=epochs,
        validation_data=val_generator,
        validation_steps=val_generator.samples // batch_size,
        #validation_steps=3,
        verbose=1,
        callbacks=[early_stop, callbacks])

# Save the model
model.save('D:\Project-project\Pemilah Sampah\Datasheet created\datasheet1405_6.h5')