import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
import os.path
import subprocess

_script = sys.argv[0]
_location = os.path.dirname(_script)

import a10_support

_bgcolor = '#d9d9d9'  # X11 color: 'gray85'
_fgcolor = '#000000'  # X11 color: 'black'
_compcolor = 'gray40' # X11 color: #666666
_ana1color = '#c3c3c3' # Closest X11 color: 'gray76'
_ana2color = 'beige' # X11 color: #f5f5dc
_tabfg1 = 'black' 
_tabfg2 = 'black' 
_tabbg1 = 'grey75' 
_tabbg2 = 'grey89' 
_bgmode = 'light' 

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''

        top.geometry("800x600+381+102")
        top.minsize(800, 600)
        top.maxsize(800, 600)
        top.resizable(1,  1)
        top.title("AutoClicker")
        top.configure(background="#c6ffc6")
        top.configure(cursor="X_cursor")
        top.configure(highlightbackground="#ff5353")
        top.configure(highlightcolor="#ff5353")
        top.configure(highlightthickness="10")

        self.top = top

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.Label1 = tk.Label(self.top)
        self.Label1.place(relx=0.075, rely=0.067, height=82, width=686)
        self.Label1.configure(activebackground="#ffffff")
        self.Label1.configure(activeforeground="#ffffff")
        self.Label1.configure(background="#ff5353")
        self.Label1.configure(compound='center')
        self.Label1.configure(disabledforeground="#ffffff")
        self.Label1.configure(font="-family {Segoe UI} -size 15")
        self.Label1.configure(foreground="#ffffff")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(relief="groove")
        self.Label1.configure(text='''AutoClicker''') # title
        
        
        
        self.Labelframe1 = tk.LabelFrame(self.top)
        self.Labelframe1.place(relx=0.025, rely=0.25, relheight=0.325, relwidth=0.465)
        self.Labelframe1.configure(relief='groove')
        self.Labelframe1.configure(foreground="#ff5353")
        self.Labelframe1.configure(text='''Change Settings''') # editing settings container
        self.Labelframe1.configure(background="#c6ffc6")
        self.Labelframe1.configure(highlightbackground="#d9d9d9")
        self.Labelframe1.configure(highlightcolor="black")
        
        self.hotkey_value = tk.StringVar()
        self.click_value = tk.IntVar()
        self.interval_value = tk.DoubleVar()
        
        self.Ehotkey = tk.Entry(self.Labelframe1, textvariable=self.hotkey_value) # input for hotkey
        self.Ehotkey.place(relx=0.511, rely=0.205, height=20, relwidth=0.226, bordermode='ignore')
        self.Ehotkey.configure(background="white")
        self.Ehotkey.configure(disabledforeground="#a3a3a3")
        self.Ehotkey.configure(font="TkFixedFont")
        self.Ehotkey.configure(foreground="#000000")
        self.Ehotkey.configure(highlightbackground="#d9d9d9")
        self.Ehotkey.configure(highlightcolor="black")
        self.Ehotkey.configure(insertbackground="black")
        self.Ehotkey.configure(selectbackground="#c4c4c4")
        self.Ehotkey.configure(selectforeground="black")
        
        self.Eclicks = tk.Entry(self.Labelframe1, textvariable=self.click_value)  # input for clicks
        self.Eclicks.place(relx=0.511, rely=0.41, height=20, relwidth=0.226, bordermode='ignore')
        self.Eclicks.configure(background="white")
        self.Eclicks.configure(disabledforeground="#a3a3a3")
        self.Eclicks.configure(font="TkFixedFont")
        self.Eclicks.configure(foreground="#000000")
        self.Eclicks.configure(highlightbackground="#d9d9d9")
        self.Eclicks.configure(highlightcolor="black")
        self.Eclicks.configure(insertbackground="black")
        self.Eclicks.configure(selectbackground="#c4c4c4")
        self.Eclicks.configure(selectforeground="black")
        
        self.Einterval = tk.Entry(self.Labelframe1, textvariable=self.interval_value)  # input for interval
        self.Einterval.place(relx=0.511, rely=0.615, height=20, relwidth=0.226, bordermode='ignore')
        self.Einterval.configure(background="white")
        self.Einterval.configure(disabledforeground="#a3a3a3")
        self.Einterval.configure(font="TkFixedFont")
        self.Einterval.configure(foreground="#000000")
        self.Einterval.configure(highlightbackground="#d9d9d9")
        self.Einterval.configure(highlightcolor="black")
        self.Einterval.configure(insertbackground="black")
        self.Einterval.configure(selectbackground="#c4c4c4")
        self.Einterval.configure(selectforeground="black")
        
        self.CHhotkey = tk.Label(self.Labelframe1)
        self.CHhotkey.place(relx=0.188, rely=0.205, height=21, width=104, bordermode='ignore')
        self.CHhotkey.configure(activebackground="#ffffff")
        self.CHhotkey.configure(anchor='w')
        self.CHhotkey.configure(background="#c6ffc6")
        self.CHhotkey.configure(compound='left')
        self.CHhotkey.configure(disabledforeground="#a3a3a3")
        self.CHhotkey.configure(foreground="#000000")
        self.CHhotkey.configure(highlightbackground="#d9d9d9")
        self.CHhotkey.configure(highlightcolor="black")
        self.CHhotkey.configure(text='''Change Hotkey :''') # display label (only cosmetics)
        
        self.CHclicks = tk.Label(self.Labelframe1)
        self.CHclicks.place(relx=0.188, rely=0.41, height=21, width=104, bordermode='ignore')
        self.CHclicks.configure(activebackground="#f9f9f9")
        self.CHclicks.configure(anchor='w')
        self.CHclicks.configure(background="#c6ffc6")
        self.CHclicks.configure(compound='left')
        self.CHclicks.configure(disabledforeground="#a3a3a3")
        self.CHclicks.configure(foreground="#000000")
        self.CHclicks.configure(highlightbackground="#d9d9d9")
        self.CHclicks.configure(highlightcolor="black")
        self.CHclicks.configure(text='''Change Clicks :''') # display label (only cosmetics)
        
        self.CHinterval = tk.Label(self.Labelframe1)
        self.CHinterval.place(relx=0.188, rely=0.615, height=21, width=104, bordermode='ignore')
        self.CHinterval.configure(activebackground="#f9f9f9")
        self.CHinterval.configure(anchor='w')
        self.CHinterval.configure(background="#c6ffc6")
        self.CHinterval.configure(compound='left')
        self.CHinterval.configure(disabledforeground="#a3a3a3")
        self.CHinterval.configure(foreground="#000000")
        self.CHinterval.configure(highlightbackground="#d9d9d9")
        self.CHinterval.configure(highlightcolor="black")
        self.CHinterval.configure(text='''Change Interval :''') # display label (only cosmetics)
        
        self.confirm = tk.Button(self.Labelframe1, command=self.update_and_clear_focus)
        self.confirm.place(relx=0.403, rely=0.769, height=24, width=57, bordermode='ignore')
        self.confirm.configure(activebackground="beige")
        self.confirm.configure(activeforeground="black")
        self.confirm.configure(background="#ffa4a4")
        self.confirm.configure(compound='left')
        self.confirm.configure(disabledforeground="#a3a3a3")
        self.confirm.configure(foreground="#000000")
        self.confirm.configure(highlightbackground="#d9d9d9")
        self.confirm.configure(highlightcolor="black")
        self.confirm.configure(pady="0")
        self.confirm.configure(text='''Confirm''')  # button to update variables
        
        
        
        self.Labelframe2 = tk.LabelFrame(self.top)
        self.Labelframe2.place(relx=0.5, rely=0.25, relheight=0.325, relwidth=0.478)
        self.Labelframe2.configure(relief='groove')
        self.Labelframe2.configure(foreground="#ff5353")
        self.Labelframe2.configure(text='''Current Settings''') #  displaying settings container
        self.Labelframe2.configure(background="#c6ffc6")
        self.Labelframe2.configure(highlightbackground="#d9d9d9")
        self.Labelframe2.configure(highlightcolor="black")
        
        self.Dhotkey = tk.Label(self.Labelframe2)
        self.Dhotkey.place(relx=0.497, rely=0.205, height=21, width=74, bordermode='ignore')
        self.Dhotkey.configure(activebackground="#f9f9f9")
        self.Dhotkey.configure(anchor='w')
        self.Dhotkey.configure(background="#c6ffc6")
        self.Dhotkey.configure(compound='left')
        self.Dhotkey.configure(disabledforeground="#a3a3a3")
        self.Dhotkey.configure(foreground="#000000")
        self.Dhotkey.configure(highlightbackground="#d9d9d9")
        self.Dhotkey.configure(highlightcolor="black")
        self.Dhotkey.configure(text='''No Hotkey''') # display label until hotkey is set/updated
        
        self.Dclicks = tk.Label(self.Labelframe2)
        self.Dclicks.place(relx=0.497, rely=0.41, height=21, width=74, bordermode='ignore')
        self.Dclicks.configure(activebackground="#f9f9f9")
        self.Dclicks.configure(anchor='w')
        self.Dclicks.configure(background="#c6ffc6")
        self.Dclicks.configure(compound='left')
        self.Dclicks.configure(disabledforeground="#a3a3a3")
        self.Dclicks.configure(foreground="#000000")
        self.Dclicks.configure(highlightbackground="#d9d9d9")
        self.Dclicks.configure(highlightcolor="black")
        self.Dclicks.configure(text='''No Clicks''') # display label until clicks is set/updated
        
        self.Dinterval = tk.Label(self.Labelframe2)
        self.Dinterval.place(relx=0.497, rely=0.615, height=21, width=74, bordermode='ignore')
        self.Dinterval.configure(activebackground="#f9f9f9")
        self.Dinterval.configure(anchor='w')
        self.Dinterval.configure(background="#c6ffc6")
        self.Dinterval.configure(compound='left')
        self.Dinterval.configure(disabledforeground="#a3a3a3")
        self.Dinterval.configure(foreground="#000000")
        self.Dinterval.configure(highlightbackground="#d9d9d9")
        self.Dinterval.configure(highlightcolor="black")
        self.Dinterval.configure(text='''No Interval''') # display label until interval is set/updated
        
        self.Chotkey = tk.Label(self.Labelframe2)
        self.Chotkey.place(relx=0.183, rely=0.205, height=21, width=94, bordermode='ignore')
        self.Chotkey.configure(activebackground="#f9f9f9")
        self.Chotkey.configure(anchor='w')
        self.Chotkey.configure(background="#c6ffc6")
        self.Chotkey.configure(compound='left')
        self.Chotkey.configure(disabledforeground="#a3a3a3")
        self.Chotkey.configure(foreground="#000000")
        self.Chotkey.configure(highlightbackground="#d9d9d9")
        self.Chotkey.configure(highlightcolor="black")
        self.Chotkey.configure(text='''Current Hotkey :''') # display label (only cosmetics)
        
        self.Cclicks = tk.Label(self.Labelframe2)
        self.Cclicks.place(relx=0.183, rely=0.41, height=21, width=94, bordermode='ignore')
        self.Cclicks.configure(activebackground="#f9f9f9")
        self.Cclicks.configure(anchor='w')
        self.Cclicks.configure(background="#c6ffc6")
        self.Cclicks.configure(compound='left')
        self.Cclicks.configure(disabledforeground="#a3a3a3")
        self.Cclicks.configure(foreground="#000000")
        self.Cclicks.configure(highlightbackground="#d9d9d9")
        self.Cclicks.configure(highlightcolor="black")
        self.Cclicks.configure(text='''Current Clicks:''') # display label (only cosmetics)
        
        self.Cinterval = tk.Label(self.Labelframe2)
        self.Cinterval.place(relx=0.183, rely=0.615, height=21, width=94, bordermode='ignore')
        self.Cinterval.configure(activebackground="#f9f9f9")
        self.Cinterval.configure(anchor='w')
        self.Cinterval.configure(background="#c6ffc6")
        self.Cinterval.configure(compound='left')
        self.Cinterval.configure(disabledforeground="#a3a3a3")
        self.Cinterval.configure(foreground="#000000")
        self.Cinterval.configure(highlightbackground="#d9d9d9")
        self.Cinterval.configure(highlightcolor="black")
        self.Cinterval.configure(text='''Current Interval :''') # display label (only cosmetics)
        

        
        self.Labelframe3 = tk.LabelFrame(self.top)
        self.Labelframe3.place(relx=0.025, rely=0.583, relheight=0.375, relwidth=0.954)
        self.Labelframe3.configure(relief='groove')
        self.Labelframe3.configure(foreground="#ff5353")
        self.Labelframe3.configure(text='''Click Tester''') # click testing container
        self.Labelframe3.configure(background="#c6ffc6")
        self.Labelframe3.configure(highlightbackground="#d9d9d9")
        self.Labelframe3.configure(highlightcolor="black")
        
        self.Clicker = tk.Button(self.Labelframe3)
        self.Clicker.place(relx=0.17, rely=0.178, height=154, width=207, bordermode='ignore')
        self.Clicker.configure(activebackground="beige")
        self.Clicker.configure(activeforeground="black")
        self.Clicker.configure(background="#ffa4a4")
        self.Clicker.configure(compound='left')
        self.Clicker.configure(disabledforeground="#a3a3a3")
        self.Clicker.configure(foreground="#000000")
        self.Clicker.configure(highlightbackground="#d9d9d9")
        self.Clicker.configure(highlightcolor="black")
        self.Clicker.configure(pady="0")
        self.Clicker.configure(text='''Click Me!''') # button to click, to test how fast clicks are in practice
        self.Clicker.configure(command=self.increment_label)
        
        self.reset = tk.Button(self.Labelframe3)
        self.reset.place(relx=0.642, rely=0.578, height=34, width=127, bordermode='ignore')
        self.reset.configure(activebackground="beige")
        self.reset.configure(activeforeground="black")
        self.reset.configure(background="#ffa4a4")
        self.reset.configure(compound='left')
        self.reset.configure(disabledforeground="#a3a3a3")
        self.reset.configure(foreground="#000000")
        self.reset.configure(highlightbackground="#d9d9d9")
        self.reset.configure(highlightcolor="black")
        self.reset.configure(pady="0")
        self.reset.configure(text='''Reset''') # button to reset clicks
        self.reset.configure(command=self.reset_label)
        
        self.counter = tk.Label(self.Labelframe3)
        self.counter.place(relx=0.642, rely=0.222, height=51, width=125, bordermode='ignore')
        self.counter.configure(activebackground="#f9f9f9")
        self.counter.configure(background="#c6ffc6")
        self.counter.configure(compound='center')
        self.counter.configure(disabledforeground="#a3a3a3")
        self.counter.configure(font="-family {Segoe UI} -size 15")
        self.counter.configure(foreground="#000000")
        self.counter.configure(highlightbackground="#d9d9d9")
        self.counter.configure(highlightcolor="black")
        self.counter.configure(text='''0''') # default click amount label for button
        self.load_and_display_settings()
        self.label_value = tk.IntVar()
        self.label_value.set(0)
        
        # Bind the Enter key to the confirm button action for the entire window
        top.bind('<Return>', lambda event=None: self.confirm.invoke())
        self.auto_process = None
        top.protocol("WM_DELETE_WINDOW", self.on_close)

    def on_close(self):
        """Custom close handler to shut down the entire application."""
        if self.auto_process:
            # Terminate the auto_process if it's running
            self.auto_process.terminate()
            # Wait for the process to terminate before exiting
            self.auto_process.wait()
        self.top.destroy()  # Close the GUI window    
        
    
    def load_and_display_settings(self):
        settings = self.read_settings_from_file()
        self.hotkey_value.set(settings.get('hotkey', ''))
        self.click_value.set(settings.get('clicks', 0))
        self.interval_value.set(settings.get('interval', 0.0))
        self.Dhotkey.configure(text=settings.get('hotkey', ''))
        self.Dclicks.configure(text=settings.get('clicks', ''))
        self.Dinterval.configure(text=settings.get('interval', ''))

    # Method to read settings from the settings.txt file
    def read_settings_from_file(self):
        settings = {}
        try:
            with open("settings.txt", "r") as file:
                for line in file:
                    key, value = line.strip().split('=')
                    settings[key] = value
        except FileNotFoundError:
            print("Settings file not found. Default values will be used.")
        return settings



    def increment_label(self):
        current_value = self.label_value.get()
        self.label_value.set(current_value + 1)
        self.counter.configure(text=str(self.label_value.get()))  # Update the label text
    def reset_label(self):
        self.label_value.set(0)
        self.counter.configure(text='''0''')  # Reset the label text


    def update_and_clear_focus(self):
        self.update_labels()
        self.save_settings()
        self.clear_focus()
    def clear_focus(self):
        """Clears focus from input fields by setting it to a neutral element."""
        self.confirm.focus_set()

    def save_settings(self):
        """Saves the current settings to a file and restarts the autoclicker."""
        with open("settings.txt", "w") as file:
            file.write(f"hotkey={self.hotkey_value.get()}\n")
            file.write(f"clicks={self.click_value.get()}\n")
            file.write(f"interval={self.interval_value.get()}\n")
        self.restart_auto_clicker()

    def restart_auto_clicker(self):
        """Restarts the auto.py script if it's running, or starts it if not."""
        if self.auto_process:
            # Terminate the existing process
            self.auto_process.terminate()
            # Wait for the process to terminate before starting a new one
            self.auto_process.wait()
        self.launch_auto_clicker()

    def launch_auto_clicker(self):
        """Launches the auto.py script."""
        script_path = os.path.join(_location, 'auto.py')
        # Start a new subprocess and keep its reference
        self.auto_process = subprocess.Popen(['python', script_path], creationflags=subprocess.CREATE_NEW_PROCESS_GROUP)
    def update_labels(self):
        hotkey = self.hotkey_value.get()
        click = self.click_value.get()
        interval = self.interval_value.get()
        
        # Update the labels with the input values
        self.Dhotkey.configure(text=hotkey)
        self.Dclicks.configure(text=click)
        self.Dinterval.configure(text=interval)
        self.save_settings()
        
    

def start_up():
    a10_support.main()

if __name__ == '__main__':
    a10_support.main()