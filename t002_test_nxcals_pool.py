import time

t_fill_start = 1527662512.98
t_fill_end = 1527704298.4750001

varlist = ['QBBI_A31L2_TT824.POSST',
 'QQBI_13L5_TT824.POSST',
 'QBBI_B13R4_TT826.POSST',
 'QBBI_A34L5_TT826.POSST']

n_pool = 1


def get_data(vv):
    import pytimber
    #db = pytimber.LoggingDB(source='nxcals')
    # res = db.get([vv], t_fill_start, t_fill_end)
    res = vv
    print (res)
    return res

import multiprocessing as mp

def foo(q, vv):
    print(f'{vv} Here 0')
    import pytimber
    print(f'{vv} Here 1')
    #db = pytimber.nxcals.NXCals()
    db = pytimber.LoggingDB(source='nxcals',
            #sparkconf='large'
           ) 
    print(f'{vv} Here 2')
    t1 = time.time()
    res = db.get([vv], t_fill_start, t_fill_end)
    t2 = time.time()
    print(f'elapsed {t2-t1}s')
    print(f'{vv} Here 3')
    q.put(res)

if __name__ == '__main__':

    p_list = []
    q_list = []
    for ii in range(1):
        ctx = mp.get_context('spawn')
        q = ctx.Queue()
        p = ctx.Process(target=foo, args=(q,varlist[ii]))

        p_list.append(p)
        q_list.append(q)

    for p in p_list:
        p.start()

    data = [q.get() for q in q_list]

    for p in p_list:
        p.join()
