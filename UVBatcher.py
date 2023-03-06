import os
import sys
import bpy
from tkinter import *
import tkinter.ttk as ttk
from tkinter.filedialog import askdirectory
import configparser

# Read configuration file
config = configparser.ConfigParser()
config.read('config.ini')

# Function to select input directory
def select_directory_in():
    root = Tk()
    root.withdraw()
    path_to_fbx_directory = askdirectory()
    directory_entry.delete(0, 'end')
    directory_entry.insert(0, path_to_fbx_directory)
    config.set('DEFAULT', 'last_input_dir', path_to_fbx_directory)
    with open('config.ini', 'w') as configfile:
        config.write(configfile)

# Function to select output directory
def select_directory_out():
    root = Tk()
    root.withdraw()
    path_to_output = askdirectory()
    directory_output.delete(0, 'end')
    directory_output.insert(0, path_to_output)
    config.set('DEFAULT', 'last_output_dir', path_to_output)
    with open('config.ini', 'w') as configfile:
        config.write(configfile)


# Function to recursively import fbx files in input directory, run smart UV project, then export them to the output directory
def run_script():
    path_to_fbx_directory = directory_entry.get()
    path_to_output = directory_output.get()
    file_list = sorted(os.listdir(path_to_fbx_directory))
    bpy.ops.object.select_all(action='DESELECT')
    bpy.data.objects['Camera'].select_set(True)
    bpy.ops.object.delete()
    bpy.ops.object.select_all(action='DESELECT')
    bpy.data.objects['Light'].select_set(True)
    bpy.ops.object.delete()
    bpy.ops.object.select_all(action='DESELECT')
    bpy.data.objects['Cube'].select_set(True)
    bpy.ops.object.delete()

    for filename in os.listdir(path_to_fbx_directory):
        f = os.path.join(path_to_fbx_directory, filename)
        print(f)
        bpy.ops.import_scene.fbx(filepath = f)
        obj = bpy.context.window.scene.objects[0]
        bpy.context.view_layer.objects.active = obj
        bpy.context.view_layer.update()
        bpy.ops.object.editmode_toggle()
        bpy.ops.mesh.select_all(action='SELECT')
        bpy.ops.uv.smart_project()
        bpy.ops.object.editmode_toggle()
        portion = os.path.splitext(f)
        newname = os.path.basename(portion[0]) + "_UV.fbx"
        path_to_file2 = os.path.join(path_to_output, newname)
        bpy.ops.export_scene.fbx(filepath = path_to_file2)
        bpy.ops.object.delete()
    sys.exit()

# Create the main window
root = Tk()
root.title("UVBatcher")
root.geometry('400x160')
root.resizable(0, 0)

# Define custom style for buttons and labels
style = ttk.Style(root)
style.configure('Custom.TButton', background='#BEBEBE')
style.configure('Custom.TLabel', font=('Futura', 10), foreground='#336B87')

# Create label and input field for input directory path
directory_labelin = ttk.Label(root, text="Input Directory Path:", style='Custom.TLabel')
directory_labelin.pack()
directory_entry = Entry(root, width=50)
directory_entry.pack()

# Set the initial value of input directory field from the config file
last_input_dir = config.get('DEFAULT', 'last_input_dir')
if os.path.isdir(last_input_dir):
    directory_entry.insert(0, last_input_dir)

# Create button for selecting input directory
selectinput_button = ttk.Button(root, text="Select Input Directory", command=select_directory_in, style='Custom.TButton')
selectinput_button.pack()

# Create label and input field for output directory path
directory_labelout = ttk.Label(root, text="Output Directory Path:", style='Custom.TLabel')
directory_labelout.pack()
directory_output = Entry(root, width=50)
directory_output.pack()

# Set the initial value of output directory field from the config file
last_output_dir = config.get('DEFAULT', 'last_output_dir')
if os.path.isdir(last_output_dir):
    directory_output.insert(0, last_output_dir)

# Create button for selecting output directory
selectoutput_button = ttk.Button(root, text="Select Output Directory", command=select_directory_out, style='Custom.TButton')
selectoutput_button.pack()

# Create button for running the batch operation
run_button = ttk.Button(root, text="Batch Process", command=run_script, style='Custom.TButton')
run_button.pack()

root.mainloop()