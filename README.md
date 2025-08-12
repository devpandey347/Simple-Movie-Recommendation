# Simple Movie Recommendation

Welcome to the **Simple Movie Recommendation** system!  
This project is a beginner-friendly, easy-to-use movie recommender built with Python. It demonstrates the basics of building a recommendation engine using pandas and cosine similarity.

## Features

- **User-friendly Recommendation:** Enter your favorite movie and get similar movie recommendations.
- **Content-based Filtering:** Uses movie features (like genres, plot descriptions, etc.) to suggest similar movies.
- **Fast and Simple:** Lightweight, fast, and easy to understand for new learners.

## How It Works

1. **Load Movie Data:** The system loads a dataset of movies with relevant features.
2. **Feature Extraction:** It processes features such as plot, genre, and keywords.
3. **Similarity Calculation:** Uses cosine similarity to compare the selected movie with others.
4. **Recommendation:** Returns a ranked list of the most similar movies.

## Setup

1. **Clone the repository:**
    ```bash
    git clone https://github.com/devpandey347/Simple-Movie-Recommendation.git
    cd Simple-Movie-Recommendation
    ```

2. **Install dependencies:**
    ```bash
    pip install pandas scikit-learn
    ```

3. **Run the recommender:**
    ```bash
    python main.py
    ```

## Example Usage

```python
Enter a movie name: Toy Story
Recommended movies:
- Toy Story 2
- Monsters, Inc.
- Finding Nemo
- A Bug's Life
- Cars
```

## File Structure

- `main.py` — Main script to run the recommendation system.
- `movies.csv` — Movie dataset containing movie features.
- `README.md` — Project documentation.

## Contributing

Feel free to fork this repo and submit pull requests for improvements, bug fixes, or additional features!

## License

This project is open source and available under the [MIT License](LICENSE).

---

If you have questions or suggestions, please open an issue or contact [devpandey347](https://github.com/devpandey347).
