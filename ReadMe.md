Install virtual env :
pip install virtualenv
virtualenv venv
source venv/bin/activate

Install All requirements 
pip install -r requirements.txt

Do database Mirgations using alembic:
follow below link for it 
https://mdhvkothari.medium.com/how-to-do-the-migration-in-fastapi-5c53d3880f12


Run Fast api app:
uvicorn index:app --reload


Then go to http://127.0.0.1:8000/docs to test the API