class Laptop():
   # constructor / initializer
    def __init__(self,color,ram,storage,processor,model,make,generation):
        self.color=color
        self.ram=ram
        self.storage=storage
        self.processor=processor
        self.model=model
        self.make=make
        self.generation=generation
        
    def specification(self):
        print(f'''
               ram:{self.ram}
               generation:{self.generation}
               storage:{self.storage}
               processor:{self.processor}
               model:{self.processor}
               make:{self.make}
               color:{self.color}
        ''')
    def set_color(self,newcolor):
        color=["black","blue","red"]
        if newcolor in color:
            self.color=newcolor
        else:
            print("color not available")
    
    def get_color(self):
        print(f"the color of laptop is {self.color}")
        
        
class Student():
    #attributes
    shirt="blue"
    shoes="black"
    semester="1st"
    courses="DSA"
    attend=""
    #functionality
    def attendence(self,attend):
        if attend>40:
            print(" attendence is ok")
        else:
            print("short attencence cannot sit in exam")
    def enrollment(self):
        print( "enrolled")
        
    def __init__(self,shirt,shoes,semester,courses):
        self.shirt=shirt
        self.shoes=shoes
        self.semester=semester
        self.courses=courses

    def report(self):
        print(f'''
                shirt: {self.shirt}
                shoes: {self.shoes}
                semester: {self.semester}
                courses: {self.courses}
        ''')        