## <font color=Maroon>**\[Note\]: 抱歉, 该软件还在开发阶段, 无法实现相关功能, 现在上传的为程序备份!!!**</font>

## <font color=Maroon>**\[Note\]: 注意, 写这个程序的人是个菜鸟, 如果有任何Bug或者是可以优化的地方欢迎指出, 谢谢!!!**</font>

### 介绍
* 这是一个用来读取和显示3D模型的软件, 也可以用于格式转换。
* 它通过使用PyQt和PyOpenGL来加载和显示模型。 
* 可以使用鼠标和键盘来移动, 旋转和缩放模型。
* English: [readme.md](readme.md)

### 需要的库
* 使用了三个库: PyQt5, QScintilla和chardet。
* 可以使用pip安装PyQt5, QScintilla和chardet, 即"pip install PackageName"。
* 请注意, v5.11及更高版本的PyQt5不包含WebEngine模块, 请用pip单独安装PyQtWebEngine。
* 还有一点需要注意, 若要使用一些Qt工具如Qt Designer, 请用pip安装pyqt5-tools(请注意版本要一致)。
* 除此之外, 还可以使用打包好的程序, 你可以在[这里][2]下载它。

### <span id="format">支持的文件格式</span>
1.	Wavefront(默认)(.obj)
2.	FBX(.fbx)
3.	MikuMikuDance Model(.pmx)

### 未来可能支持的文件格式
1.	Collada(.dae)
2.	Alembic(.abc)
3.	Stl(.stl)
4.	DirectX(.x)
5.	X3D Extensible 3D(.x3d)
6.	Motion Capture(.bvh)
7.	3D Studio(.3ds)
8.	Stanford(.ply)
9.	VRML(.wrl)

### 使用帮助
1. 模型的查看: 
> * 可以使用左键来移动模型, 模型会位移至与鼠标的相对位置不变的位置。
> * 可以使用右键来旋转模型, 按照旋转模式"XYZ欧拉"看, 左右移动鼠标则水平旋转(改变Z值), 上下移动鼠标则垂直翻转(改变Y值), Alt+任意方向移动则平面旋转(改变X值),  具体旋转角度则按离初始位置的距离决定。
> * 可以滚动鼠标中键来缩放模型, 向前为放大, 向后为缩小。
2. 文件菜单: 
> * 模型并不会因为打开另一个模型而关闭, 可以使用快捷键"Ctrl+F"或打开"视图>文件菜单"来查看已经打开的模型, 关闭当前模型请使用快捷键"Ctrl+C"或选择"文件>关闭"。
3. 格式转换: 
> * 使用快捷键"Ctrl+E"或选择"文件>导出"进行文件的导出。
> * 只支持部分通用格式, 参见[支持的文件格式](#format)。

### 参考资料
* 目前还没有参考资料。。。

[1]: <https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyopengl>
[2]: <https://www.github.com>