# coding=utf-8
# 重要标志和变量
SuffixList=[
    "Wavefront (*.obj)",
    "FBX (*.fbx)",
    "MikuMikuDance Model (*.pmx)",
]
LoaderDictionary={
    ".obj": "Core.ObjLoader",
    ".fbx": "Core.FbxLoader",
    ".pmx": "Core.PmxLoader",
}