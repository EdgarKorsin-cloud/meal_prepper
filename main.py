import tkinter
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from datetime import datetime

#DB setup
engine = create_engine('sqlite:///app.db.sqlite')
Base=declarative_base()

class Recipe(Base):
    __tablename__ = 'recipes'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    ingredients = Column(String)
    steps = Column(String)
Base.metadata.create_all(engine)

# Functions
def save_recipe(name,ingredients,steps):
    Session = sessionmaker(bind=engine)
    session = Session()
    new_recipe = Recipe(name=name,ingredients=ingredients,steps=steps)
    session.add(new_recipe)
    session.commit()

def passing_info_to_save():
    name=meal_name_entry.get()
    ingredients=meal_ingredient_entry.get()
    steps=list_of_steps_entry.get()
    save_recipe(name,ingredients,steps)

    meal_name_entry.delete(0, 'end')
    meal_ingredient_entry.delete(0, 'end')
    list_of_steps_entry.delete(0, 'end')
    meal_ingredient_quantity_entry.delete(0, 'end')
    meal_name_entry.focus_set()

    print("Recipe saved")

#UI, Labels, Entry boxes, buttons
window = tkinter.Tk()
window.title("Meal Prepper")
canvas_recipe = tkinter.Canvas(window, width=200, height=200) # Potential logo
canvas_recipe.grid(row=0, column=0)
meal_name_label = tkinter.Label(window, text="Meal Name:")
meal_name_label.grid(row=0, column=1)
meal_name_label.grid(row=1, column=0)
meal_name_entry = tkinter.Entry(window)
meal_name_entry.focus_set()
meal_name_entry.grid(row=1, column=1)
meal_ingredient_label = tkinter.Label(window, text="Meal Ingredients:")
meal_ingredient_label.grid(row=2, column=1)
meal_ingredient_entry = tkinter.Entry(window)
meal_ingredient_entry.grid(row=3, column=1)
meal_ingredient_quantity_label = tkinter.Label(window, text="Quantity:")
meal_ingredient_quantity_label.grid(row=2, column=2)
meal_ingredient_quantity_entry = tkinter.Entry(window)
meal_ingredient_quantity_entry.grid(row=3, column=2)
meal_ingredient_amount_label = tkinter.Label(window)
meal_ingredient_amount_label.grid(row=3, column=3)
add_ingredient_button = tkinter.Button(text="add ingredient")
add_ingredient_button.grid(row=3, column=4)
# to be called when there are at least two ingredients
remove_ingredient_button = tkinter.Button(text="remove ingredient")
steps_label = tkinter.Label(window, text="STEPS")
steps_label.grid(row=4, column=1,columnspan=2)
list_of_steps = tkinter.Label(window, text="Steps:")
list_of_steps.grid(row=5, column=0)
list_of_steps_entry = tkinter.Entry(window)
list_of_steps_entry.grid(row=5, column=1)
add_steps_button = tkinter.Button(text="add step")
add_steps_button.grid(row=5, column=2) # Must add another entry box below to add a new step
# to be called when there are at least two steps
remove_steps_button = tkinter.Button(text="remove step")
# saves to sqldb
save_recipe_button = tkinter.Button(text="SAVE RECIPE",command=passing_info_to_save)
save_recipe_button.grid(row=6, column=1,columnspan=2)

window.mainloop()