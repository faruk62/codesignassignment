# Palette Project

The Palette Project is a web-based application that allows users to manage, view, and favorite color palettes. Built with Django and the Django Rest Framework, it provides a robust backend API to cater to all palette-related operations.

## Installation

1. Ensure you have the project files on your local machine.
2. Navigate to the project directory:

   ```
   cd codesignassignment
   ```
3. Set up a virtual environment:

   ```
   python -m venv venv
   ```
4. Activate the virtual environment:

   - On macOS and Linux:
     ```
     source venv/bin/activate
     ```
   - On Windows:
     ```
     .\venv\Scripts\activate
     ```
5. Install the required packages:

   ```
   pip install -r requirements.txt
   ```

## Running the Project

1. Apply migrations to set up your database schema:

   ```
   python manage.py migrate
   ```
2. Run the server:

   ```
   python manage.py runserver
   ```
3. Open a browser and navigate to `http://127.0.0.1:8000/` to access the project.

## API Endpoints

### Palettes

- **List & Create**: `/palettes/`
- **Retrieve, Update, & Delete**: `/palettes/{palette_id}/`

### Favorites

- **Add to Favorites**: `/favorites/{palette_id}/add_to_favorites/`
- **List User's Favorites**: `/favorites/`
- **Remove from Favorites**: `/favorites/{favorite_id}/` (Use DELETE method)

### Palette Revisions

- **List Revisions for a Palette**: `/palette-revisions/?palette_id={palette_id}`

### Django Admin Panel Credential

* username: faruk
* password: 1234

## Authentication & JWT Tokens

The API uses JWT (JSON Web Tokens) for authentication:

1. **Obtain a Token**:

   - Endpoint: `/api/token/`
   - Method: `POST`
   - Data:
     ```json
     {
       "username": "faruk",
       "password": 1234
     }
     ```
   - This will return a `refresh` and `access` token.
2. **Using the Token**:

   - For endpoints that require authentication, include the token in your request headers:
     ```
     Authorization: Bearer YOUR_ACCESS_TOKEN
     ```
3. **Refreshing a Token**:

   - Endpoint: `/api/token/refresh/`
   - Method: `POST`
   - Data:
     ```json
     {
       "refresh": "YOUR_REFRESH_TOKEN"
     }
     ```

## Features

- **User Management**: Register, login, and manage user profiles.
- **Palettes**: Create, update, delete, and view color palettes.
- **Favorites**: Users can mark palettes as favorites.
- **Revision History**: Track changes to palettes over time.
- **Public & Private Palettes**: Control the visibility of your palettes.
