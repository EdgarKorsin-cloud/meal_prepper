Meal Prepper
A web application designed to plan, organize, and track weekly meals, recipes, and grocery lists.

Note: Embed a GIF of your web application interface in action or a screenshot of the dashboard.

🎯 Objective
A web utility built to streamline weekly meal planning, manage recipes, and automatically generate consolidated grocery lists, eliminating manual organization friction and simplifying home kitchen preparation.

✨ Key Features
Recipe & Ingredient Management: Structured relational database to store personal recipes, ingredient lists, and instructions.

Weekly Meal Planner: Intuitive web interface to schedule breakfasts, lunches, and dinners across the week.

Automated Grocery Lists: Dynamically aggregates and categorizes required ingredients from selected weekly meals into a unified shopping list.

🛠️ Tech Stack
Language: Python 3.10+

Frameworks & Libraries: Flask, SQLAlchemy, Jinja2

Frontend: HTML5, CSS3, Bootstrap, JavaScript

Architecture: Model-View-Controller (MVC) web application pattern using Flask blueprints and SQLite persistence.

🚀 Installation & Setup
To run this project locally, follow these steps:

Clone the repository:
git clone [https://github.com/EdgarKorsin-cloud/meal_prepper.git](https://github.com/EdgarKorsin-cloud/meal_prepper.git)

Navigate to the directory:
cd meal_prepper

Create a virtual environment:
python -m venv venv

Activate the virtual environment:

Windows: venv\Scripts\activate

Mac/Linux: source venv/bin/activate

Install required dependencies:
pip install -r requirements.txt

💻 Usage
To launch the application, run the following command from the root directory:
python app.py

(Once running, open your browser and navigate to [http://127.0.0.1:5000](http://127.0.0.1:5000). Use the dashboard to add your favorite recipes, assign them to your weekly schedule, and automatically generate your shopping list.)

🗺️ Roadmap & Issue Tracking
Development is tracked via GitHub Issues.
Upcoming milestones include:

Adding external API integration for automated nutritional data estimation.

Implementing user account authentication and recipe sharing capabilities.
