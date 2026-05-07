# Homel's Utils
Some general utilities for using TKinter

<<<<<<< HEAD
you can find a demo program called 'test.py' for more information on the module
=======
just a more cleaned-up version of ui.py and misc_utils.py from my final project for CTI-110 meged into one user-friendly tkinter add-on module.

what thes module adds:

a simpler way to create tkinter widgets for both beginners and experts

and integrated system for creating tkinter objects modularly

asigning each object a common name in a dictionary, rather than needing a dedicated variable

2 new classes that inherit from tkinter objects
    DraggableFrame:
        a frame that works like a window within a window 
        it is moveable by dragging the top bar 
        can be destroyed with a little X icon
        can house anything a regular frame or window can
        note: does have issues on slower CPUs (<4-core, <4ghz) with a visual bug
    GraphDrawer:
        a canvas object that automatically draws a graph with configureable arguments
        has a seperate function to update the graph
        customizable width, height, x-range, y-range, point size, line size, background, line color

note: this module is still in development, expect issues, confusion, and proprietary variables not within the module (this will be fixed eventually)