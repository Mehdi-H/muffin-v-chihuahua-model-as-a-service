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
		pyenv virtualenv ${PYTHON_VERSION} muffin-v-chihuhua-backend-${PYTHON_VERSION} && \
		pyenv activate muffin-v-chihuhua-backend-${PYTHON_VERSION}

.PHONY: dependencies  ## 🐍 ⬇️ Install python dependencies
dependencies:
	pip install .

.PHONY: model  ## 🧠 ⬇️ Download a model to classify muffin and chihuahua images, it may take a few seconds
model:
	wget -nc https://github.com/fchollet/deep-learning-models/releases/download/v0.5/inception_v3_weights_tf_dim_ordering_tf_kernels.h5 -O muffin_v_chihuahua_ml_service/inception_v3_weights_tf_dim_ordering_tf_kernels.h5 || true

.PHONY: package-docker  ## 📦 🐳 packaging the application for Docker
package-docker:
	docker build -t muffin-v-chihuahua-backend:v1 -t mho7/muffin-v-chihuahua-backend:v1 .

.PHONY: run-docker  ## 🐳 ⚙️ run the application as a docker container
run-docker:
	docker run -p 8000:8000 muffin-v-chihuahua-backend:v1

lint-dockerfile:
	hadolint dockerfile