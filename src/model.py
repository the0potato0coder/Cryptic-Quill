import tensorflow as tf
import matplotlib.pyplot as plt

import tensorflow as tf

def build_model(vocab_size, max_length, num_classes):
    # Define the CNN model
    model = tf.keras.Sequential([
        tf.keras.layers.Embedding(input_dim=vocab_size + 1, output_dim=64, input_length=max_length),
        tf.keras.layers.Conv1D(filters=128, kernel_size=5, activation='relu'),
        tf.keras.layers.MaxPooling1D(pool_size=2),
        tf.keras.layers.Conv1D(filters=128, kernel_size=5, activation='relu'),
        tf.keras.layers.MaxPooling1D(pool_size=2),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(128, activation='relu'),
        tf.keras.layers.Dense(num_classes, activation='softmax')
    ])

    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    return model

def plot_history(history):
    # Plot accuracy and loss curves
    acc = history.history['accuracy']
    val_acc = history.history['val_accuracy']
    loss = history.history['loss']
    val_loss = history.history['val_loss']
    epochs = range(len(acc))

    plt.figure(figsize=(8, 6))
    plt.plot(epochs, acc, 'b', label='Training accuracy')
    plt.plot(epochs, val_acc, 'r', label='Validation accuracy')
    plt.title('Training and validation accuracy')
    plt.legend()

    plt.figure(figsize=(8, 6))
    plt.plot(epochs, loss, 'b', label='Training loss')
    plt.plot(epochs, val_loss, 'r', label='Validation loss')
    plt.title('Training and validation loss')
    plt.legend()

    plt.show()

if __name__ == "__main__":
    from data_preprocessing import load_and_preprocess_data

    # Load and preprocess the data
    X_train, X_val, X_test, y_train, y_val, y_test, tokenizer, label_encoder, max_length = load_and_preprocess_data('data/encrypted_dataset.csv')

    # Build the model
    vocab_size = len(tokenizer.word_index)
    num_classes = len(label_encoder.classes_)
    model = build_model(vocab_size, max_length, num_classes)

    # Train the model
    history = model.fit(X_train, y_train, epochs=10, validation_data=(X_val, y_val))

    # Plot the history
    plot_history(history)

    # Evaluate the model
    test_loss, test_accuracy = model.evaluate(X_test, y_test)
    print(f"Test Accuracy: {test_accuracy:.4f}")
