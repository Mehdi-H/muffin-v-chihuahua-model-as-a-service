SHELL := /bin/bash
.SHELLFLAGS = -ec
.SILENT:
MAKEFLAGS += --silent
.ONESHELL:

.EXPORT_ALL_VARIABLES:
PYTHON_VERSION?=3.8.1

.DEFAULT_GOAL: help

.PHONY: help
help:
	echo "❓ Use \`make <target>' where <target> can be"
	grep -E '^\.PHONY: [a-zA-Z0-9_-]+ .*?## .*$$' $(MAKEFILE_LIST) | \
		awk 'BEGIN {FS = "(: |##)"}; {printf "\033[36m%-30s\033[0m %s\n", $$2, $$3}'

.PHONY: create-env  ## 🐍 Create a python virtualenv
create-env:
	eval "$(pyenv virtualenv-init -)" && \
		pyenv virtualenv ${PYTHON_VERSION} muffin-v-chihuhua-frontend-${PYTHON_VERSION} && \
		pyenv activate muffin-v-chihuhua-frontend-${PYTHON_VERSION}

.PHONY: dependencies  ## 🐍 ⬇️ Install python dependencies
dependencies:
	pip install .

.PHONY: chihuahua-dataset  ## 🐶 ⬇️ Download some chihuahua images, it may take a few minutes
chihuahua-dataset:
	curl -s http://image-net.org/api/text/imagenet.synset.geturls?wnid=n02085620 | head -n 50 > muffin_v_chihuahua/data/chihuahua/urls.txt
	cd muffin_v_chihuahua/data/chihuahua/ && wget -nc -i urls.txt || true
	echo "$$(ls | wc -l) images are now in this folder"

.PHONY: muffin-dataset  ## 🍪 ⬇️ Download some muffin images, it may take a few minutes
muffin-dataset:
	curl -s http://image-net.org/api/text/imagenet.synset.geturls?wnid=n07690273 | head -n 50 > muffin_v_chihuahua/data/muffin/urls.txt
	cd muffin_v_chihuahua/data/muffin/ && wget -nc -i urls.txt || true
	echo "$$(ls | wc -l) images are now in this folder"

.PHONY: datasets  ## 🍪 🐶 ⬇️ Download some muffin and chihuahua images, it may take a few minutes
datasets: chihuahua-dataset muffin-dataset

.PHONY: package-wheel  ## 📦 ☸️ packaging the application as a Wheel
package-wheel: datasets
	pip install wheel && python setup.py bdist_wheel

.PHONY: package-docker  ## 📦 🐳 packaging the application for Docker
package-docker: package-wheel
	docker build -t muffin-v-chihuahua-frontend:v1 -t mho7/muffin-v-chihuahua-frontend:v1 .

.PHONY: run-docker  ## 🐳 ⚙️ run the application as a docker container
run-docker:
	docker run -p 8090:8090 muffin-v-chihuahua-frontend:v1

.PHONY: package-wheel  ## ☸️ ⚙️ run the application from the Wheel distribution
run-app: package-wheel
	pip install dist/muffin_v_chihuahua_with_embedded_model-1.0-py3-none-any.whl
	muffin-v-chihuahua-with-embedded-model run-demo

lint-dockerfile:
	hadolint dockerfile
