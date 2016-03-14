import util
import os
import sys 
import shutil 
import trench
import estuary_test2
import wetdry
import ducknc 
import speclight
import sedbed_toy 
import sed_floc_toy 
import sandy
import ripcurrent
import inlettest
import joetc
import shoreface 

def setup_testcase():
    """Create everything needed to run a testcase

    Takes testcase name and creates compiled exe and new bash script
    """
    code_path = util.get_coawst()
    print "----------------------------------------------"
    print " The source code is located in:", code_path

    """ This is the order in which test cases run """

    trench.regress_trench(code_path) 
    estuary_test2.regress_estuary_test2(code_path)
    wetdry.regress_wetdry(code_path)
    ducknc.regress_ducknc(code_path) 
    speclight.regress_speclight(code_path) 
    sedbed_toy.regress_sedbed_toy(code_path) 
    sed_floc_toy.regress_sed_floc_toy(code_path) 
    ripcurrent.regress_ripcurrent(code_path) 
    inlettest.regress_inlet(code_path) 
    joetc.regress_joetc(code_path) 
    sandy.regress_sandy(code_path) 
    shoreface.regress_shoreface(code_path)
