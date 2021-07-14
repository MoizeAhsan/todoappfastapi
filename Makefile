run-db:
	docker run --name todo_postgres -p 5432:5432 -e POSTGRES_PASSWORD=mysuperpassword -e POSTGRES_DB=todo -v ${PWD}/db_data:/var/lib/postgresql/data -d postgres
