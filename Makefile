.PHONY: help setup dependencies copy-envs test test-docker lint pre-commit run-local run-docker report clean migration-docker migration-local migrate-docker migrate-local requirements create-trigger-dev create-trigger-prod run-trigger-dev run-trigger-prod

PROJECT_NAME := gym-movement

help: ## Show help.
	@printf "A set of development commands.\n"
	@printf "\nUsage:\n"
	@printf "\t make \033[36m<commands>\033[0m\n"
	@printf "\nThe Commands are:\n\n"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\t\033[36m%-30s\033[0m %s\n", $$1, $$2}'

setup: ## Setup poetry environment
	poetry shell
	poetry install

copy-envs: ## Create secret file
	@cp -n .example.secret.toml .secret.toml

test: ## Run tests locally
	poetry run pytest --cov=src --color=yes tests/

test-docker: ## Run tests on docker instance
	poetry run docker-compose -f ./docker-compose-dev.yml run --service-ports --rm api bash -c "pytest --cov=src --color=yes -vvvv"

lint | pre-commit: ## Run the pre-commit config
	poetry run pre-commit run -a

run-local: ## Run server locally
	python main.py

run-docker: ## Run server on docker instance
	docker-compose -f ./docker-compose-dev.yml run --service-ports --rm api bash -c "python main.py"

report: test ## Create test report
	pytest --cov=$(API_CONTAINER_NAME) --color=yes tests/
	coverage report
	coverage html -d coverage_html

clean: ## Clean up
	@find ./ -name '*.pyc' -exec rm -f {} \;
	@find ./ -name 'Thumbs.db' -exec rm -f {} \;
	@find ./ -name '*~' -exec rm -f {} \;
	rm -rf .coverage
	rm -rf  coverage_html
	rm -rf .pytest_cache
	rm -rf .cache
	rm -rf build
	rm -rf dist
	rm -rf *.egg-info
	rm -rf htmlcov
	rm -rf .tox/
	rm -rf docs/_build
	rm -rf celerybeat-schedule
	rm -rf *.pyc
	rm -rf *__pycache__

migration-docker: ## Database migration on docker
	docker-compose -f ./docker-compose-dev.yml run --service-ports --rm api bash -c "alembic revision --autogenerate -m '$(filter-out $@,$(MAKECMDGOALS))'"

migration-local: ## Database migration locally
	poetry run alembic revision --autogenerate -m '$(filter-out $@,$(MAKECMDGOALS))'

migrate-docker: ## Database migrate on docker
	docker-compose -f ./docker-compose-dev.yml run --service-ports --rm api bash -c "alembic upgrade head && alembic stamp head"

migrate-local: ## Database migrate locally
	poetry run alembic upgrade head
	poetry run alembic stamp head

requirements: ## Export requirements file based on poetry packages
	poetry export -f requirements.txt --output requirements.txt --without-hashes
