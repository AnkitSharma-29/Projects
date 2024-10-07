
# Language Detection Model : Machine Learning & NLP

This repository contains a simple **Language Detection Model** built using **Machine Learning (ML)** and **Natural Language Processing (NLP)** techniques. The model utilizes the **Multinomial Naive Bayes** algorithm and the **Bag of Words (BoW)** model to classify a given text into its respective language. The project is developed and run in **Google Colab**.

## Dataset

The dataset used for this project is stored in a CSV file (`language.csv`) that contains two columns:
- **Text**: The actual text content.
- **Language**: The corresponding language of the text.

## Installation

To run this project in **Google Colab**, follow these steps:

1. Upload the dataset (`language.csv`) to your Google Drive.
2. Mount Google Drive to access the dataset using the following code:

    ```python
    from google.colab import drive
    drive.mount('/content/drive')
    ```

3. Install necessary libraries if not already available:

    ```bash
    !pip install numpy pandas scikit-learn
    ```

4. Read the dataset:

    ```python
    data = pd.read_csv('/content/language.csv')
    ```

## Model Training

The model utilizes the **Multinomial Naive Bayes** algorithm. Here's a brief outline of the steps to train the model:

1. **Data Preprocessing**:
   - The text data is vectorized using the **CountVectorizer** from `sklearn.feature_extraction.text`.
   - The dataset is split into training and testing sets using `train_test_split` from `sklearn.model_selection`.

2. **Model Training**:
   - The **Multinomial Naive Bayes** model is trained on the vectorized text data using the training set.
   - The model's accuracy is evaluated on the training data.

3. **Prediction**:
   - The model can predict the language of a given text by transforming it into a format understandable by the model and outputting the language.

## Usage

After training the model, you can enter any text to detect its language:

```python
user = input('Enter a text: ')
data = cv.transform([user]).toarray()
output = model.predict(data)
print(output)
```

## Example

```bash
Enter a text: "Hola, ¿cómo estás?"
['Spanish']
```

## Dependencies

- **Python** (3.x)
- **NumPy**
- **Pandas**
- **scikit-learn**

## License

This project is licensed under the MIT License.
