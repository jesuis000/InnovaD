# Django Phonebook App

This is a simple phonebook application built with Django.

## Installation

1. Clone this repository: `git clone https://github.com/yourusername/phonebook.git`
2. Navigate to the project directory: `cd phonebook`
3. Install the requirements: `pip install -r requirements.txt`
4. Apply the migrations: `python manage.py migrate`
5. Run the server: `python manage.py runserver`

## Usage

After running the server, you can access the application at `http://localhost:8000`.

## Contributing

If you want to contribute to this project, please fork this repository, make your changes, and open a pull request.

## Credits

This project was created by Your Name.

## ERD

The application has two main models:

- Contact:
  - id (automatically added by Django)
  - name

- PhoneNumber:
  - id (automatically added by Django)
  - contact_id (a foreign key to the Contact model)
  - number

Each Contact can have multiple associated PhoneNumbers through the foreign key relationship.
