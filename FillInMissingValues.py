import copy
from scipy import spatial

def calc_probability( listOfList ):
    length = len(listOfList[0])
    probs = []
    
    for i in range(0,length):
        ones = 0
        zeroes = 0
        others = 0
        
        for j in range( 0, len(listOfList)  ):
            if ( listOfList[j] [i] == '0' ):
                zeroes += 1
            elif ( listOfList[j] [i] == '1' ):
                ones += 1

        prob_1 = ones/length
        prob_0 = zeroes/length

        probs.append( (prob_1,prob_0 ) )
 
    return probs


def calc_similarity(list1,list2):
    matches = 0
    mis_matches = 1

    for i,j in zip( list1, list2) :
        if ( i == j ):
            matches += 1
        else:
            mis_matches += 1

    return ( matches/mis_matches)
        
f = open ( "hey.csv" , "r")
f2 = open( "results.csv", "w");

line = []
for i in f:
    line.append(i.strip().split(','))


probs = calc_probability(line)
innn = copy.deepcopy(line)


result0 = []

for inn in innn:
    inn_soln = copy.deepcopy(inn)

    query = []
    for i in range(0, len(inn) ):
        if( inn[i] == '-' ):
            query.append(i)       

    max_sim = 0
    answer = 0

    print ( query )

    for i in line:
        similarity = calc_similarity(i,inn)
        print ( "similarity score" + str(similarity) )
        if ( similarity  > max_sim):
            max_sim = similarity
        for  q in query :
            if ( i[q] != '-' ):
                if ( probs[q][0] >= 0.6 ):
                    inn_soln[q] = '1'
                elif ( probs[q][1] >= 0.6 ):
                    inn_soln[q] = '0'
                else:
                    inn_soln[q] = i[q]

            if ( inn_soln[q] == '-' ):
                if ( probs[q][0] >= 0.6 ):
                    inn_soln[q] = '1'
                elif ( probs[q][1] >= 0.6 ):
                    inn_soln[q] = '0'                
    


                    
    result0.append(inn_soln)
    print( inn_soln) 
    f2.write(','.join(inn_soln) +"\n")

f.close()
f2.close()



                                                    

    

                                                            
                                            
                                                    
                                            
