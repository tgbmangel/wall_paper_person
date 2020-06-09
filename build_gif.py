# -*- coding: utf-8 -*-
# @Project : P3 
# @Time    : 2020/6/8 11:17
# @Author  : zsr
# @File    : build_gif.py
# @Software: PyCharm
from PIL import Image
from PIL import ImageSequence
def frame_interator(frames):
    size=(1920,1080)
    for frame in frames:
        frame_copy=frame.copy()
        frame_copy=frame_copy.resize(size,Image.ANTIALIAS)
        yield frame_copy
def resize_gif(origin_path):
    img=Image.open(origin_path)
    _frames=ImageSequence.Iterator(img)
    frames=frame_interator(_frames)
    out_img=next(frames)
    out_img.info=img.info
    save_path=origin_path.replace('.',"_resize.")
    out_img.save(save_path,save_all=True,append_images=list(frames))
    return save_path

if __name__=="__main__":
    resize_gif('dd.gif')