from flask import Flask, request, jsonify
import os
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = (
    f"sqlite:///{os.path.join(basedir, 'app.db.sqlite')}"
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
class Recipe(db.Model):
    __tablename__ = "recipes"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    ingredients = db.Column(db.String)
    steps = db.Column(db.String)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "ingredients": self.ingredients,
            "steps": self.steps,
        }

@app.route("/api/v1/recipes", methods=["GET"])
def get_recipes():
    recipe_name = request.args.get("name", type=str)
    stmt= db.select(Recipe)
    if recipe_name:
        stmt = stmt.where(Recipe.name == recipe_name)
    recipes = db.session.scalars(stmt).all()
    if not recipes:
        return jsonify({"success": False, "error": "Item not found"}), 404

    return jsonify({"success": True, "data": [r.to_dict() for r in recipes]}), 200

@app.route("/api/v1/recipes/names", methods=["GET"])
def get_all_recipes_names():
    stmt = db.select(Recipe)
    recipes = db.session.scalars(stmt).all()
    recipe_names = [recipe.name for recipe in recipes]

    if not recipe_names:
        return jsonify({"success": False, "error": "No recipes found"}), 404
    return jsonify({"success": True, "data": recipe_names}), 200

if __name__ == "__main__":
    app.run(debug=True)