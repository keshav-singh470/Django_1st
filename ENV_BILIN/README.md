## Setup
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

## API
GET/POST  /api/people/
GET/PUT/PATCH/DELETE  /api/people/<id>/