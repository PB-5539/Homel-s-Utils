import HL_Utils
from HL_Utils import ui
"""
NOTE: this is not a tutorial for Tkinter, nor is this associated with the developers of the Tkinter module. 
this is an independent project made to make working with Tkinter easier for anyone who is new to the module
or anyone who is new to python in general. 
(this does not cover most of the basics but it outlines some concepts here and there that may be less evident)
"""
#-------some info-------
#this module prints debug information every time an object is created using it, commonly something like <object> created with name: <name> with parent: <parent object>. xpad: <horizontal padding> etc...
#this module was partially made using AI*, I have kept the usage to a minimum and with that this project was heavily iterated on by me alone. I understand why some may be against it, I thought I would at least make that clear.
#again this is a simple module for beginners to Tkinter and it is only made by one person (with minimal help from AI) whom of which is also relatively new to python so expect inconsistencies, bugs, Inneficient methods, and any other problems.
#I do intend to update this but do not expect updates very often, I do accept suggestions and to that I will try to the best of my ability to add them if it fits.
#apologies if any of the comments are confusing, this was a branch project of my final project for my python class. Its a collection of useful functions I used to simplify Tkinter's process for creating and customizing widgets when working on said final project.
#-----------------------

#lists for storing refrences to Tkinter objects
ls_root = []
#dictionaries for refrencing tkinter widgets by a simpler-string based name system where the key is the name and the value is the object, 
#  to, for example, edit a config you would use something like: dict_<type of object and/or wherever you stored the object>["name given to 
#  object"].configure(...)

ui.create_main_ui(name="Homel's Utils Demo", geometry="1920x1080", ls_root=ls_root) #some of these arguments are remnants of the project these came from and may be repurposed later


ui.add_frame(parent=ls_root[0], name="frame test", xpad=10, ypad=30, backg="red", fill="both", LorR="left", dict_frames=ui.dict_frames)
#ls_root[0] refers to the root window
#name is what is stored as the key for this object in the dict_frames dictionary
#xpad is the Padding along the X axis for the widget in pixels on the left or right
#ypad is the Padding along the Y axis for the widget in pixels on the top and bottom
#backg is the background color which can use any of the colors tkinter supports
#fill is an argument that gives the frame the ability to fill along an axis, options are: "x", "y", or "both"
#LorR is an argument that alignes the object to either the left or right, options are: "left" or "right"
#LorR can be used to have multiple tkinter objects on the same Y level with some limitations
#dict_frames stores the frame as a key:value pair as described previously

ui.add_button(parent=ui.dict_frames["frame test"], name="button test", xpad=10, ypad=10, fill="x", backg="grey", dict_buttons=ui.dict_buttons, action=lambda: print("button pressed!"))
#dict_frames["frame test"] refers to the previously made frame
#name is what is stored as the key for this object in the dict_buttons dictionary as well as being the text displayed on the button object in the ui
#action refrences a function by the function name alone with no parenthesis, if you wish to pass arguments my recomendation is to use lambda as shown here where you can refrence
#  your own funtion while passing arguments or run code as lambda just creates a quick temporary function. this version will print "button pressed!" to the terminal every time 
#  the button is pressed.
#dict_button stores the button as a key:value pair as described previously
#all of the other arguments are the same as the frame

ui.DraggableWindow(parent=ls_root[0], title="draggable window test", x=400, y=100, w=450, h=350, color="blue")
#DraggableWindow is a custom class that creates a window that can be dragged around the screen by clicking and dragging the title bar. 
#there is no way to store a refrence to this object currently but that may change in the future if i find a use for it.
#title is the name that will appear at the top of the draggable frame window.
#x and y are the coordinates for where the window will appear on the screen when it's created, in pixels, (0,0) is the top left 
#  corner of the screen
#w and h are the width and height of the window in pixels
#color is the background color of the window which can use any of the colors tkinter supports

ui.add_text_area(parent=ui.dict_frames["frame test"], name="text area test", xpad=10, ypad=10, fill="both", backg="white", dict_text_areas=ui.dict_text_areas)
#dict_frames["frame test"] refers to the previously made frame
#name is what is stored as the key for this object in the dict_text_areas dictionary
#all of the other arguments are the same as usual

ui.dict_text_areas["text area test"].insert("end", f"this is a text area, you can type in it and it will scroll when you reach the end of the visible area. you can also insert text into it using the insert method as shown here. It can also be used to display text that is too long to fit in the visible area as well as being configurable to be read-only if you want a text-based interface with tkinter.\nUsing {r"\n"} (the newline keyword) pushes all of the following text to the next line, if you look at the code after this there are 2 after this one and one before this one. \n\nNow this text should be below the previous text with a one line space between.")
#this line uses the insert method of the text area object to insert some text into the text area, the "end" argument tells it to insert 
#  the text at the end of the current text in the text area, you could also use "1.0" to insert at the beginning or "2.5" to insert at 
#  line 2 character 5, there are also other options for where to insert text that you can find in the tkinter documentation as this is 
#  not part of the homel's utils module.
#'\n' is used to create a new line in the text area, this is a common way to format text in a text area as it allows you to control where
#  lines break and how the text is displayed.

def logic_loop():
    print("this code will run either 100 times a second or as fast as possible.") #this might clutter up the console so avoid actually printing so much
    #for loops like this it is best to keep a counter variable for how many times this loop has run, this would be useful for timing while not interupting other functions. 
    ls_root[0].after(10, logic_loop)
    #this should stay last in the logi_loop function, the name of this function can be anything so long as it matches elsewhere.

ls_root[0].after(1000, logic_loop)
#this waits one second while Tkinter starts up, then starts the logic loop. depending on the hardware you may want to change the timing on "ls_root[0].after(1, logic_loop)" to
# relieve any resource stress.
ui.run(ls_root[0])
#this runs the actual ui, it starts the mainloop function for tkinter where it processes everything UI related, this will allow ls_root[0].after to run based on it's set time.


#---*AI Usage Clarification---
#AI (GPT-OSS:20b hosted through Ollama on my own local server) was used to generate the following parts of this module:

#-The Graph Drawer-
#The Idea was mine and I had a reasonable assumtion of how it would work but I had no Idea how to actually get it to work with the updating system I wanted. 

#-The Draggable Frame-
#Same thing, I had the idea and roughly an idea as to how it would works but had no idea how to actually controll windows like I needed to.

#-General Edits-
#Mostly just using AI for the more tedious tasks of changing all of the functions from Positional Arguments to Keyword Arguments, also handling any simple additions like the cardinal direction alignment that I never actually ended up using in the original project this came from.