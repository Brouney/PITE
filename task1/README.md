# Task one - raport #

In this exercise we had to write module that will be simulate autonomic car.
The simulation is event based. The program act on the event,prints out current steering wheel angle, speed and distance,
runs in infinite loop until user breaks the loop.
After writing exercise i learnt about how to use events and classes. In editing: I added : if __name__ =="__main__"
and rename classes to pep8 standard, deleted some unused code, rewrite printing -> to use "String".format() and added writing output to file.
In output we can see: "speed: 0 m/s angle: -19 distance: 0.0" . Its example. To write exercise, I decided to make separately class for every event.
In my oppinion it was clear enought at that moment. Every event makes what has to, at example event class "TurnRight" makes car to turn right, everything was made in separated functions. 
In while loop every event is randomly choosen and car "rides autonomicaly". 

