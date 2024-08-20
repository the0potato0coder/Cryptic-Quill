import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

def load_and_preprocess_data(file_path):
    # Load the dataset
    df = pd.read_csv(file_path)

    # Preprocess the text
    X = df['Encrypted_Text'].values
    y = df['Cipher_Type'].values

    # Tokenize the text
    tokenizer = Tokenizer(char_level=True)  # Char-level tokenization
    tokenizer.fit_on_texts(X)
    X_seq = tokenizer.texts_to_sequences(X)

    # Pad sequences to ensure uniform input size
    max_length = max(len(x) for x in X_seq)
    X_pad = pad_sequences(X_seq, maxlen=max_length, padding='post')

    # Encode labels
    label_encoder = LabelEncoder()
    y_encoded = label_encoder.fit_transform(y)

    # Split the data into train, validation, and test sets
    X_train, X_temp, y_train, y_temp = train_test_split(X_pad, y_encoded, test_size=0.3, random_state=42)
    X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)

    return X_train, X_val, X_test, y_train, y_val, y_test, tokenizer, label_encoder, max_length
