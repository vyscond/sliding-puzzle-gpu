from lordran import platform_selector       as ps
from lordran import sliding_puzzle_parallel as spp
   
def init_pop( context , random_list ):
    
    chromossome_list_itself , chromossome_size_list , chromossome_max_size = spp.InitialPopulationGeneratorEnhanced( context , True ).execute( ps.Execution.SYNC , random_list , [ -1 , -3 , 1 , 3 ] )

    for chromossome in chromossome_list_itself :

        print '[python][test_routine][population generator] ' , chromossome

    exit( 0 )

if __name__ == '__main__' :
     
    context = ps.get_intel_context()

    import time
    
    a = time.time()

    population , list_size , max_size = init_pop( context , range(1,10) )
   
    a = time.time() - a
    
    print '-->[ Finish at : ' , ( a / 60 ) , ']'


