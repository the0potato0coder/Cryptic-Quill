# Cipher Type Detection

This project involves building a machine learning model to detect the type of cipher used in encrypted text. The model is trained using encrypted texts derived from Shakespeare's *Macbeth*, and can classify the type of cipher used in the encryption.

## Project Structure

```bash
Cipher-Type-Detection/
│
├── data/
│   ├── macbeth.txt               # Raw text from Shakespeare's Macbeth
│   ├── cipher_dataset.csv        # Generated dataset for training
│
├── src/
│   ├── data_preparation.py       # Script to generate the dataset
│   ├── model.py                  # Script to build and train the model
│   ├── predict.py                # Script to predict the cipher type
│   ├── playfair.py               # Implementation of the Playfair cipher
│
├── main.py                       # Main script to run the project
├── requirements.txt              # List of required Python packages
├── README.md                     # Project documentation
```

## Getting Started

### Prerequisites

- Python 3.x
- TensorFlow
- NumPy
- Pandas
- Scikit-learn

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/Cipher-Type-Detection.git
   cd Cipher-Type-Detection
   ```

2. **Install required packages:**

   Use the `requirements.txt` file to install the necessary packages:

   ```bash
   pip install -r requirements.txt
   ```

### Dataset Preparation

The dataset is generated from the raw text of Shakespeare's *Macbeth*, which is used to create examples of various ciphers. The dataset file `cipher_dataset.csv` is automatically generated when you run `main.py`.

### Running the Project

1. **Generate the dataset and train the model:**

   Run the `main.py` script to prepare the dataset, train the model, and evaluate its performance:

   ```bash
   python main.py
   ```

2. **Predict Cipher Type:**

   After the model is trained, you can use the `main.py` script to predict the cipher type of encrypted text. Enter the encrypted text when prompted, or type `'exit'` to quit.

### Files

- **`main.py`**: Main script to run the project, including dataset preparation, model training, and prediction.
- **`src/data_preparation.py`**: Script to create the dataset from the raw Macbeth text.
- **`src/model.py`**: Script to build and train the machine learning model.
- **`src/predict.py`**: Script to predict the cipher type based on the trained model.
- **`src/playfair.py`**: Implementation of the Playfair cipher algorithm.
- **`data/macbeth.txt`**: Raw text data from Shakespeare's Macbeth.
- **`data/cipher_dataset.csv`**: Generated dataset for model training.

### Notes

- The model uses encrypted text derived from Shakespeare's Macbeth and is trained to recognize different cipher types.
- Ensure that the `macbeth.txt` file is present in the `data` directory before running `main.py`.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Shakespeare's Macbeth for the raw text data.
- TensorFlow, NumPy, Pandas, and Scikit-learn for the machine learning framework and tools.
