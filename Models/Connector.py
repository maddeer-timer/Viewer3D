# coding=utf-8
# 所有要用的模块导入
import Models.ObjLoader
import Models.FbxLoader
import Models.PmxLoader
# 重要标志和变量
SuffixList=[
    "Wavefront (*.obj)",
    "FBX (*.fbx)",
    "MikuMikuDance Model (*.pmx)",
]
LoaderDictionary={
    ".obj": "Models.ObjLoader",
    ".fbx": "Models.FbxLoader",
    ".pmx": "Models.PmxLoader",
}
