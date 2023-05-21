import tensorflow as tf
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Data augmentation
train_datagen = ImageDataGenerator(
    rescale=1./255,
    rotation_range=30,
    zoom_range=0.2,
    shear_range=0.2,
    horizontal_flip=True,
    fill_mode='reflect',
)

val_datagen = ImageDataGenerator(
    rescale=1./255,
    rotation_range=20,
    zoom_range=0.1,
    shear_range=0.1,
    horizontal_flip=True,
    fill_mode='reflect',
)

# Directories and batch size
train_dir = r'D:\Project-project\Pemilah Sampah\Datasheet created\train'
val_dir = r'D:\Project-project\Pemilah Sampah\Datasheet created\validation'
img_rows, img_cols = 100, 100
sub_object,batch_size = 3,3

# Image data generators
train_generator = train_datagen.flow_from_directory(
    train_dir,
    target_size=(img_rows, img_cols),
    batch_size=batch_size,
    class_mode='categorical',
    classes=['kertas', 'botol', 'kaleng']
)

val_generator = val_datagen.flow_from_directory(
    val_dir,
    target_size=(img_rows, img_cols),
    batch_size=batch_size,
    class_mode='categorical',
    classes=['kertas', 'botol', 'kaleng']
)

# Model architecture
model = tf.keras.models.Sequential([
    tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(img_rows, img_cols, sub_object), kernel_regularizer=tf.keras.regularizers.l2(0.01)),
    tf.keras.layers.BatchNormalization(),
    tf.keras.layers.MaxPooling2D(2, 2),
    tf.keras.layers.Dropout(0.25),

    tf.keras.layers.Conv2D(64, (3, 3), activation='relu', kernel_regularizer=tf.keras.regularizers.l2(0.01)),
    tf.keras.layers.BatchNormalization(),
    tf.keras.layers.MaxPooling2D(2, 2),
    tf.keras.layers.Dropout(0.25),

    tf.keras.layers.Conv2D(128, (3, 3), activation='relu', kernel_regularizer=tf.keras.regularizers.l2(0.01)),
    tf.keras.layers.BatchNormalization(),
    tf.keras.layers.MaxPooling2D(2, 2),
    tf.keras.layers.Dropout(0.25),

    tf.keras.layers.Flatten(),

    tf.keras.layers.Dense(256, activation='relu', kernel_regularizer=tf.keras.regularizers.l2(0.01)),
    tf.keras.layers.BatchNormalization(),
    tf.keras.layers.Dropout(0.5),

    tf.keras.layers.Dense(128, activation='relu', kernel_regularizer=tf.keras.regularizers.l2(0.01)),
    tf.keras.layers.BatchNormalization(),
    tf.keras.layers.Dropout(0.5),

    tf.keras.layers.Dense(sub_object, activation='softmax')
])

model.summary()

# Compile the model
optimizer = Adam(learning_rate=0.05)
model.compile(loss='categorical_crossentropy', optimizer=optimizer, metrics=['accuracy'])

# Callbacks
class myCallback(tf.keras.callbacks.Callback):
    def on_epoch_end(self, epoch, logs={}):
        if logs.get('accuracy') > 0.95:
            print('\nAkurasi mencapai 95%')
            self.model.stop_training = True

callbacks = myCallback()

# Train the model
history = model.fit(
train_generator,
steps_per_epoch= train_generator.n // batch_size,
epochs=50,
validation_data=val_generator,
validation_steps=3,
verbose=1,
callbacks=[callbacks]
)

# Save the model
model.save('D:\Project-project\Pemilah Sampah\Datasheet created\datasheet_new.h5')
