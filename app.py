from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Placeholder data for the templates
    featured_recipes = [{'name': 'Tomato Soup', 'description': 'A delicious tomato soup recipe.'},]
    latest_posts = [{'title': 'The Art of Baking', 'summary': 'Learn the secrets of perfect baking with our latest guide.'},]
    testimonials = [{'user': 'John Doe', 'comment': 'This app transformed my cooking!'}]
    
    return render_template('index.html', 
                           featured_recipes=featured_recipes,
                           latest_posts=latest_posts,
                           testimonials=testimonials)

if __name__ == '__main__':
    app.run(debug=True)