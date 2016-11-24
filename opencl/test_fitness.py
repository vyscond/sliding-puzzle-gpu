from lordran import platform_selector       as ps
from lordran import sliding_puzzle_parallel as spp
   
def init_pop( context , random_list , puzzle ):
    
    return spp.InitialPopulationGeneratorEnhanced( context ).execute( ps.Execution.ASYNC , random_list , [ -1 , puzzle.move_top , 1 , puzzle.move_bot ] )
    
if __name__ == '__main__' :
    
    #~ puzzle = spp.Puzzle( range( 9 ) )
    
    puzzle = spp.Puzzle( [1,0,2,3,4,5,6,7,8] )
    
    context = ps.get_intel_context()
    
    import time
    
    population , offset_list , max_chromossome_size = init_pop( context , range(1,10000) , puzzle )    
    
    a = time.time()
    
    # ( self , execution_mode , chromossome_list , chromossome_offset_list , chromossome_max_size , problem_instance ):
    #~ spp.FitnessEnhanced( context , True ).execute( 0 , population , offset_list , max_chromossome_size , [1,0,2,3,4,5,6,7,8] )
    #fitness_results , chromossome_list , chromossome_offset_list = 
    spp.FitnessEnhanced( context , False ).execute( 0 , population , offset_list , max_chromossome_size , puzzle )
    
    a = time.time() - a
    
    print '-->[ Finish at : ' , ( a / 60 ) , ']'
    
    #~ for x in fitness_results :
        
        #~ print x
        
    
    # this is the last thing that you need to do ;)
    # implement on CPU DEBUG RP fitness, ok? VryHppy :3

    # ( invalid_positions_remaining ** 4 ) - ( valid_moves_qtt * 2 )
