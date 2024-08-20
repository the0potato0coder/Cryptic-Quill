import os
from src.create_dataset import create_encrypted_dataset
from src.data_preprocessing import load_and_preprocess_data
from src.model import build_model, plot_history
from src.predict import predict_cipher_type


def main():
    # Step 1: Create the dataset
    if not os.path.exists('data/encrypted_dataset.csv'):
        print("Creating dataset...")
        create_encrypted_dataset('data/plaintext.txt')
        print("Dataset created successfully!")

    # Step 2: Load and preprocess the data
    print("Loading and preprocessing data...")
    X_train, X_val, X_test, y_train, y_val, y_test, tokenizer, label_encoder, max_length = load_and_preprocess_data(
        'data/encrypted_dataset.csv')

    # Step 3: Build and train the model
    print("Building and training the model...")
    vocab_size = len(tokenizer.word_index)
    num_classes = len(label_encoder.classes_)
    model = build_model(vocab_size, max_length, num_classes)
    history = model.fit(X_train, y_train, epochs=10, validation_data=(X_val, y_val))

    # Plot training history
    plot_history(history)

    # Save the model weights
    model.save_weights('model_weights.h5')

    # Step 4: Evaluate the model
    print("Evaluating the model...")
    test_loss, test_accuracy = model.evaluate(X_test, y_test)
    print(f"Test Accuracy: {test_accuracy:.4f}")

    # Step 5: Make predictions
    while True:
        encrypted_text = input("Enter the encrypted text to predict the cipher type (or 'exit' to quit): ")
        if encrypted_text.lower() == 'exit':
            break
        cipher_type = predict_cipher_type(model, tokenizer, label_encoder, encrypted_text, max_length)
        print(f"Predicted Cipher Type: {cipher_type}")


if __name__ == "__main__":
    main()
