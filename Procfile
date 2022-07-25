web: gunicorn q_music_site.wsgi
--log-file - --log-level debug
python manage.py collectstatic --noinput
manage.py migrate