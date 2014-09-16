# MCL Clustering

Python implementation of Markov Clustering technique.
This implementation si not yet optimized for large networks.

## Installation:

    python setup.py install

##Usage:

###Command line:

    Usage: ./mcl_clustering.py [options] <input_file> <output_file>


    Options:
      -h, --help            show this help message and exit
      -e EXPAND_FACTOR, --expand_factor=EXPAND_FACTOR
                            expand factor (default: 2)
      -i INFLATE_FACTOR, --inflate_factor=INFLATE_FACTOR
                            inflate factor (default: 2)
      -m MULT_FACTOR, --mult_factor=MULT_FACTOR
                            multiply factor (default: 1)
      -l MAX_LOOP, --max_loops=MAX_LOOP
                            max loops (default: 60)



###Code:
        
        numpy adjacency matrix
    
            from mcl_clustering import mcl
        
            A = <your matrix>

            M, clusters = mcl(A, expand_factor = options.expand_factor,
                               inflate_factor = options.inflate_factor,
                               max_loop = options.max_loop,
                               mult_factor = options.mult_factor)

        networkx graph

            from mcl_clustering import networkx_mcl

            G = <your graph>
    
            M, clusters = networkx_mcl(G, expand_factor = options.expand_factor,
                               inflate_factor = options.inflate_factor,
                               max_loop = options.max_loop,
                               mult_factor = options.mult_factor)
        
            
        Output:
            M = otuput matrix
            clusters = dict with keys = [<cluster id>] values = [<vertex id>]

##Requirements
    
        numpy
        networkx


##Example:



##Parameters:

    -i --inflate-factor
    -e --expand-factor
    -m --multiply-factor
    -l --max-loops
    -s --show-graph     show graph with networkx



## References

      Stijn van Dongen, Graph Clustering by Flow Simulation.
      PhD thesis, University of Utrecht, May 2000.
      ( http://www.library.uu.nl/digiarchief/dip/diss/1895620/inhoud.htm )

      Stijn van Dongen. A cluster algorithm for graphs.  Technical Report
      INS-R0010, National Research Institute for Mathematics and Computer
      Science in the Netherlands, Amsterdam, May 2000.
      ( http://www.cwi.nl/ftp/CWIreports/INS/INS-R0010.ps.Z )

