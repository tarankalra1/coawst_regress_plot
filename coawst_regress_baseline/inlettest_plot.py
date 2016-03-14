import util_plot
import os
import sys 

def plot_sandy(pdf):
    inlet_tests=os.listdir(os.path.join(code_path,'Projects/Inlet_test'))
 26     ignored = ['.svn']
 27     inlet_tests= [x for x in inlet_tests if x not in ignored]
 28 
 29     print "----------------------------------------------"
 30     print " INLET TEST CASES INCLUDED:", inlet_tests
 31 
 32     for each_inlet_case in inlet_tests:
 33         project_str='Projects/Inlet_test'+'/'+each_inlet_case
 34         project_subpath=os.path.join(code_path,project_str)
 35 

    his_name='Sandy_ocean_his.nc'
    testcase='Sandy'
    path_his_old, path_his_new=os.path.join(util_plot.get_result_path())
    path_his_old=path_his_old+'/Projects/'+testcase+'/'+his_name
    path_his_new=path_his_new+'/Projects/'+testcase+'/'+his_name
    if os.path.isfile(path_his_old) and os.path.isfile(path_his_new):
        print "------------------------------------------------------------"
        print "The history file from OLDER COAWST regression run for",testcase,"case is",path_his_old
        print "------------------------------------------------------------"
        print "The history file from NEW COAWST regression run for",testcase,"case is",path_his_new
        """ set the contour levels for zeta plots """
        colormin=-1.3
        colormax=0.9
        xmin=-82.0
        xmax=-65.0
        ymin=27.5
        ymax=43.0 
        """ call the function for zeta (water level) plots """
        util_plot.plot_zeta(pdf,path_his_old,path_his_new,his_name,testcase,xmin,xmax,\
                         ymin,ymax,colormin,colormax)
    else:
        print "-------------------xx---------------------------------------"
        print "One or both HISTORY files for", testcase, "don't exist in the path"
