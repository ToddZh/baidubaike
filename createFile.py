import os
import time


def createF(s):
	filePath = "./new/"
	state = os.path.exists(filePath)  # 判断路径是否存在
	if state:
		print("File Exist!")
	else:
		os.makedirs(filePath)  # 创建目录

	for i in range(1, s + 1):
		localTime = time.strftime("%Y%m%d%H%M%S", time.localtime())
		fileName = 'TEST_' + str(localTime) + '.txt'

		#        f=open("E:\\LearnPython\\JpgFile\\fileName",'a')
		#        testNote='测试文件'
		#        f.write(testNote)
		#        f.close()

		with open(filePath + fileName, 'w') as f:  # open()函数可以判断文件是否存在，如果不存在，则创建文件
			testNote = 'test'
			f.write(testNote)

		print("file" + str(i) + ":" + fileName)
		time.sleep(1)

	print("ALL Down!")
	time.sleep(1)


if __name__ == '__main__':
	s = int(input("请输入需要生成的文件数："))
	createF(s)