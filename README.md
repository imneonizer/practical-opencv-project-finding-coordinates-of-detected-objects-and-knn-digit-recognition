# Practical-opencv-project-finding-coordinates-of-detected-objects-and-knn-digit-recognition
In this project i will show you how you can find circles, their coordinates in an image plus recognize digits on those circles using knn and finally arrange the recognized digits in ascending order of their value and click on those circles sequencially with the help of coordinates associated with the numbers.
>Actually the whole project is about 
>creating a program to play a game automatically
>the aim of the program is to find circles on the main screen it can be 4 or 5
>every circle has a number between 1 to 10
>after finding the circles position on the screen it recognizes
>the digits inside the circles using KNN algorithm
>after that it process the information i.e 'numbers and their coordinates'
>on the screen whic are basically stored inside a python dictionary
>the numbers are arranged in ascending order along with thier position coordinates
>after processing the information it clicks on to those circles 
>in the ascending order of their values.
## External Modules required
```
>> pip install opencv-contrib-python
>> pip install pyautogui
>> pip install pillow
>> pip install numpy
```
### lets move to the Practical hands on
##### Step 1: launch run.py
You will see output something similar to this
![output](https://github.com/imneonizer/practical-opencv-project-finding-coordinates-of-detected-objects-and-knn-digit-recognition/blob/master/images/assets/5.png)
##### Step 2: Lets try a different image
you can change the image to test the program, i have provides five sample images
![Change image](https://github.com/imneonizer/practical-opencv-project-finding-coordinates-of-detected-objects-and-knn-digit-recognition/blob/master/images/assets/1.png)
change `screenshot = 'images/1.png'` to `screenshot = 'images/2.png'` or `screenshot = 'images/3.png'` upto five sample images that i have provided.
>BTW you can download and play this game by downloading the applicaation from this [ webiste](https://www.funnearn.com/)
#### So far you have got the idea and working pipeline of the project
Now lets discuss whats going behind KNN character recognition,
so the program acturally reads the image from `images/1.png` after that
it preprocess the image i.e blurring, dilation etc..
and finally runs canny edge detection algorithm to find the suitable size contours
and after that it records the position coordinates in a dictionary and rename them as per their loop index numbers i.e, the circle which is at the bottom most of the images will preferably be saved as '1.png ' out of those detected circles and crops the circle and save it to an external directory for character recognition.
![cropped circles](https://github.com/imneonizer/practical-opencv-project-finding-coordinates-of-detected-objects-and-knn-digit-recognition/blob/master/images/assets/3.png)
once the cropped images along are saved the recogniton directory contains another `find_number.py`
 which crops the digit parts from those circles and after recognizing the numbers it renames the files as their recognized values i.e if a circle has number written as '5' inside it then it will be save as concatinated value of its index value and its recognized value `idx_val.png` ==`1_5.png`
![recognized numbers](https://github.com/imneonizer/practical-opencv-project-finding-coordinates-of-detected-objects-and-knn-digit-recognition/blob/master/images/assets/4.png)
i have written idx value first becase when we match our data with the dictionary in whih we have stored the idx values and the coordinates of the recognized it will be easier to link the recoggnized the number images with their original coordinate position after they are arranged in ascending order more over we dont know how many circles were there in the images so the index numbers `idx` will help to fetch the information i.e if we will call `idx = 0` it will always printout the smallest recognized value and its coordinate postion from the detected circles.
#### Final words
The project is developed for the computer to play the game automatically and score as high as possible it is able to do so because before taking any steps it takes the screen shot analyse it and then perform any action how ever i skipped that screenshort part here and explained everything after that so you can check the program still runs when i give the screenshotted image as input.

 
