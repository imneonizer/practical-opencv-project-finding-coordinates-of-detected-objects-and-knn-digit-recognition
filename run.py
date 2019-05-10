import cv2
import time
import os
import collections
import pyautogui
import PIL.ImageGrab as ImageGrab
global run_status
run_status = 0
global screenshot



#----------------------------
							#
							#
screenshot = "images/1.png" #
							#
							#
#----------------------------



os.system('color 0a')
def main():
	print("running in loop through while command")
	play = True
	while play:
		try:
			work()
			print()
			#time.sleep(1) #at 0.08 score 240
			os.system("pause")
			play = False #delete this line if you want to play in loop
		except Exception as e:
			time.sleep(1) #score = 235
			play = False
			print(e)

def click(ord):
	pyautogui.moveTo(ord)#moves to x,y (top left as reference)
	pyautogui.click()
def capture():
    im = ImageGrab.grab()
    #im.save('scr_shot.png','png') #originally this was made to play virtual game but for this tutorial i am using a image instead
def work():
	global run_status
	print("run status is: " + str(run_status))
	run_status += 1
	capture()
	#Reading image and cropping Numbers =========================================================================================
	
	#deleting already written photos==================================
	print('deleting photos from recognition/temp_photos if any')
	try:
		#os.system("call recognition/temp_photos/cleaner.bat")
		os.system("cleaner.exe")
	except Exception as e:
		print(e)
		pass

	if not os.path.exists('recognition/temp_photos/arranged'):
		os.mkdir('recognition/temp_photos/arranged')
	if not os.path.exists('recognition/temp_photos/cropped'):
		os.mkdir('recognition/temp_photos/cropped')

	print('finding contour and writing photos')
	#=================================================================
	info_dict = {}
	image = cv2.imread(screenshot)
	image_blur = cv2.GaussianBlur(image.copy(), (5, 5), 0)
	gray=cv2.cvtColor(image_blur,cv2.COLOR_BGR2GRAY)
	edged = cv2.Canny(gray, 10, 250)
	(cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
	idx = 0
	for c in cnts:
		x,y,w,h = cv2.boundingRect(c)
		if w>50 and w<85 and h>50 and h<85:
			idx+=1
			c_cord = (x+40,y+40)
			#print('idx: '+str(idx)+', Coord: '+str(c_cord))
			info_dict.update({idx : c_cord})
			new_img=image[y:y+h,x:x+w]
			cv2.imwrite('recognition/temp_photos/cropped/'+str(idx) + '.png', new_img)
	#============================================================================================================================


	#object for recognizing number  =============================================================================================
	print('running find_number.py, to recognize the numbers')
	from recognition.find_number import my_recognizer
	my_recognizer = my_recognizer.start()
	#============================================================================================================================


	#object for recognized number list ==========================================================================================
	print('running dictionary.py, to get the informations of recognized numbers')
	from recognition.temp_photos.dictionary import my_dict
	my_dict = my_dict.start('recognition/temp_photos/arranged')
	#============================================================================================================================

	#Altering lists to find information==========================================================================================
	print('val_dict: '+str(my_dict)) #idx, value
	print('coord_dict: '+str(info_dict)) #idx, coord)

	print('altering lists to link found informations')
	x_x = list(my_dict)
	y_y = list(info_dict)

	#lets concatenate above two dictionaries
	fin_dict = {}

	for i in my_dict:
		x_x = my_dict[i]
		y_y = info_dict[i]
		fin_dict.update({x_x:y_y})

	print('finally')
	print(fin_dict)
	fin_dict = collections.OrderedDict(sorted(fin_dict.items())) 
	print('sorted')
	print(fin_dict)
	list_num_map = list(fin_dict)
	print('Digits: ',end='')
	print(list_num_map)
	print()

	#accessing dictionary items without knowing key values using index after storing in list===========
	num_idx = len(list_num_map)
	print('Number of digits found: '+str(num_idx))
	print()
	#============================================================================================================================

	#finally clicking in ascending order=========================================================================================
	for idx in range (0, num_idx):
		print('idx: '+str(idx))
		print('digit: '+str(list_num_map[idx]))
		print('(x,y): '+str(fin_dict[list_num_map[idx]]))
		print('click'+str(fin_dict[list_num_map[idx]]))
		#click(fin_dict[list_num_map[idx]])
		print()
	#============================================================================================================================

###################################################################################################
if __name__ == "__main__":
    main()


