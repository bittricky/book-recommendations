# Book Recommendations

A Flask-based web application that provides book recommendations using the Open Library API. The application features a modern UI built with Tailwind CSS, allowing users to search for books and get recommendations.

## Features

- Search for books by title, author, or keywords
- Get random book recommendations
- View book details including cover images, authors, and publication years
- Responsive design that works on different screen sizes
- Custom 404 error page

## Screenshots

(Add screenshots here)

## Tech Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML, JavaScript, Tailwind CSS
- **API**: Open Library API
- **Package Management**: npm (for Tailwind CSS)

## Prerequisites

- Python 3.7+
- pip (Python package manager)
- Node.js and npm (for Tailwind CSS)

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/bittricky/book-recommendations.git
cd book-recommendations
```

### 2. Set up Python virtual environment

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

### 3. Install Python dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up Tailwind CSS

```bash
# Install npm dependencies
npm install

# Build the CSS
npm run build:css
```

### 5. Run the application

```bash
# Set Flask to development mode
# On Windows
set FLASK_ENV=development
# On macOS/Linux
export FLASK_ENV=development

# Run the application
python run.py
```

The application will be available at http://localhost:5000

## Development Environment Setup

### Frontend Development

For frontend development with hot-reloading of Tailwind CSS:

```bash
# Run Tailwind CSS in watch mode
npm run watch:css
```

This will automatically rebuild the CSS whenever you make changes to the Tailwind configuration or HTML files.

### Backend Development

For backend development, you can use Flask's debug mode which is enabled by default in the run.py file. This allows for automatic reloading of the server when Python files are changed.

## Project Structure

```
book-recommendations/
├── app/                    # Application package
│   ├── __init__.py         # Application initialization
│   ├── routes.py           # Route definitions
│   ├── services.py         # Service layer (API interactions)
│   ├── static/             # Static files
│   │   ├── scripts/        # JavaScript files
│   │   └── styles/         # CSS files
│   └── templates/          # HTML templates
├── venv/                   # Virtual environment (not in repository)
├── .gitignore              # Git ignore file
├── package.json            # npm package configuration
├── requirements.txt        # Python dependencies
├── run.py                  # Application entry point
└── tailwind.config.js      # Tailwind CSS configuration
```

## Acknowledgments

- [Open Library API](https://openlibrary.org/developers/api) for providing book data
- [Tailwind CSS](https://tailwindcss.com/) for the utility-first CSS framework
- [Flask](https://flask.palletsprojects.com/) for the web framework
