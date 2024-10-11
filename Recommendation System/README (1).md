
# Movie Recommendation System

This project is a **Movie Recommendation System** implemented in Python using popular data manipulation libraries like **Pandas**. The system recommends movies based on user ratings and movie similarities. The dataset used includes user movie ratings and the system calculates movie similarity using collaborative filtering.

## Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Dataset](#dataset)
6. [Project Structure](#project-structure)
7. [Contributing](#contributing)
8. [License](#license)

## Introduction

The goal of this project is to build a recommendation system that suggests movies to users based on collaborative filtering. The system uses movie ratings provided by users and recommends movies that are similar to the ones a user has rated highly.

## Features

- **Movie Filtering:** Recommend movies based on users' past ratings.
- **Rating Count:** Count the number of ratings per movie.
- **Collaborative Filtering:** Use user interactions (movie ratings) to generate recommendations.
- **Dataset Handling:** Efficient handling of the movie and rating data using **Pandas**.

## Installation

1. **Clone the repository:**

    \`\`\`bash
    git clone <repository-url>
    cd <repository-directory>
    \`\`\`

2. **Install the required dependencies:**

    Ensure you have Python 3.x installed, then install the required packages:

    \`\`\`bash
    pip install -r requirements.txt
    \`\`\`

3. **Dependencies:**
    - `pandas`
    - `numpy`
    - `jupyter`

4. **Dataset:**

    Ensure the required movie dataset and user ratings are placed in the correct directory (see [Dataset](#dataset)).

## Usage

1. **Run the Jupyter Notebook:**

    To run the recommendation system, open the notebook file:

    \`\`\`bash
    jupyter notebook Recommendation_System.ipynb
    \`\`\`

2. **Load and Preprocess the Data:**

    In the notebook, you will find code to load and preprocess the movie dataset and user ratings data.

3. **Generate Recommendations:**

    The system will generate recommendations for a given movie using collaborative filtering. Here's a sample workflow in the notebook:

    \`\`\`python
    # Example of counting ratings for a given movie
    movie_id = 1  # Replace with the movieId you want to check
    rat_count = ratings_df.loc[ratings_df['movieId'] == movie_id].count().iloc[0]
    \`\`\`

4. **Exploration and Customization:**

    You can explore the notebook to test various functionalities and customize the recommendation algorithm according to your requirements.

## Dataset

The dataset used in this project consists of:

- **Movies Metadata:** Contains information about movie IDs and titles.
- **User Ratings:** Contains user ratings of movies.

### Sample Format:

- **movies.csv:**
    | movieId | title               |
    |---------|---------------------|
    | 1       | Toy Story (1995)     |
    | 2       | Jumanji (1995)       |

- **ratings.csv:**
    | userId | movieId | rating | timestamp |
    |--------|---------|--------|-----------|
    | 1      | 1       | 4.0    | 964982703 |
    | 1      | 3       | 4.0    | 964981247 |

You can download a sample dataset from [MovieLens](https://grouplens.org/datasets/movielens/) if needed.

## Project Structure

\`\`\`
Recommendation_System/
│
├── Recommendation_System.ipynb    # Jupyter notebook implementing the recommendation system
├── movies.csv                     # Movie metadata (sample)
├── ratings.csv                    # User ratings (sample)
├── README.md                      # Project documentation
└── requirements.txt               # Python dependencies
\`\`\`

## Contributing

Contributions are welcome! If you'd like to contribute, please fork the repository and make changes as you'd like. Pull requests are warmly welcome.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
