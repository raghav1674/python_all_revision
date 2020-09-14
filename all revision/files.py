# f=open("myfile.txt","a+")
# f.write("hello")
# f.close()

#
# f=open("myfile.txt","r")
# lines=f.readline()
# print(lines)
# for line in lines:
#     print(line)

# import pickle,student
# f=open("student.dat","wb")
#
# s=student.Student("RAGHAV",20)
# pickle.dump(s,f)
# f.close()

# import pickle,sys,os,logging
# logging.basicConfig(filename="mystudent.log",level=logging.DEBUG)
# logging.warning("OPENING FILE")
# if os.path.isfile("student.dat"):
#     f=open("student.dat","rb")
# else:
#
#     sys.exit()
# obj=pickle.load(f)
# print(obj)
# f.close()