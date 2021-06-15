from playsound import playsound 
from gtts import gTTS 
import os
import wikipedia


print()
print('*'*90)
print('*'*90)
print('Welcome to Wikipedia Search Engine'.rjust(50))
print('type "exit" to Exit'.rjust(40))
print('\n\n\n')
while True:
	title = input('Enter Here what to search on wikipedia: ')
	if title == 'exit' or title == 'Exit' or title == 'EXIT':
		print('Thanks For Interacting')
		break
	else:
		print()
		texx = (wikipedia.summary(title))
		print('\n\n\n')

		text = str(texx)

		ss= text.split('.')
		import time
		for i in ss:
			print(i)
			time.sleep(3)
			v =gTTS(text=i,lang="en",slow=False) 
			try:
				v.save("D:\\Python Small Projects\\name11.mp3") 
				os.system('mpg321 name11.mp3')
				# playsound("D:\\Python Small Projects\\name11.mp3") 
			except PermissionError:
				print('permidskkf')

		print('*'*90)
		print('*'*90)
		print()

print()


	# x=input() 
	# s = gTTS(text="hello"+x+" I am Google Text To Speech", lang="en") 
	# s.save("welcome.mp3") 
	# playsound("welcome.mp3") 