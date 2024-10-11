# Movie Recommendation System

This repository contains a Movie Recommendation System implemented in Python using collaborative filtering techniques. The system utilizes user ratings to suggest movies to users based on their preferences.

## Requirements

To run this code in Google Colab, you need to install the following packages:

- `pandas`
- `numpy`
- `scikit-learn`
- `matplotlib`

## Getting Started

1. **Open Google Colab**

   Go to [Google Colab](https://colab.research.google.com/).

2. **Create a New Notebook**

   Click on `File` > `New Notebook`.

3. **Install Required Packages**

   In the first cell, install the necessary packages by running:

   ```python
   !pip install pandas numpy scikit-learn matplotlib
   ```

4. **Upload the Dataset**

   You will need to upload the dataset files used in the recommendation system. Use the following code to upload files:

   ```python
   from google.colab import files
   uploaded = files.upload()
   ```

   Select the dataset files from your local machine to upload them.

5. **Copy and Paste the Code**

   Copy the code from the `code.py` file and paste it into a new cell in your Colab notebook.

6. **Run the Code**

   Execute each cell step by step by clicking the "Run" button or pressing `Shift + Enter`.

## Usage

Once you have run the code, you can interact with the recommendation system by providing user ratings and receiving movie suggestions based on the collaborative filtering algorithm.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
