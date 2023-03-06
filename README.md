# UVBatcher
UVBatcher is a user-friendly Python script that uses 'bpy' to automatically run the Smart UV Project operation on all fbx files in a designated folder. The script has a simple tkinker GUI that can remember your previous directory selections for input and output. I developed UVBatcher to speed up my XR development workflow when dealing with geometry originating from CAD software like Solidworks and NX. I use a batch export script in 3DS Max to seperate large parasolids into a bunch of individual fbx files so that the Smart UV Project operation has the best shot at generating clean UVs. Ultimately I still sometimes need to manually fix topology and UV maps for certain meshes, but this gives me a fast way to reach a good starting place for unwieldy files.
## Installation
To run the script, you will need 'bpy' running outside of Blender. Setting this up properly can be a bit troublesome, but I've found success using Python version 3.7.6 and pip version 20.2.4. 
## Usage
To use UVBatcher, follow these steps:
1. Install Python version 3.7.6 and pip version 20.2.4.
2. Run `pip install bpy`.
3. Clone or download the repository to your computer.
4. Open a terminal window and navigate to the `UVBatcher` directory.
5. Run `python UVBatcher.py` to start the script.
6. Use the GUI to select the input and output directories.
7. Click the `Batch Process` button to start the UV projection process.
8. Wait for the script to finish running.
9. Check the output directory for the UV mapped fbx files.
Note that there are limitations to what Blender's smart project feature can do in terms of quality, so you may need to manually adjust UV maps for certain meshes.
## License 
This project is licensed under the MIT License.