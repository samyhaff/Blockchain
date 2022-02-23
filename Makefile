start:
	./app.py -p 8000
update:
	pipenv update
build: update
	docker-compose build node
push: build
	docker-compose push node


