import time
from multiprocessing import Process, Pipe

def pi_naive(start, end, step, conn):
    # print('Start Step:', str(start),'|', 'End Step:', str(end))
    sum = 0.0

    for i in range(start, end):
        x = (i+0.5) * step
        sum = sum + 4.0/(1.0+x*x)
    conn.send(sum * step)
    # print(sum * step)

if __name__ == '__main__':
    PROCS = 24

    a, b = Pipe()
    
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
        
        worker = Process(target=pi_naive, args=(step_start, step_end, step, a,))
        workers.append(worker)
        worker.start()

    for worker in workers:
        worker.join()
    
    result_list = []
    for i in range(PROCS):
        result_list.append(b.recv())
        
    print(result_list)
    final_sum = sum(result_list)
    # for i in result_list:
    #     final_sum += i
    
    print(final_sum)
    toc = time.time()
    # pi = step * sums
    # print('Valor Pi: %.10f'%pi)
    print('Tempo Pi: %.8f s'%(toc - tic))