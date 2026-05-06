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
ui.create_main_ui(name="Homel's Utils Demo", geometry="800x700", ls_root=ls_root) #some of these arguments are remnants of the project these came from and may be repurposed later


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





ui.run(ls_root[0])
#this runs the actual ui, it starts the mainloop function for tkinter where it processes everything. this will pause the code here and run the ui, anything you want to happen 
#  while the ui runs is if you set up your own system using functions and likely tk.after(...)
