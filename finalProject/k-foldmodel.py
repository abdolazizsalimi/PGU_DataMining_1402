from sklearn.model_selection import KFold
from tensorflow.keras.layers import Conv2D, MaxPooling2D, BatchNormalization
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import ReduceLROnPlateau
from tensorflow.keras.regularizers import L1, L2, L1L2
from tensorflow.keras.layers import GaussianNoise, Lambda
import tensorflow as tf
def create_model():
    model = Sequential([
        base_model,
        Conv2D(512, (3, 3), padding='same'),
        LeakyReLU(alpha=leaky_relu_alpha),
        BatchNormalization(),
        MaxPooling2D((2, 2)),
        Conv2D(256, (3, 3), activation='relu', padding='same'),
        BatchNormalization(),
        MaxPooling2D((2, 2)),
        Conv2D(128, (3, 3), activation='relu', padding='same'),
        BatchNormalization(),
        GlobalAveragePooling2D(),
        Dense(128, activation='relu'),
        BatchNormalization(),
        Dropout(0.4),
        Dense(64, activation='relu'),
        Dropout(0.6),
        Dense(num_classes, activation='softmax')
    ])
    optimizer = Adam(learning_rate=0.001)
    model.compile(optimizer=optimizer, loss='categorical_crossentropy', metrics=['accuracy'])
    return model




def train_and_evaluate_model(X_data, y_data, n_splits=5):
    kfold = KFold(n_splits=n_splits, shuffle=True, random_state=42)
    histories = []
    fold = 1

    for train_idx, val_idx in kfold.split(X_data, y_data):
        print(f"Training fold {fold}")
        model = create_model()

        # Prepare training and validation data
        X_train, X_val = X_data[train_idx], X_data[val_idx]
        y_train, y_val = y_data[train_idx], y_data[val_idx]

        # Train the model
        history = model.fit(
            X_train,
            y_train,
            epochs=epochs,
            validation_data=(X_val, y_val),
            callbacks=[
                early_stopping,
                lr_scheduler,
                model_checkpoint,
            ]
        )

        histories.append(history)
        fold += 1

    return histories




# histories = train_and_evaluate_model(X_data, y_data, n_splits=5)