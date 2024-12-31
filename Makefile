init:
	docker-compose exec django python manage.py migrate
	docker-compose exec django python manage.py seed_subway_lines
