import random

m = 7
poblacion_total = []
poblacion_1 = []
poblacion_2 = []
var1_size = 4
var2_size = 4

# generacion de invidviuos

def decodif(my_codif):
	chain_size =  len(my_codif)
	var_val = 0
	for i in range(0, chain_size):
		var_val += (2**(chain_size - 1 - i))*my_codif[i]		
	return var_val

def gen_sub_pobl(poblaciom_total):
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

def gen_sub_indiv(idx, poblacion_total):
        current = poblacion_total[idx]
        candidate = []
        nuevo_individuo = []
        for j in range(0, var1_size):
                nuevo_individuo.append(current[j])
        candidate.append(nuevo_individuo)
        nuevo_individuo = []
        for j in range(var1_size, var1_size + var2_size):
                nuevo_individuo.append(current[j])
        candidate.append(nuevo_individuo)
        return candidate


def calc_function(var1, var2):
    return (13*(var1 - 2)*(var1 - 2)) + 8*(var2 - 1)*(var2 - 1)

def tournament(my_pob):
    tournament_size = 2
    tmp1 = -1
    tmp2 = -1
    while(tmp1 == tmp2):
        tmp1 = random.randint(0,m - 1)
        tmp2 = random.randint(0,m - 1)
    val_vars1 = gen_sub_indiv(tmp1, my_pob)
    val_vars2 = gen_sub_indiv(tmp2, my_pob)
    calc1 = calc_function(decodif(val_vars1[0]), decodif(val_vars1[1]))
    calc2 = calc_function(decodif(val_vars2[0]), decodif(val_vars2[1]))
    if calc1 > calc2:
            return my_pob[tmp1]
    else:
            return my_pob[tmp2]

def crossover(my_pob):
    for j in range(0,len(my_pob)):
        indiv1 = tournament(my_pob)
        indiv2 = tournament(my_pob)
        print indiv1, "vs", indiv2
        new_indiv = []
        uniform_rate = 0.5
        for i in range(0,len(indiv1)):
            tmp = random.uniform(0,1)
            if(tmp > uniform_rate):
                new_indiv.append(indiv1[i])
            else:
                new_indiv.append(indiv2[i])
        print "bef_indiv", my_pob[j]
        my_pob[j] = new_indiv
        print "new_indiv", my_pob[j]
    return my_pob

def mutate(my_pob):
    mutation_rate = 0.015
    uniform = 0.5
    for j in range(0,len(my_pob)):
        current_ind = my_pob[j]
        for i in range(0,len(current_ind)):
            if(random.uniform(0,1) < mutation_rate):
                tmp = random.uniform(0,1)
                if(tmp < uniform):
                    current_ind[i] = 0
                else:
                    current_ind[i] = 1
        my_pob[j] = current_ind

    

for i in range(0,m):
	b = random.randint(1,6)
	new_codif = [0,0,0,0,0,0,0,0]
	last_bit_changed = -1
	for j in range(0,b):
		bit_to_change = random.randint(0,7)
		while(new_codif[bit_to_change] == 1):
			bit_to_change = random.randint(0,7)
		new_codif[bit_to_change] = 1
	poblacion_total.append(new_codif)

gen_sub_pobl(poblacion_total)
print poblacion_total
print poblacion_1
print poblacion_2

for i in range(0, var1_size):
	print "variable 1, individuo ",i,": ", decodif(poblacion_1[i])

for i in range(0, var2_size):
	print "variable 2, individuo ",i,": ", decodif(poblacion_2[i])

#cruzamiento
poblacion_total = crossover(poblacion_total)
print poblacion_total
poblacion_1 = []
poblacion_2 = []
gen_sub_pobl(poblacion_total)
print " "
for i in range(0, var1_size):
	print "variable 1, individuo ",i,": ", decodif(poblacion_1[i])

for i in range(0, var2_size):
	print "variable 2, individuo ",i,": ", decodif(poblacion_2[i])

