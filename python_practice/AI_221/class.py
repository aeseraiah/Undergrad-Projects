class Agent:
	def __init__( self ): # default constructor
		self.hidden_variable = False; # no such thing as private in Python
		self.array_position = [0,0]; 
		self.hunger = 0.0;
		self.ID = 0; 
		return; 
	
	def move_me( self , dx, dy ): # member function 
		self.array_position[0] += dx ; 
		self.array_position[1] += dy; 
		print( self.array_position )
		return;

#creating an instance of class named Bob
Bob = Agent()
Bob.ID = 1

Bob.move_me(1,-1)

# Import libraries 
import numpy as np

# Declare environment class
class Environment:
    def __init__( self ):
        return; 
    def setup( self ):
        return; 
    def update( self ):
        return; 

# Declare Agent class (or classes)
class Agent:
    def __init__( self ):
        return; 
    def setup( self ):
        return; 
    def update( self ):
        return; 

# Instantiate and set up environment 
environment = Environment(); 
environment.setup(); 

# Instantiate and set up Agents
number_of_agents = 12; 
agents = {};
for i in range(0,number_of_agents):
	agents[i] = Agent();
	agents[i].setup();
    
# run main loop
number_of_steps = 12; 
for n in range(1,number_of_steps):
	print(n)
	# update environment 
	environment.update(); 

	# update agents 
	for i in range(0,len(agents)-1):
		# we should probably shuffle this order 
		agents[i].update();

print(agents)