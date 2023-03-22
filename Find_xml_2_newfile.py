import  os,shutil

def  xml(fileDir, xmlDir):
    list2=os.listdir(fileDir)#从文件夹读取文件名到list2
    for  i  in list2:
        ext = os.path.splitext(i)
        j=ext[0]+'.xml'#改成标注文件的文件格式
        if os.path.exists(xmlDir+ '/' + j):
            shutil.move(xmlDir + j, new_xmlDir + "\\" + j)#将原xml文件的路径移到新xml的文件路径
    return
if __name__ == '__main__':
    fileDir=r"D:\Python\Classic_network\ssd-pytorch-master\ssd-pytorch-master\ssd-pytorch-master\VOCdevkit\VOC2007\JPEGImages" + "\\" #原图像路径
    xmlDir=r"D:\Python\Classic_network\ssd-pytorch-master\ssd-pytorch-master\ssd-pytorch-master\VOCdevkit\VOC2007\1" + "\\"#原xml路径
    new_xmlDir=r'D:\Python\Classic_network\ssd-pytorch-master\ssd-pytorch-master\ssd-pytorch-master\VOCdevkit\VOC2007\Annotations' #新xml路径
    xml(fileDir, xmlDir)
