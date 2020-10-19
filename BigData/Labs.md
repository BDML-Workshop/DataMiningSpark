# Ecosystem and prerequisites

1. [Spark and how to install](Spark/) (Linux or windows 10 with WSL or virtualmachine image)
2. [Python API for Spark](http://spark.apache.org/docs/latest/api/python/)
3. [Python documents](https://docs.python.org/3/)


# Introduction wgy python with Spark

Notwithstanding its fame as only a scripting language, Python exposes several programming paradigms like array-oriented programming, object-oriented programming, asynchronous programming, and many others. One paradigm that is of particular interest for Big Data processing is functional programming.

**Functional programming** is a common paradigm when you are dealing with Big Data. Writing in a functional manner makes easier parallel code. This means it’s easier to take your code and have it run on several CPUs or even entirely different machines. You can work around the physical memory and CPU restrictions of a single host by running on multiple systems at once.

This is the power of the PySpark ecosystem, allowing you to take functional code and automatically distribute it across an entire cluster of computers.

Many of the core ideas of functional programming are available in Python’s standard library and built-ins. *You can learn many of the concepts needed for Big Data processing without ever leaving the comfort of Python!*

The core idea of functional programming is that data should be manipulated by functions without maintaining any external state. This means that your use ummutable data and always returns new data instead of manipulating the data in-place.

Another common idea in functional programming is anonymous functions (lambda). Python exposes anonymous functions using the lambda keyword.