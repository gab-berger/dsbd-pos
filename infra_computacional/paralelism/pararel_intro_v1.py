from multiprocessing import Process

def f(name, id):
    print('hello, i am', name)

if __name__ == '__main__':
    p = Process(target=f, args=('gabs',))
    p.start()
    p.join()