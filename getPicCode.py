import re
# ~ 选取想要提取的文件
content=open('main.js','r+',encoding='utf-8')
l=content.readlines()

patternFirstLine=re.compile('prototype\._getBGTexture')
patternEnd=re.compile('return PIXI\.Texture\.EMPTY')
patternPicNum=re.compile('case (\d{3})')
nums=0
#获取画图部分的第一行编号
for i in range(len(l)):
	rs=patternFirstLine.findall(l[i])
	if rs:
		firstLine=i
		break
#获取画图部分最后一行编号
for i in range(firstLine,len(l)):
	rs=patternEnd.findall(l[i])
	rsPicNum=patternPicNum.findall(l[i])
	#获取图片编号
	if rsPicNum:
		picNum=rsPicNum[0][:-1]
	if rs:
		nums+=1
	if nums==3:
		lastLine=i
		break

def filterFirstLine(arr):#处理第一行
	for i in range(len(arr)):
		if arr[i]=='_':
			return arr[i:]
l[firstLine]=filterFirstLine(l[firstLine])

#写入文件
file=open('filteredPicCode.txt','w',encoding='utf-8')
file.write(l[firstLine])
#处理},的换行
patternPrototype=re.compile('prototype')
for i in range(firstLine+1,lastLine+3):
	rs=patternPrototype.findall(l[i])
	if rs:
		temp=l[i].split('},')
		file.write('        },\n')
		file.write(temp[1])
	else:
		file.write(l[i])
print('picNum='+picNum)		
print('Code is filtered')
