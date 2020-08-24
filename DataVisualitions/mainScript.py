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


		screen=pygame.display.set_mode((800,600))
		pygame.display.set_caption("Graph Analyser")

		file=open("MP1Try1Luis","r")
		xPosArray1=file.read().split("$")
		file.close()

		file=open("MP1Try2Lars","r")
		xPosArray2=file.read().split("$")
		file.close()

		file=open("MP1Try3Luis","r")
		xPosArray3=file.read().split("$")
		file.close()

		file=open("MP2Try1Lars","r")
		xPosArray4=file.read().split("$")
		file.close()





		for i in range(len(xPosArray1)-1):
			drawPoint(float(xPosArray1[i]),i,scale,visualScale,screen,(255,0,0),2,800,600)
		for i in range(len(xPosArray2)-1):
			drawPoint(float(xPosArray2[i]),i,scale,visualScale,screen,(0,200,0),2,800,600)
		for i in range(len(xPosArray3)-1):
			drawPoint(float(xPosArray3[i]),i,scale,visualScale,screen,(0,0,200),2,800,600)
		for i in range(len(xPosArray4)-1):
			drawPoint(float(xPosArray4[i]),i,scale,visualScale,screen,(205,200,200),2,800,600)
		

		
		pygame.display.flip()
		
		clock=pygame.time.Clock()
		done=False

		while not done:
			for event in pygame.event.get():
				if event.type==pygame.QUIT:
					done=True




		

	#getAndCleanInput()
	#monitoreFile("MP1Try3Luis")
	displayGraph("MP1Try3Luis",5,5)
if __name__=="__main__":
	main()
	