Step 1: Set Up the Environment
Clone the Repository:
git clone https://github.com/MammadSofiyev/Blog
Set Up a Virtual Environment:
python -m venv myblogenv
Activate the virtual environment:
On Windows:myblogenv\Scripts\activate
On macOS and Linux:source myblogenv/bin/activate
Step 2: Install Dependencies
Navigate to the Project Directory:
Where manage.py is located
Install Required Packages:
pip install -r requirements.txt
Step 3: Database Setup
Run Migrations:
python manage.py makemigrations
python manage.py migrate
Step 4: Run the Django Server
Start the Server:
python manage.py runserver
Step 5: Access the Blog Website
Access the Site:
Open a web browser and go to http://127.0.0.1:8000/ or http://localhost:8000/ to view the blog.

  
