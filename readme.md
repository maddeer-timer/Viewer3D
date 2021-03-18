English: [readme.md](readme.md)

## 介绍
* 这是一个用来读取和显示3D模型的软件, 也可以用于格式转换。
* 它通过使用PyQt和PyOpenGL来加载和显示模型。 
* 可以使用键盘来移动模型, 使用鼠标来旋转和缩放模型。

## 需要的库
* 使用了两个库: PyQt5和PyOpenGL。
* 可以使用pip安装PyQT5, 即“pip install pyqt5”。
* 不过, 要在64位机器上安装PyOpenGL, 需要访问[这里][1], 因为pip默认安装的是32位版本。
* 除此之外, 还可以使用打包好的程序, 你可以在[这里][2]下载它。

## 支持的文件格式
Collada(.dae)
Alembic(.abc)
3D Studio(.3ds)
FBX(.fbx)
Motion Capture(.bvh)
Stanford(.ply)
Wavefront(.obj)
X3D Extensible 3D(.x3d)
VRML(.wrl)
Stl(.stl)
DirectX(.x)
MikuMikuDance Model(.pmx)

## 参考


[1]: <https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyopengl>
[2]: <https://www.github.com>