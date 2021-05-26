## <font color=Maroon>**\[Note\]: Sorry, the software is still in development stage, the relevant functions cannot be implemented yet, now uploaded for the program backup!!!**</font>

## <font color=Maroon>**\[Note\]: Please note this, the person who wrote this program is a rookie, if there are any bugs or areas which can be optimized, please point out, thank you!!!**</font>

### Introduction
* This is a software for reading and displaying 3D models, and it can also be used for format conversion.
* It loads and displays the model by using PyQt and PyOpenGL.
* You can use the mouse and the keyboard to move, rotate or scale the model.
* Chinese: [readme_cn.md](readme_cn.md)

### Requirements
* Only one library is used: PyQt5, you can use pip to install it, namely, "pip install pyqt5".
* Please note that to use some Qt tools such as Qt Designer, install pyqt5-tools using pip (please note that the version should be the same).
* In addition to this, another option is to use the packaged application, which you can download it [here][2].

### <span id="format">Supported file formats</span>
1.	Wavefront(Default)(.obj)
2.	FBX(.fbx)
3.	MikuMikuDance Model(.pmx)

### File formats are possibly supported in the future
1.	Collada(.dae)
2.	Alembic(.abc)
3.	Stl(.stl)
4.	DirectX(.x)
5.	X3D Extensible 3D(.x3d)
6.	Motion Capture(.bvh)
7.	3D Studio(.3ds)
8.	Stanford(.ply)
9.	VRML(.wrl)

### Help during using
1. How to view the models
> * You can use the left mouse button to move the model, the model will be moved to the same position relative to the mouse position.
> * You can use the right mouse button to rotate the model, according to the rotation mode "XYZ Euler", move the mouse left and right to rotate horizontally (change the Z value), move the mouse up and down to flip vertically (change the Y value), Alt+any direction to rotate in the plane (change the X value), the specific rotation Angle is determined by the distance from the mouse to its initial position.
> * You can scroll the middle mouse button to zoom in and out the model. scroll forward to zoom in, and scroll backwards to zoom out.
2. About the file menu: 
> * The Model doesn't close while opening another model. You can use the shortcut "Ctrl+F" or click "View>File menu" to view the opened models.To close the current model, please use the shortcut "Ctrl+C" or click "File>Close".
3. About format conversion:
> * You can use the shortcut "Ctrl+E" or click "File>Export" to export the model.
> * Only support some common formats, see [supported file formats](#format) for more information.

### References
* There are no references yet...

[1]: <https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyopengl>
[2]: <https://www.github.com>
