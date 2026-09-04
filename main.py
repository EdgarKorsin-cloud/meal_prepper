import tkinter

window = tkinter.Tk()
window.title("Meal Prepper")

#UI, Labels, Entry boxes, buttons
canvas_recipe = tkinter.Canvas(window, width=200, height=200) # Potential logo
canvas_recipe.grid(row=0, column=0)
meal_name_label = tkinter.Label(window, text="Meal Name:")
meal_name_label.grid(row=1, column=0)
meal_name_entry = tkinter.Entry(window)
meal_name_entry.grid(row=1, column=1)
meal_ingredient_label = tkinter.Label(window, text="Meal Ingredients:")
meal_ingredient_label.grid(row=2, column=0)
meal_ingredient_entry = tkinter.Entry(window)
meal_ingredient_entry.grid(row=2, column=1)
meal_ingredient_quantity_entry = tkinter.Entry(window)
meal_ingredient_quantity_entry.grid(row=2, column=2)
meal_ingredient_amount_label = tkinter.Label(window)
meal_ingredient_amount_label.grid(row=2, column=3)
add_ingredient_button = tkinter.Button(text="add ingredient")
add_ingredient_button.grid(row=2, column=4)
# to be called when there are at least two ingredients
remove_ingredient_button = tkinter.Button(text="remove ingredient")
steps_label = tkinter.Label(window, text="STEPS")
steps_label.grid(row=3, column=1,columnspan=2)
list_of_steps = tkinter.Label(window, text="Steps:")
list_of_steps.grid(row=4, column=0)
list_of_steps_entry = tkinter.Entry(window)
list_of_steps_entry.grid(row=4, column=1)
add_steps_button = tkinter.Button(text="add step")
add_steps_button.grid(row=4, column=2) # Must add another entry box below to add a new step
# to be called when there are at least two steps
remove_steps_button = tkinter.Button(text="remove step")

save_recipe_button = tkinter.Button(text="SAVE RECIPE")
save_recipe_button.grid(row=5, column=1,columnspan=2)

window.mainloop()