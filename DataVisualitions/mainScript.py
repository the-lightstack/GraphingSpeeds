def main():
	import pygame
	pygame.init()
	fn=None
	def getAndCleanInput():
		fileName=input("File Name: ")
		file=open(fileName,"a")
		global fn
		fn=fileName
		done=False
		while not done:
			inputVar1=input("1:")
			inputVar2=input("2:")
			
			print("----------")

			if inputVar1=="stop" or inputVar2=="stop":
				done=True
				break
			else:
				try:
					result=str((float(inputVar1)+float(inputVar2))/2)+"$"
					file.write(result)
					print("Result: "+result)
				except:
					print("Error caught.")
		file.close()


	def monitoreFile(fileName):
		data="Error -1"
		with open(fileName,"r") as file:
			data=file.read()
		data=data.split("$")[:-1]
		for i in range(len(data)):
			print((i+1)*5,":",data[i]+"\n")
	def drawScala(width,height,margin,boxWidth,boxHeight,screen,color):
		import pygame
		pygame.init()

		pygame.draw.rect(screen,color,pygame.Rect(margin,(height-margin-boxHeight),width-margin,boxHeight))
	def drawPoint(value,index,scale,visualScale,screen,color,r,w,h):
		margin=20

		x=index*scale*visualScale+margin
		y=h-(value*scale*visualScale+margin)
		pygame.draw.circle(screen,color,(int(x),int(y)),r)





	def displayGraph(inputFile,scale,visualScale):
		import random

		screen=pygame.display.set_mode((800,600))
		pygame.display.set_caption("Graph Analyser")
		
		iterations=4
		for i in range(1,iterations+1):
			rgb=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
			file=open(str(i),"r")
			data=file.read().split("$")
			for i in range(len(data)-1):
				drawPoint(float(data[i]),i,scale,visualScale,screen,rgb,4,800,600)
			file.close()

		
		pygame.display.flip()
		
		clock=pygame.time.Clock()
		done=False

		while not done:
			for event in pygame.event.get():
				if event.type==pygame.QUIT:
					done=True




		

	#getAndCleanInput()
	#monitoreFile("MP1Try3Luis")
	displayGraph("",5,5)
if __name__=="__main__":
	main()
	