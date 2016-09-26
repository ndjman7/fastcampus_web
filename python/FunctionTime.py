import time

def hello(name):
    print("안녕하세요, 저는 {name}입니다.".format(name=name))

start_time = time.time()
hello("나대진")
end_time = time.time()
exec_time = end_time - start_time
print("Execute Time: {time}".format(time=exec_time))



# 함수를 리턴하는 함수
def track_time(func):
    def new_func(*args, **kwargs):
        start_time = time.time()
        func(*args,**kwargs)
        end_time = time.time()
        exec_time = end_time - start_time
        print("Excute Time: {time}".format(time=exec_time))
    return new_func

hello = track_time(hello)
hello("나대진")
