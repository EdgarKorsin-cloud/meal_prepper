import tkinter
from tkinter import ttk
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime

#DB setup
engine = create_engine('sqlite:///app.db.sqlite')
Base=declarative_base()
# variables
next_row = 2
ingredients_rows = []
steps_rows = []
ingredient_type_options = ["mg","g","kg", "oz","ml","ml","lbs"]

class Recipe(Base):
    __tablename__ = 'recipes'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    ingredients = Column(String)
    steps = Column(String)
Base.metadata.create_all(engine)

# Functions
def add_row(row_type):
    global next_row

    if row_type == "ingredient":
        new_ingredient_entry = tkinter.Entry(middle_frame_left)
        new_ingredient_entry.grid(row=next_row, column=1, padx=10, pady=10)

        new_quantity_entry = tkinter.Entry(middle_frame_left)
        new_quantity_entry.grid(row=next_row, column=2, padx=10, pady=10)
        new_meal_ingredient_type = ttk.Combobox(middle_frame_left, values=ingredient_type_options,state="readonly")
        new_meal_ingredient_type.grid(row=next_row, column=3, padx=10, pady=10)

        add_ingredient_button.grid(row=next_row, column=4)

        ingredients_rows.append((new_ingredient_entry, new_quantity_entry))

    elif row_type == "step":
        new_step_entry = tkinter.Entry(bottom_frame_left)
        new_step_entry.config(width=40)
        new_step_entry.grid(row=next_row, column=1, padx=10, pady=10)

        add_steps_button.grid(row=next_row, column=4)
        save_recipe_button.grid(row=next_row + 1, column=1)

        steps_rows.append(new_step_entry)

    next_row += 1
def remove_row(row_type):
    global next_row
    if row_type == "ingredient":
        pass


def save_recipe(name,ingredients,steps):
    Session = sessionmaker(bind=engine)
    session = Session()
    new_recipe = Recipe(name=name,ingredients=ingredients,steps=steps)
    session.add(new_recipe)
    session.commit()

def passing_info_to_save():
    name=meal_name_entry.get()
    ingredients_list = []
    for i, (ing_entry, qty_entry) in enumerate(ingredients_rows, 1):
        ing_name = ing_entry.get()
        qty = qty_entry.get()
        if ing_name:
            ingredients_list.append(f"{i}. {ing_name} ({qty})")

    ingredients_string = "\n".join(ingredients_list)

    steps_list = []
    for i, step_entry in enumerate(steps_rows, 1):
        step_text = step_entry.get()
        if step_text:
            steps_list.append(f"{i}. {step_text}")

    steps_string = "\n".join(steps_list)

    save_recipe(name, ingredients_string, steps_string)

    for widget in window.winfo_children():
        for child in widget.winfo_children():
            if isinstance(child, tkinter.Entry):
                child.delete(0, tkinter.END)

    meal_name_entry.focus_set()

    print("Recipe saved")

#UI, Labels, Entry boxes, buttons for entering recipes
window = tkinter.Tk()
window.title("Meal Prepper")
window.geometry("600x600")

top_frame_left = tkinter.Frame(window)
top_frame_left.grid(row=0, column=0, padx=10, pady=10)
middle_frame_left = tkinter.Frame(window)
middle_frame_left.grid(row=1, column=0, padx=10, pady=10)
bottom_frame_left = tkinter.Frame(window)
bottom_frame_left.grid(row=2, column=0, padx=10, pady=10)

meal_name_label = tkinter.Label(top_frame_left, text="Meal Name:",anchor="w")
meal_name_label.grid(row=0, column=0,padx=10,pady=10)
meal_name_entry = tkinter.Entry(top_frame_left)
meal_name_entry.focus_set()
meal_name_entry.grid(row=0, column=1,padx=10,pady=10,sticky="w")

meal_ingredient_label = tkinter.Label(middle_frame_left, text="Meal Ingredients:",anchor="w")
meal_ingredient_label.grid(row=0, column=1)
meal_ingredient_entry = tkinter.Entry(middle_frame_left)
meal_ingredient_entry.grid(row=1, column=1,sticky="w")
meal_ingredient_quantity_label = tkinter.Label(middle_frame_left, text="Quantity:",anchor="w")
meal_ingredient_quantity_label.grid(row=0, column=2)
meal_ingredient_quantity_entry = tkinter.Entry(middle_frame_left)
meal_ingredient_quantity_entry.grid(row=1, column=2,sticky="w")
ingredient_type = tkinter.Label(middle_frame_left, text="Ingredient Type:",anchor="w")
ingredient_type.grid(row=0, column=3)
meal_ingredient_entry_type = ttk.Combobox(middle_frame_left, values=ingredients_rows,state="readonly")
meal_ingredient_entry_type.grid(row=1, column=3,sticky="w")
ingredients_rows.append((meal_ingredient_entry, meal_ingredient_quantity_entry))

add_ingredient_button = tkinter.Button(middle_frame_left, text="add ingredient", command=lambda: add_row("ingredient"))
add_ingredient_button.grid(row=1, column=4)


### to be called when there are at least two ingredients remove_ingredient_button = tkinter.Button(text="remove ingredient")
steps_label = tkinter.Label(bottom_frame_left, text="STEPS",anchor="w")
steps_label.grid(row=0, column=1,columnspan=2)
list_of_steps = tkinter.Label(bottom_frame_left, text="Steps:",anchor="w")
list_of_steps.grid(row=1, column=0)
list_of_steps_entry = tkinter.Entry(bottom_frame_left)
list_of_steps_entry.grid(row=1, column=1, columnspan=3,sticky="w")
list_of_steps_entry.config(width=40)
add_steps_button = tkinter.Button(bottom_frame_left, text="add step", command=lambda: add_row("step"))
add_steps_button.grid(row=1, column=4)
steps_rows.append(list_of_steps_entry)
# to be called when there are at least two steps
remove_steps_button = tkinter.Button(text="remove step")

save_recipe_button = tkinter.Button(bottom_frame_left, text="SAVE RECIPE", command=passing_info_to_save)
save_recipe_button.grid(row=2, column=1,)


#UI for showing recipe
center_frame=tkinter.Frame(window)
center_frame.grid(row=0, column=1, padx=10, pady=10)
recipe_name_label = tkinter.Label(center_frame, text="Recipe for ",font=("Serif", 24),anchor="w")
recipe_name_label.grid(row=0, column=1)



window.mainloop()