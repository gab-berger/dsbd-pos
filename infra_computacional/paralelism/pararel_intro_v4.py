import time
from multiprocessing import Process

def pi_naive(start, end, step):
    print('Start: ', str(start))
    print('End: ', str(end))
    sum = 0.0

    for i in range(start, end):
        x = (i+0.5) * step
        sum = sum + 4.0/(1.0+x*x)
    print(sum)

if __name__ == '__main__':
    num_steps = 1_000_000_00
    sums = 0.0
    step = 1.0/num_steps
    tic = time.time()

    proc_n = 4
    for id in range(proc_n):
        id_sum = 0.0
        id_start = int(id*proc_n//step)
        id_end = int(((id+1)*proc_n//step)-1)
        
        p = Process(target=pi_naive, args=(id_start, id_end, step,))
        p.start()
        
    toc = time.time()
    # pi = step * sums
    # print('Valor Pi: %.10f'%pi)
    # print('Tempo Pi: %.8f s'%(toc - tic))