# Multilingual Story Generation and Speech System

A Django-based web application that generates stories from user input, translates them into multiple languages, and converts the generated story into speech output.

## Overview

This project allows users to:
- enter a keyword or prompt,
- generate a story using GPT-2,
- translate the generated story into Hindi or Telugu,
- display the story in the browser,
- convert the story into audio using gTTS,
- listen to the spoken version.

This project is designed for academic, demonstration, and portfolio purposes.

## Features

- Story generation using GPT-2
- Multilingual story output
- Hindi and Telugu translation
- Text-to-speech conversion
- Django-based web application
- SQLite database support
- Admin login flow

## Tech Stack

- Python
- Django
- Hugging Face Transformers
- GPT-2
- Googletrans
- gTTS
- playsound
- SQLite

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/badripraneeth/Major-Project-Multilingual-Story-Generation-and-Speech-System.git
cd Major-Project-Multilingual-Story-Generation-and-Speech-System
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it:

Windows:
```bash
venv\Scripts\activate
```

Linux/macOS:
```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install --upgrade pip
pip install Django==2.1.7
pip install transformers==4.30.2
pip install gTTS==2.2.2
pip install gTTS-token==1.1.4
pip install requests==2.28.1
pip install playsound==1.2.2
pip install numpy==1.21.6
pip install pandas==1.3.5
pip install torch==1.13.1
pip install torchvision==0.14.1
```

### 4. Apply database migrations

```bash
python manage.py migrate
```

## Run the Project

Start the development server:

```bash
python manage.py runserver
```

Then open:

```text
http://127.0.0.1:8000/
```

## Login Credentials

```text
Username: admin
Password: admin
```

## Project Structure

```text
Major-Project-Multilingual-Story-Generation-and-Speech-System/
├── manage.py
├── requirements.txt
├── db.sqlite3
├── story.py
├── Story/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── StoryApp/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   ├── migrations/
│   ├── static/
│   │   ├── default.css
│   │   ├── story.txt
│   │   └── images/
│   └── templates/
│       ├── GenerateStory.html
│       ├── index.html
│       ├── Output.html
│       ├── UserLogin.html
│       └── UserScreen.html
```

## Notes

- The first run may take time because GPT-2 is downloaded automatically.
- Internet access is required for translation and model loading.
- Some packages may need OS-specific installation depending on the system.

## Author

Badripraneeth
