import numpy as np
from tensorflow.keras.preprocessing.sequence import pad_sequences

def predict_cipher_type(model, tokenizer, label_encoder, encrypted_text, max_length):
    # Preprocess the input text using the tokenizer
    text_seq = tokenizer.texts_to_sequences([encrypted_text])
    text_pad = pad_sequences(text_seq, maxlen=max_length, padding='post')

    # Predict the cipher type
    prediction = model.predict(text_pad)
    predicted_label = np.argmax(prediction, axis=1)

    # Decode the label to get the cipher type using label encoder
    cipher_type = label_encoder.inverse_transform(predicted_label)[0]

    return cipher_type

if __name__ == "__main__":
    from data_preprocessing import load_and_preprocess_data
    from model import build_model

    # Load and preprocess the data (needed to get tokenizer and label encoder)
    X_train, X_val, X_test, y_train, y_val, y_test, tokenizer, label_encoder, max_length = load_and_preprocess_data('data/encrypted_dataset.csv')

    # Build and load the model
    vocab_size = len(tokenizer.word_index)
    num_classes = len(label_encoder.classes_)
    model = build_model(vocab_size, max_length, num_classes)
    model.load_weights('model_weights.h5')  # Load pre-trained weights if available

    # Example prediction
    encrypted_text = input("Enter the encrypted text: ")
    cipher_type = predict_cipher_type(model, tokenizer, label_encoder, encrypted_text, max_length)
    print(f"Predicted Cipher Type: {cipher_type}")
