help:
	@echo "run 'make dev' for development mode, or 'make prod' for production mode (requires installed Docker and running dockerd)"

prod:
	@sudo docker-compose up -d
	@sudo docker-compose run web python manage.py makemigrations
	@sudo docker-compose run web python manage.py migrate
