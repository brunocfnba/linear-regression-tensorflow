# Simple Linear Model using TensorFlow
The idea of this repo is to give you a initial idea of how TensorFlow works.

### How the code works

1. The code begins creating two TensorFlow variables (W and b) and 0.3 and -0.3 are assigned to them respectively.
>Any value could be assigned to the variables since they will be trained and changed
TensorFlow knows that variables have been created in his graph model and it wil be responsible for updating them.

2. Two TensorFlow placeholders are created (x and y), the first will receive the input data to be trained and the second the expected correct labels.
>Placeholders are used to let TensorFlow know there will be data coming in through them but you just provide them when actually executing the graph later on.

3. The actual model is created by just setting up the formula using the placeholder and variables.

4. In order to calculate the cost we need to get the difference between what we get from the model and the expected correct value, square them to avoid negative values and then sum them up.

5. With the cost, we need to work to minimize that. In this case we are using [Gradient Descent](https://machinelearningmastery.com/gradient-descent-for-machine-learning/). TensorFlow already provides API for that so it handles all the process in its graph.

6. At this point we have everything in place, now let's start our session and initialize our variables.
>The TensorFlow session will actually run the graph you just built.

7. For our traiing process we'll run our training 1000 times and print the cost after each iteration so you can see it's decreasing.

8. After training we print the values for W and b and imediately test our model by providing a value to view its result. You can provide any value here.
>If you take a look at the values of y (the correct ones) you see that the correct values for W and b are -1.0 and 1.0 respectively and when you check the model printed values for them they are basically the same (assuming we are rounding up).

### Running tensorboard to view the graph

To view the generated TensorFlow graph in Tensorboard, you need first save the graph.

1. Uncomment line 30, replace the path to the place you want to save the graph file and run the code again.

2. In your terminal run `# tensorboard --logdir "<the path where the file should be saved without filename>"`

3. Tensorboard will show a URL and port so you just need to access from your web browser.
>If the URL does not work, try using 'localhost' instead.
