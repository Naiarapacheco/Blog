docker-compose exec web python manage.py startapp content

docker-compose exec web python manage.py makemigrations

docker-compose exec web python manage.py migrate

docker-compose exec web python manage.py createsuperuser

-----------------------------------------------------------

pip install django-ckeditor

pip freeze > requirements.txt

    settings:
        'ckeditor',
        'ckeditor_uploader',

        # Static files (CSS, JavaScript, Images)
        MEDIA_URL = '/media/'
        MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
        STATIC_URL = '/static/'

        CKEDITOR_UPLOAD_PATH = "uploads/"
        CKEDITOR_BASEPATH = "/static/ckeditor/ckeditor/"

                            # Default primary key field type
                            DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

        # Optional CKEditor settings
        CKEDITOR_CONFIGS = {
            'default': {
                'toolbar': 'full',
                'height': 300,
                'width': 300,
            },
        }

    .................................................................

    urls:
        path('ckeditor/', include('ckeditor_uploader.urls')),  # Adiciona URLs do CKEditor
        + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    ..................................................................

    Comando para coletar os arquivos estáticos do CKEditor:
        docker-compose exec web ./manage.py collectstatic

    ..................................................................

    Reinicie os Containers docker
        docker-compose down
        docker-compose up --BigAutoField

    ...................................................................

     docker-compose up -d  (update)

     ------------------------------------------------------------------

     DATABASES
        Fazer ás configs do db

        pip install psycopg2-binary --upgrade    (psycopg2 - especifico para o Postgres)
        pip freeze > requirements.txt

        docker-compose build
        docker-compose up -d
        docker-compose exec web python manage.py migrate
        docker-compose exec db psql -U username -d namedb

    -------------------------------------------------------------------





