import multiprocessing as mp

print(mp.get_start_method())

def sum_square(number):
    return sum(i*i for i in range(number))

mp.set_start_method('fork', force=True)
p = mp.Pool(8)
# p = mp.get_context("fork").Pool(8)

input = [1, 2, 3, 4, 5, 6, 7, 8]
results = p.map(sum_square, input)
p.close()
print(results)