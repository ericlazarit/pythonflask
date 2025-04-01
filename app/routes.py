from flask import render_template, redirect, url_for, flash, current_app as app
from app.forms import RecipeForm
from app.models import Recipe
from app import db

# Route for the home page
def main():
    name = "carlos"
    return render_template("hello.html", name=name)

# Route to display user accounts (placeholder for future functionality)
@app.route("/accounts")
def users():
    return "My USER ACCOUNTS"

# Route for user login (dummy implementation for now)
@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():  # Check if form data is valid
        print(f"Here is the input from the user {form.username.data} and {form.password.data}")
        return redirect("/")  # Redirect to home on successful login
    else:
        print("MOOOO MOOO")  # Debugging message
    return render_template("login.html", form=form)

# Route to display all recipes
@app.route('/recipes')
def recipes():
    all_recipes = Recipe.query.all()  # Query all recipes from database
    return render_template('recipes.html', recipes=all_recipes)

# Route to create a new recipe
@app.route('/recipe/new', methods=['GET', 'POST'])
def new_recipe():
    form = RecipeForm()
    if form.validate_on_submit():  # Check if form data is valid
        recipe = Recipe(
            title=form.title.data,
            description=form.description.data,
            ingredients=form.ingredients.data,
            instructions=form.instructions.data
        )
        db.session.add(recipe)  # Add new recipe to database
        db.session.commit()  # Commit transaction
        flash('Recipe added successfully!', 'success')  # Flash success message
        return redirect(url_for('recipes'))  # Redirect to recipe list
    return render_template('recipe_form.html', form=form)

# Route to display a specific recipe by ID
@app.route('/recipe/<int:recipe_id>')
def recipe_detail(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)  # Get recipe or return 404
    return render_template('recipe_detail.html', recipe=recipe)

