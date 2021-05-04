import os
from dotenv import load_dotenv

dirname = os.path.dirname(__file__)

try:
    load_dotenv(dotenv_path = os.path.join(dirname, '..', '.env'))
except FileNotFoundError:
    pass

DATABASE_FILENAME = os.getenv(('DATABASE_FILENAME') or  "database.sqlite3")
DATABASE_FILE_PATH = os.path.join(dirname, '..', 'data', DATABASE_FILENAME)

COURSES_FILENAME = os.getenv(('COURSES_FILENAME') or "courses.csv")
COURSES_FILE_PATH = os.path.join(dirname, '..', 'data', COURSES_FILENAME)

NOTES_FILENAME = os.getenv(('NOTES_FILENAME') or "notes.csv")
NOTES_FILE_PATH = os.path.join(dirname, '..', 'data', NOTES_FILENAME)
