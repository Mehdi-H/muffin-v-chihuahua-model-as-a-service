# muffin-v-chihuahua with a ML model exposed as a service 🍪 🐶

This repo offers some code to illustrate the following blog article <http://link to come when published>.

It aims to demonstrate one way to package with Wheel and Docker a Machine Learning application able to classify muffins and chihuahua in an image. 

This way is described as the packaging of an ML application with **"a model isolated as a separate service"** in the [Continuous Delivery for Machine Learning (CD4ML)](https://martinfowler.com/articles/cd4ml.html#ModelServing) article from Martin Fowler's blog. 


This app needs :

* a pre-trained Deep Learning model 🧠,
* some images of muffins 🍪 and chihuahuas 🐶, for demonstration purposes,
* some Python code 🐍.

Packaging of this Python app is done with :

* the Wheel format ☸️, with setuptools 
* and docker 🐳.

## Specificity of this approach (model isolated as a separate service)

This muffin-v-chihuahua classifier works with 2 services :

- one of them is a Streamlit frontend application, with the responsibility to expose images of muffins or chihuahua with their associated classification prediction

- the other one is a FastAPI backend application, with the responsibility to provide a muffin or chihuahua classification prediction when requested with a machine learning model.

![illustrating model isolated from the frontend app as a separate ML service](./docs/model-isolated-as-a-separate-service.png)

Thus, the model is isolated from the "core" application, in a dedicated service.

