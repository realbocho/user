from flask import Flask, render_template
import random

app = Flask(__name__)

# Sample texts in different categories
category_texts = {
    'category1': ['Text 1 for Category 1', 'Text 2 for Category 1', 'Text 3 for Category 1'],
    'category2': ['Text 1 for Category 2', 'Text 2 for Category 2', 'Text 3 for Category 2'],
    # Add more categories and texts as needed
}

@app.route('/')
def index():
    # Choose a random category
    category = random.choice(list(category_texts.keys()))
    # Choose three random texts from the selected category
    selected_texts = random.sample(category_texts[category], 3)
    return render_template('index.html', category=category, texts=selected_texts)

if __name__ == '__main__':
    app.run(debug=True)
