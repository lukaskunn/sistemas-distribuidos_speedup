from time import perf_counter_ns
import simples as sp
import mtrhead as mt

with open("data.csv") as file:
    data = [line.strip() for line in file]

data = list(map(int, data))

arrThreads = [2, 5, 10, 15, 20, 25]

#print('\n\nanalise de %d valores\n\n'%(len(data)))
for i in arrThreads:

    totalSimples = 0
    totalThreads = 0

    for j in range(0, 50):

        print(f'j atual: {j}')

        start1 = perf_counter_ns()
        primo_sp = sp.resolve_simples(data)
        finish1 = perf_counter_ns()

        start2 = perf_counter_ns()
        primo_mt = mt.resolve_trhread(data, i)
        finish2 = perf_counter_ns()

        totalSimples += (finish1-start1)/1000000
        totalThreads += (finish2-start2)/1000000
    
    mediaSimples = totalSimples/50
    mediaThreads = totalThreads/50
    melhoriaTotal = mediaSimples - mediaThreads

    print(f'numero de threads atual: {i}')
    print(f'melhoria total: {melhoriaTotal}')
    print(f'media simples: {mediaSimples}')
    print(f'media threads: {mediaThreads}\n')
    

#print('simples          > threads')
#print('%f ms   > %f ms  : tempo execucao'%((finish1-start1)/1000000,(finish2-start2)/1000000))
#print('%d            > %d           :numeros primos encontrados'%(primo_sp,primo_mt))