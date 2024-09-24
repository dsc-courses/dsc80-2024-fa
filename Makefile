TODAY := $(shell date +"%m-%d")


.PHONY:
help:
	@echo "Available make commands"
	@echo "==================="
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'


.PHONY:
push: ## Pushes changes
	git add -A
	git commit -m "Deploy $(TODAY)" --allow-empty
	git pull origin main
	git push origin main