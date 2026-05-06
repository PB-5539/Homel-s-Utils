# Homel's Utils
Some general utilities for using TKinter

just a more cleaned-up version of ui.py and misc_utils.py from my final project for CTI-110 meged into one user-friendly tkinter add-on module.

what thes module adds:

a simpler way to create tkinter widgets for both beginners and experts
2 new classes that inherit from tkinter objects
    DraggableFrame:
      a frame that works like a window within a window 
      it is moveable by dragging the top bar 
      can be destroyed with a little X icon
      can house anything a regular frame or window can
      note: does have issues on slower CPUs (<4-core, <4ghz) with a visual bug
