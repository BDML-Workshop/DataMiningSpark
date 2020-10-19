# Tentative Schedule

| Date         | Instructor | Title |
|  ---- |  ----------|   ------|
| Day 1 (November 16)/5-5:30 | Pascal | BigData, Machine Learning and text mining by example. Using PySpark (Spark+Python). Why Spark for BigData and ML: Basic knowledge for Text Mining:LSA,DSA,TF-IDF,Word2Vec. installing pyspark on Windows or Linux and first basic examples|
| Day 2 (November 17)/5-8| Pascal| Implementing 1 or 2 relalistics Text Mining examples  |
| Day 3 (November 19)/5-8 | Hikmat | Introduction, Logistic Regression (Identifying Shipts), Shallow Network (Movie Reviews), Backpropagation|
| Day 4 (November 21)/5-8| Hikmat | Feedforward Networks (MNIST digits), Tensorflow and Keras|
| Day 5 (November 24)/5-8 | Hikmat | Convolution Networks (MNIST digits), Recurrent Networks|
| Day 6 (November 26)/5-8 | Hikmat |Autoencoders (denoising), Variational Encoders(data generation), Generative Adversarial Networks|
| Day 7 (November 30)/5-8 | Walid |Machine learning application:Face Mask Detection |
| Day 8 (December 1)/5-8 | M. Hülsman |Introduction to NLP|
| Day 9 (December 2)/5-8| Walid | Title 2 |
| Day 10 (December 3)/5-8| Herpers | CNN applications|



# Neural Network and Text Mining

## Neural Networks

This course introduces Neural Network for Machine Learning. It is meant to be a hands-on
course without sacrificing the conceptual background. As such the first few code examples are developed (using numpy or cupy) from basic principles without using any ML framework. After that we use Tensorflow v2 for almost all examples.

### Already done

Below are already done (the code) but need (a lot of) polishing. Especially integrating the lecture with the code.
1. Introduction
1. Logistic Regression: basic concepts, perceptron, activation function, loss and trainning. Two different applications: one using CIFAR10 data set  and the second using  **sentiment analysis** in Tweets
1. Neural Network with a single layer: a single hidden layer, backpropagation example, training using gradient descent. Using a generate data set
1. The same example as the previous but using Tensorflow low level API (as opposed to Keras) automatic differentiation.
1. Feedforward Networks: design of a feedforward network with an arbitrary number of layers and backpropagation from first principles using numpy (cupy) with no framework used. Application to MNIST data set
1. Same as the above but using the high level Keras API in tensorflow
1. Convolution Networks using Keras. Application to CIFAR10 data set

### coming soon

1. Recurrent Neural Networks: using RNN in Tensorflow to detect spam messages  
1. Autoencoder.


## Text mining

Visit this directory [BigData](BigData)

<img src="https://github.com/hikmatfarhat-ndu/CSC645/blob/master/figures/gradient-descent.png" width=200 />

