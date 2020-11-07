from flask import Flask, render_template
app = Flask(__name__)


# Render homepage/index
@app.route('/')
def index():
    return render_template('index.html')

# Render meal-search
@app.route('/meal_search')
def meal_search():
    return render_template('meal-search.html')


# Render create-recipe
@app.route('/create_recipe', methods=["GET", "POST"])
def create_recipe():
    return render_template('create-recipe.html')


if __name__ == "__main__":
    app.run(debug = True)