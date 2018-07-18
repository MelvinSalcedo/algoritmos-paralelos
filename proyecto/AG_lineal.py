
import sys
from random import random
from operator import add
import copy
from random import randint
from time import time



tam_cromosomas=18 #multimplo de 3
tam_poblacion=4800;
num_iteracion=100000
test_set_size=0;
tam_inputFileColum=0

Pobacion=[]
Pobacion_fitness=[]

Legal_Searh=[]
Legal_Value=[]
Pair_Seach=[]

array_repetidos=[]
mejor_global=[[],100000]
suma=0

tam_Datos=10
def comprovar_enLegal_Values(x,y):
    for l in Legal_Value[x]:
        if int(f"{l}")==y:
            #print(x,y)
            return True
    return False
    #print("_______________")
def iniciar_matrizLs_pS_Lv():
    ff=[]
    contador_=0
    for i in range(tam_Datos):
    	p=10
    	f=[]
    	for x in range(p):
    		f.append(contador_)
    		contador_+=1
    	ff.append(f)


    global test_set_size
    global tam_inputFileColum
    global Legal_Searh
    #____________________________________
    for line in ff:
        temporal=[]
        tam_inputFileColum+=1
        for l in line:
           # if l.isdigit():
            temporal.append(l)
            if int(l)>test_set_size:
                test_set_size=int(l)
        Legal_Value.append(temporal)
    test_set_size+=1
    #print("LEGAL VALUE = ",Legal_Value)
    #print("TEST SET SIZE = ",test_set_size-1)
    #print("tam_inputFileColum value = ",tam_inputFileColum)
    #_______________________________
    for x in range(tam_inputFileColum):
        Legal_Searh.append([0]*test_set_size)
    #print(Legal_Searh)
    for x in range(tam_inputFileColum):
        for y in range(test_set_size):
            if comprovar_enLegal_Values(x,y)==True:
                #print(x,y)
                Legal_Searh[x][y]=1
    #print("LEGAL SEACH = ",Legal_Searh,"\n\n\n")
    #_______________________________
    for x in range(test_set_size):
        Pair_Seach.append([0]*test_set_size)

    #____________________________________

    for x in range(tam_inputFileColum-1):
        for l in range(len(Legal_Value[x])):

            for i in range(x+1,tam_inputFileColum):
                for j in range(len(Legal_Value[i])):
                    a=int(Legal_Value[x][l])
                    b=int(Legal_Value[i][j])
                    Pair_Seach[a][b]=1
                i+=1
    #____________________________________
    #print("PAIR SEARCH = ",Pair_Seach,"\n\n\n");
def comprovar_repeticion(a,b):
	for x in range(0,len(array_repetidos),3):
		if array_repetidos[x]==a and array_repetidos[x+1]==b:
			return True
		elif array_repetidos[x]==a and array_repetidos[x+2]==b:
			return True
		elif array_repetidos[x+1]==a and array_repetidos[x+2]==b:
			return True
	return False

def num_puntos_cruzamiwnto(puntos,lista):
	array_=[]
	for i in range(puntos):
		array_.append(randint(0,puntos))
	for i in range(puntos-1):
		temporal=lista[array[i]]
		lista[array[i]]=lista[array[i+1]]
		lista[array[i+1]]=temporal
	return lista

def validar_poblacion(dato,pos):
    for x in Legal_Searh[pos]:
        if Legal_Searh[pos][dato]==1:
            return True
    return False

def poblacion_inicial():
    for i in range(tam_poblacion):
        Pobacion.append([0]*tam_cromosomas)

    for p in range(tam_poblacion):
        contador=0
        for q in range(tam_cromosomas):
            while True:
                rand=randint(0,test_set_size-1)
                if validar_poblacion(rand,contador)==True:
                    Pobacion[p][q]=rand
                    break

            contador+=1
            if contador==3:
                contador=0
    print("POBLACION ",Pobacion,"\n\n\n")

def fitness(pob):
	suma_fitness=0
	for x in range(0,tam_cromosomas,3):
		if (comprovar_repeticion(pob[x],pob[x+1])==False):
			suma_fitness+=Pair_Seach[pob[x]][pob[x+1]]
		if (comprovar_repeticion(pob[x],pob[x+1])==False):
			suma_fitness+=Pair_Seach[pob[x]][pob[x+2]]

		if (comprovar_repeticion(pob[x],pob[x+1])==False):
			suma_fitness+=Pair_Seach[pob[x+1]][pob[x+2]]
		array_repetidos.append(pob[x])
		array_repetidos.append(pob[x+1])
		array_repetidos.append(pob[x+1])
	array_repetidos.clear()
	return suma_fitness

def mejor_global_(pob,count):
    pos=0
    for i in range(len(count)):
    	if(count[i]<mejor_global[1]):
    		mejor_global[1]=count[i]
    		pos=i
    mejor_global[0]=Pobacion[pos]

def asiganar_fitness_poblacion(count):
	for i in range(len(count)):
		Pobacion_fitness.append((Pobacion[i],count[i]))

def evolucion(iterator):	
	mayor=[]

	for x in iterator:
		mayor.append(x[0])
	#print(mayor)
	mayor_=len(mayor)-1
	if(mayor_==0):
		return mayor[0]
	it = 0
	
	while it<num_iteracion:
		padre1=randint(0,mayor_)
		padre2=0
		while (padre1==padre2):
			padre2=randint(0,mayor_)

		#print(padre1,"------",padre2)
		num_puntos_cruzamiwnto(iterator,2)
		#________________________________________-
		hijo=[0]*tam_cromosomas
		hijo1=[0]*tam_cromosomas
		#print(padre1,"/////////////////////////////////////////////",padre2)
		r0=int(tam_cromosomas/2)
		while ((r0 % 3)!=0):
			r0+=1
		#print(len(mayor[padre1]),"------> ",r0)
		for i in range(r0):
			hijo[i] =int(mayor[padre1][i])
			hijo1[i]=int(mayor[padre1][r0+i])
		for i in range(r0,tam_cromosomas):
			hijo[i]=int(mayor[padre2][i])
			hijo1[i]=int(mayor[padre1][i-r0])
		#print("/////////////////////////////////////////////")
		aaa=randint(0,tam_cromosomas-1)/2
		a=int(aaa)
		b=int(aaa+3)
		#print("\n\n",a,b,aaa,tam_cromosomas,"\n\n")
		temporal=int(hijo[a])
		hijo[a]=hijo[b]
		hijo[b]=temporal
		temporal=int(hijo1[a])
		hijo1[a]=hijo1[b]
		hijo1[b]=temporal
		#print("/////////////////////////////////////////////")
		#print(hijo1,hijo)
		#print("/////////////////////////////////////////////")
		fit_p=fitness(padre1)
		fit_p1=fitness(padre2)
		fit_h=fitness(hijo)
		fit_h1=fitness(hijo1)

		if(fit_h<fit_p):
			mayor[padre1]=hijo
		if(fit_h1<fit_p1):
			mayor[padre2]=hijo1
		it+=1
	mejor_local=mayor[0]
	for i in mayor:
		if(fitness(mejor_local)>fitness(i)):
			mejor_local=i

	return [mejor_local]

def evolucion_lineal(iterator,num):	
	mayor=[]

	for x in iterator:
		mayor.append(x[0])
	#print(mayor)
	mayor_=len(mayor)-1
	if(mayor_==0):
		return mayor[0]
	it = 0
	
	while it<num_iteracion*num:
		padre1=randint(0,mayor_)
		padre2=0
		while (padre1==padre2):
			padre2=randint(0,mayor_)

		#print(padre1,"------",padre2)
		#________________________________________-
		hijo=[0]*tam_cromosomas
		hijo1=[0]*tam_cromosomas
		#print(padre1,"/////////////////////////////////////////////",padre2)
		r0=int(tam_cromosomas/2)
		while ((r0 % 3)!=0):
			r0+=1
		#print(len(mayor[padre1]),"------> ",r0)
		for i in range(r0):
			hijo[i] =int(mayor[padre1][i])
			hijo1[i]=int(mayor[padre1][r0+i])
		for i in range(r0,tam_cromosomas):
			hijo[i]=int(mayor[padre2][i])
			hijo1[i]=int(mayor[padre1][i-r0])
		#print("/////////////////////////////////////////////")
		aaa=randint(0,tam_cromosomas-1)/2
		a=int(aaa)
		b=int(aaa+3)
		#print("\n\n",a,b,aaa,tam_cromosomas,"\n\n")
		temporal=int(hijo[a])
		hijo[a]=hijo[b]
		hijo[b]=temporal
		temporal=int(hijo1[a])
		hijo1[a]=hijo1[b]
		hijo1[b]=temporal
		fit_p=fitness(mayor[padre1])
		fit_p1=fitness(mayor[padre2])
		fit_h=fitness(hijo)
		fit_h1=fitness(hijo1)
		if(fit_h<fit_p):
			mayor[padre1]=hijo
		if(fit_h1<fit_p1):
			mayor[padre2]=hijo1
		it+=1
	mejor_local=mayor[0]
	for i in mayor:
		if(fitness(mejor_local)>fitness(i)):
			mejor_local=i

	return mayor

def mejor_global_total(count):
    for i in range(len(count)):
    	if(mejor_global[1]>fitness(count[i])):
    		mejor_global[0]=count[i]
    		mejor_global[1]=fitness(count[i])


def main():
	partitions = 4
	tiempo_inicial = time()
	n = 2 * partitions
	iniciar_matrizLs_pS_Lv()
	poblacion_inicial()
	matriz=[]
	count=[]
	print("hallando fitness")
	for i in Pobacion:
		count.append(fitness(i))
	print("calculando mejor global")
	mejor_global_(Pobacion,count)
	asiganar_fitness_poblacion(count)
	print("evolucion")
	mejor_indivual=evolucion_lineal(Pobacion_fitness,partitions)
	mejor_global_total(mejor_indivual)
	tiempo_final = time()
	tiempo_ejecucion = tiempo_final - tiempo_inicial
	print ('TIEMPO DE EJECUCION LINEAL :',tiempo_ejecucion)
	print(mejor_global[0],mejor_global[1])

if __name__ == "__main__":
    main()


