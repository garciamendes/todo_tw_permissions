# Docker
run-docker:
	docker compose --env-file .env -f docker-compose.yml up -d

docker-down:
	docker compose -f docker-compose.yml down

# Django
runserver: run-docker
	./manage.py runserver 0.0.0.0:8000

migrate: run-docker
	./manage.py migrate

migrations: run-docker
	./manage.py makemigrations

test:
	./manage.py test

superuser:
	./manage.py createsuperuser

urls:
	./manage.py show_urls

shell:
	./manage.py shell_plus