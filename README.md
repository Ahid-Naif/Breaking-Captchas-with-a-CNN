# Breaking Captchas with Convolutional Neural Networks
* This project is a captcha breaker system that utilizes deep learning to achieve its goal.
* The model has been trained using LeNet architecture.
* An example of a captcha we aim to break is shown below.
<br>

![](https://github.com/Ahid-Naif/Breaking-Captchas-with-a-CNN/blob/master/assets/captcha_example.jpg)

# The steps followed to build the model:
1. Download the captcha dataset.
2. Split dataset into training and testing datasets.
3. Labelling images. The `annotate.py` script annotates all of the extract the digits from each image in `downloads` images and hand-label every digit automatically.
4. Training the model. The `train_model.py` script will train LeNet on the labelled digits.
5. Testing and evaluating our model on example images. The `test_model.py` will apply LeNet to captcha images themselves.

# Result
This model has achieved  100% accuracy. However, the used dataset  might be simple.

## Samples
<br>

![](https://github.com/Ahid-Naif/Breaking-Captchas-with-a-CNN/blob/master/assets/exp1.png)
<br>

![](https://github.com/Ahid-Naif/Breaking-Captchas-with-a-CNN/blob/master/assets/exp2.png)
<br>

![](https://github.com/Ahid-Naif/Breaking-Captchas-with-a-CNN/blob/master/assets/exp3.png)
<br>

![](https://github.com/Ahid-Naif/Breaking-Captchas-with-a-CNN/blob/master/assets/exp4.png)
<br>

![](https://github.com/Ahid-Naif/Breaking-Captchas-with-a-CNN/blob/master/assets/exp5.png)
