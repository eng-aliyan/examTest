import math

class Rectangle:

	def __init__(self, width, height):
		self.width = width
		self.height = height
		
	def area(self):
		ans = self.width*self.height
		print(ans)
		
	def diagram(self):
		ans = math.sqrt((self.width*self.width+self.height*self.height))
		print(ans)
        
	def compareArea(self, secondRec):
		statment = self.width*self.height > secondRec.width*secondRec.height
		if statment:
 			print(True)
		else:
			print(False)
        
        
rec1 = Rectangle(15, 36)
rec2 = Rectangle(15, 32)

rec1.compareArea(rec2)
	


