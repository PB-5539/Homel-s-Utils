# Homel's Utils
Some general utilities for using TKinter


You can find a demo program called 'test.py' for more information on the module

just a more cleaned-up version of ui.py and misc_utils.py from my final project for my python class merged into one user-friendly tkinter add-on module.

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
      note: does have issues on slower CPUs (<2-core, <3ghz) with a visual bug

    GraphDrawer:
        a canvas object that automatically draws a graph with configureable arguments
        has a seperate function to update the graph
        customizable width, height, x-range, y-range, point size, line size, background, line color

Notes:
=======
this is not a tutorial for Tkinter, nor is this associated with the developers of the Tkinter module. 

this is an independent project made to make working with Tkinter easier for anyone who is new to the module or anyone who is somewhat new to python in general. 

(this does not cover most of the basics but it outlines some concepts here and there that may be less evident)

this module prints debug information every time an object is created using it, commonly something like [object] created with name: [name] with parent: [parent object]. xpad: [horizontal padding] etc...

this module was partially made using AI*, I have kept the usage to a minimum and with that this project was heavily iterated on by me alone. I understand why some may be against it, I thought I would at least make that clear.

again this is a simple module for beginners to Tkinter and it is only made by one person (with minimal help from AI) whom of which is also relatively new to python so expect inconsistencies, bugs, Inneficient methods, and any other problems.

I do intend to update this but do not expect updates very often, I do accept suggestions and to that I will try to the best of my ability to add them if it fits.

apologies if any of the comments are confusing, this was a branch project of my final project for my python class. Its a collection of useful functions I used to simplify Tkinter's process for creating and customizing widgets when working on said final project.

*AI Usage Clarification
=======
AI (GPT-OSS:20b hosted through Ollama on my own local server) was used to generate the following parts of this module:

The Graph Drawer

The Idea was mine and I had a reasonable assumtion of how it would work but I had no Idea how to actually get it to work with the updating system I wanted. 

The Draggable Frame

Same thing, I had the idea and roughly an idea as to how it would works but had no idea how to actually controll windows like I needed to.

General Edits

Mostly just using AI for the more tedious tasks of changing all of the functions from Positional Arguments to Keyword Arguments, also handling any simple additions like the cardinal direction alignment that I never actually ended up using in the original project this came from.