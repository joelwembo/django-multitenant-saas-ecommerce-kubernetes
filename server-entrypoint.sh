python3 manage.py makemigrations

until python3 manage.py migrate
do
    echo "Waiting for db to be ready..."
    sleep 2
done


python3 manage.py collectstatic --noinput

python3 manage.py createsuperuser --noinput

# gunicorn fintechengine.wsgi --bind 0.0.0.0:8000 --workers 4 --threads 4
# for debug
python3 manage.py runserver 0.0.0.0:8000