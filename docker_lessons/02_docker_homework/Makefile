# HELP
# This will output the help for each task
# thanks to https://marmelab.com/blog/2016/02/29/auto-documented-makefile.html
.PHONY: help

help: ## This help.
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

.DEFAULT_GOAL := help

run: ## Run containers
	docker-compose run -d

up: ## Up containers
	docker-compose up -d

dev-up: ## Up containers with `.env` environment
	docker-compose --env-file ./.env up -d

stop: ## Stop containers
	docker-compose stop

down: ## Down the containers and remove volumes
	docker-compose down -v

clean:  ## Cleaning up old container images
	docker rmi $(docker images -f "dangling=true" -q)

psql: ##Run psql cli in db container
	docker-compose exec db psql -U postgres
