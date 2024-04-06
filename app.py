from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Placeholder data for the home page templates
    featured_recipes = [{'name': 'Tomato Soup', 'description': 'A delicious tomato soup recipe.'},]
    latest_posts = [{'title': 'The Art of Baking', 'summary': 'Learn the secrets of perfect baking with our latest guide.'},]
    testimonials = [{'user': 'John Doe', 'comment': 'This app transformed my cooking!'}]
    
    # Here we fetch more recipes from a database.
    # For now, using placeholder data

    return render_template('index.html',
                           featured_recipes=featured_recipes,
                           latest_posts=latest_posts,
                           testimonials=testimonials)

@app.route('/recipe')
def recipe():
    # Placeholder data for a single recipe
    ingredients = [
        '3/4 pound fresh asparagus, trimmed',
        '8 turkey breast cutlets (about 1 pound)',
        '1 tablespoon Dijon-mayonnaise blend',
        # ... additional ingredients ...
    ]
    instructions = """
    Step 1: Preheat your grill to medium heat.
    Step 2: Grill asparagus and turkey until cooked.
    Step 3: Spread Dijon-mayonnaise blend on turkey cutlets.
    Step 4: Wrap each cutlet with ham and cheese, and secure with a toothpick.
    Step 5: Grill until cheese is melted.
    Step 6: Serve with your choice of sauce.
    """
    # This data could also come from a database in a more dynamic application
    return render_template('recipe.html', ingredients=ingredients, instructions=instructions)

if __name__ == '__main__':
    app.run(debug=True)