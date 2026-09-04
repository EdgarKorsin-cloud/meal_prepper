import tkinter
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from datetime import datetime

#DB setup
engine = create_engine('sqlite:///app.db.sqlite')
Base=declarative_base()
# variables
next_row = 4
ingredients_rows = []
steps_rows = []

class Recipe(Base):
    __tablename__ = 'recipes'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    ingredients = Column(String)
    steps = Column(String)
Base.metadata.create_all(engine)

# Functions
def add_ingredient_row():
    global next_row

    new_ingredient_entry = tkinter.Entry(middle_frame)
    new_ingredient_entry.grid(row=next_row, column=1,padx=10,pady=10)
    new_quantity_entry = tkinter.Entry(middle_frame)
    new_quantity_entry.grid(row=next_row, column=2,padx=10,pady=10)

    add_ingredient_button.grid(row = next_row, column = 4)
    ingredients_rows.append((new_ingredient_entry, new_ingredient_entry))

    steps_label.grid(row=next_row +1, column=1, columnspan=2)
    list_of_steps.grid(row=next_row +2, column=0)
    list_of_steps_entry.grid(row=next_row +2, column=1)
    add_steps_button.grid(row=next_row +2, column=2)
    save_recipe_button.grid(row=6, column=1, columnspan=2)

    next_row += 1

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

# canvas_recipe = tkinter.Canvas(window, width=200, height=200) # Potential logo
# canvas_recipe.grid(row=0, column=0)

top_frame = tkinter.Frame(window)
top_frame.pack(pady=10)
middle_frame = tkinter.Frame(window)
middle_frame.pack(pady=20)
bottom_frame = tkinter.Frame(window)
bottom_frame.pack(pady=30)

meal_name_label = tkinter.Label(top_frame, text="Meal Name:")
meal_name_label.grid(row=0, column=0,padx=10,pady=10)
meal_name_entry = tkinter.Entry(top_frame)
meal_name_entry.focus_set()
meal_name_entry.grid(row=0, column=1,padx=10,pady=10)

meal_ingredient_label = tkinter.Label(middle_frame, text="Meal Ingredients:")
meal_ingredient_label.grid(row=0, column=1)
meal_ingredient_entry = tkinter.Entry(middle_frame)
meal_ingredient_entry.grid(row=1, column=1)
meal_ingredient_quantity_label = tkinter.Label(middle_frame, text="Quantity:")
meal_ingredient_quantity_label.grid(row=0, column=2)
meal_ingredient_quantity_entry = tkinter.Entry(middle_frame)
meal_ingredient_quantity_entry.grid(row=1, column=2)
add_ingredient_button = tkinter.Button(middle_frame,text="add ingredient",command=add_ingredient_row)
add_ingredient_button.grid(row=1, column=4)
ingredients_rows.append((meal_ingredient_entry, meal_ingredient_quantity_entry))

# to be called when there are at least two ingredients remove_ingredient_button = tkinter.Button(text="remove ingredient")
steps_label = tkinter.Label(bottom_frame, text="STEPS")
steps_label.grid(row=0, column=1,columnspan=2)
list_of_steps = tkinter.Label(bottom_frame, text="Steps:")
list_of_steps.grid(row=1, column=0)
list_of_steps_entry = tkinter.Entry(bottom_frame)
list_of_steps_entry.grid(row=1, column=1, columnspan=3)
list_of_steps_entry.config(width=40)
add_steps_button = tkinter.Button(bottom_frame,text="add step")
add_steps_button.grid(row=1, column=4) # Must add another entry box below to add a new step
# to be called when there are at least two steps
remove_steps_button = tkinter.Button(text="remove step")
# saves to sqldb
save_recipe_button = tkinter.Button(bottom_frame,text="SAVE RECIPE",command=passing_info_to_save)
save_recipe_button.grid(row=2, column=1,)

window.mainloop()