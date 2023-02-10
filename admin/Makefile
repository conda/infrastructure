# Makefile for various tasks with or around the code.
#

SHELL := /bin/bash -o pipefail -o errexit

GH_TOKEN ?= abc

help:
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'

clean:                ## Delete the local terraform state file
	rm -rf terraform.tfstate

init:                 ## Initialise terraform
	terraform init

upgrade:              ## Upgrade to latest compatible terraform/module versions
	terraform init -upgrade

fmt:                  ## Format the .tf files
	terraform fmt

import-repositories:  ## Import all repositories
	rm -f repository-*.tf
	REPOS=$$(gh api orgs/conda/repos --paginate | jq ".[] | .name"); \
	for repository in $$REPOS; do \
		make clean; \
		repository="$${repository#\"}"; \
		repository="$${repository%\"}"; \
		echo Importing $$repository; \
		make import-repository repository=$$repository; \
	done

import-repository:    ## Import repository, e.g. GH_TOKEN=abc make import-repository repository=conda-pack
	rm -f repository-$(repository).tf
	cp repository.tf.tmpl repository-$(repository).tf
	sed -i 's/__repository__/$(repository)/' repository-$(repository).tf
	terraform import \
		-var token=$(GH_TOKEN) \
		github_repository.$(repository) \
		$(repository)
	terraform import \
		-var token=$(GH_TOKEN) \
		github_branch_protection.$(repository) \
		$(repository):main
	terraform show -no-color > repository-$(repository).tf

validate:             ## Validate terraform configuration
	terraform validate

.PHONY: $(MAKECMDGOALS)
