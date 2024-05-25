import time
from multiprocessing import Process, Value

def pi_naive(start, end, step, val):
    # print('Start Step:', str(start),'|', 'End Step:', str(end))
    sum = 0.0

    for i in range(start, end):
        x = (i+0.5) * step
        sum = sum + 4.0/(1.0+x*x)
    
    with val.get_lock():
        val.value += (sum * step)
        # print(sum * step)

if __name__ == '__main__':
    PROCS = 24

    val_pi = Value('f', 0, lock=True)
    
    num_steps = 100_000_000
    step = 1.0/num_steps
    proc_size = num_steps // PROCS
    tic = time.time()
    
    sums = 0.0
    workers = []
    for id in range(PROCS):
        id_sum = 0.0
        step_start = id*proc_size
        step_end = (id+1)*proc_size-1
        
        worker = Process(target=pi_naive, args=(step_start, step_end, step, val_pi, ))
        workers.append(worker)
        worker.start()

    for worker in workers:
        worker.join()
    
    pi = val_pi.value
    
    toc = time.time()
    print('Valor Pi: %.10f'%pi)
    print('Tempo Pi: %.8f s'%(toc - tic))