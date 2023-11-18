
# Learning Blog

A Django-powered minimalist blog for users that don't like complicated designs.


## Table of Contents

- [Features](#Features)
- [Installation](#installation)
## Features

- User Registration: Users can create an account to start creating and managing their blog posts.
- Blog Post Management: Create, edit, delete, and classify posts as either published or drafts.
- Tagging System: Easily organize and filter posts by tags.


## Environment Variables

To run this project, you will need to add the following environment variables to your .env file.

- `POSTGRES_URL`: external URL connection to your database.
- `DJANGO_SECRET_KEY` (optional).


## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/soraia653/Learning-Blog.git
    cd learning-blog
    ```

2. Run the `build_staticfiles.sh` script to set up the project:

    ```bash
    ./build_staticfiles.sh
    ```

3. Create a superuser account (optional):

    ```bash
    python manage.py createsuperuser
    ```

6. Run the development server:

    ```bash
    python manage.py runserver
    ```

The Learning Blog should now be accessible at http://localhost:8000/.