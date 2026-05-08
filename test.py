import HL_Utils
from HL_Utils import ui
#lists for storing refrences to Tkinter objects
ls_root = []
#dictionaries for refrencing tkinter widgets by a simpler-string based name system where the key is the name and the value is the object, 
#  to, for example, edit a config you would use something like: dict_<type of object and/or wherever you stored the object>["name given to 
#  object"].configure(...)
dict_buttons = {}
dict_sliders = {}
dict_labels = {}
dict_entries = {}
dict_frames = {}
dict_text_areas = {}
dict_graphs = {}
ui.create_main_ui(name="Homel's Utils Demo", geometry="1920x1080", ls_root=ls_root) #some of these arguments are remnants of the project these came from and may be repurposed later


ui.add_frame(parent=ls_root[0], name="frame test", xpad=10, ypad=30, backg="red", fill="both", LorR="left", dict_frames=dict_frames)
#ls_root[0] refers to the root window
#name is what is stored as the key for this object in the dict_frames dictionary
#xpad is the Padding along the X axis for the widget in pixels on the left or right
#ypad is the Padding along the Y axis for the widget in pixels on the top and bottom
#backg is the background color which can use any of the colors tkinter supports
#fill is an argument that gives the frame the ability to fill along an axis, options are: "x", "y", or "both"
#LorR is an argument that alignes the object to either the left or right, options are: "left" or "right"
#LorR can be used to have multiple tkinter objects on the same Y level with some limitations
#dict_frames stores the frame as a key:value pair as described previously

ui.add_button(parent=dict_frames["frame test"], name="button test", xpad=10, ypad=10, fill="x", backg="grey", dict_buttons=dict_buttons, action=lambda: print("button pressed!"))
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

ui.add_text_area(parent=dict_frames["frame test"], name="text area test", xpad=10, ypad=10, fill="both", backg="white", dict_text_areas=dict_text_areas)
#dict_frames["frame test"] refers to the previously made frame
#name is what is stored as the key for this object in the dict_text_areas dictionary
#all of the other arguments are the same as usual

dict_text_areas["text area test"].insert("end", "this is a text area, you can type in it and it will scroll when you reach the end of the visible area. you can also insert text into it using the insert method as shown here. It can also be used to display text that is too long to fit in the visible area as well as being configurable to be read-only if you want a text-based interface with tkinter\n\n")
#this line uses the insert method of the text area object to insert some text into the text area, the "end" argument tells it to insert 
#  the text at the end of the current text in the text area, you could also use "1.0" to insert at the beginning or "2.5" to insert at 
#  line 2 character 5, there are also other options for where to insert text that you can find in the tkinter documentation as this is 
#  not part of the homel's utils module.
#\n is used to create a new line in the text area, this is a common way to format text in a text area as it allows you to control where
#  lines break and how the text is displayed.






ui.run(ls_root[0])
#this runs the actual ui, it starts the mainloop function for tkinter where it processes everything. this will pause the code here and run the ui, anything you want to happen 
#  while the ui runs is if you set up your own system using functions and likely tk.after(...)
