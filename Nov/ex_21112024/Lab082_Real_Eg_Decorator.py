# Time taken by 2 functions ,calculate using a decorator
import time


def time_taken(func):
    def wrapper():
        print("Starting time")
        start_time = time.time()
        print(start_time)
        func()
        print("Ending time")
        end_time = time.time()
        print(end_time)
        print("Total time taken by the function", end_time - start_time)
    return wrapper

def show_Logs(func):
    def wrapper():
        print("Starting Logs")
        func()
        print("Created Logs")
    return wrapper


@time_taken
@show_Logs
def test_UI_1():
    print("First function")
    time.sleep(2)
test_UI_1()
@time_taken
@show_Logs
def test_UI_2():
    print("Second function")
    time.sleep(5)

test_UI_2()