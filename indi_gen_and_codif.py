import random

m = 5
poblacion_total = []
poblacion_1 = []
poblacion_2 = []
var1_size = 4
var2_size = 4

def decodif(my_codif):
	chain_size =  len(my_codif)
	var_val = 0
	for i in range(0, chain_size):
		var_val += (2**(chain_size - 1 - i))*my_codif[i]		
	return var_val
for i in range(0,m):
	b = random.randint(1,6)
	new_codif = [0,0,0,0,0,0,0,0]
	last_bit_changed = -1
	print b
	for j in range(0,b):
		bit_to_change = random.randint(0,7)
		while(new_codif[bit_to_change] == 1):
			bit_to_change = random.randint(0,7)
		new_codif[bit_to_change] = 1
	poblacion_total.append(new_codif)

for i in range(0,m):
	current = poblacion_total[i]
	nuevo_individuo = []
	for j in range(0, var1_size):
		nuevo_individuo.append(current[j])
	poblacion_1.append(nuevo_individuo)

for i in range(0,m):
	current = poblacion_total[i]
	nuevo_individuo = []
	for j in range(var1_size, var1_size + var2_size):
		nuevo_individuo.append(current[j])
	poblacion_2.append(nuevo_individuo)



print poblacion_total
print poblacion_1
print poblacion_2

for i in range(0, var1_size):
	print "variable 1, individuo ",i,": ", decodif(poblacion_1[i])

for i in range(0, var2_size):
	print "variable 2, individuo ",i,": ", decodif(poblacion_2[i])
