import util_plot
import os
import sys 

def plot_estuary_test2(pdf):
    his_name='ocean_estuary2_his.nc'
    testcase='Estuary_test2'
    path_his_old, path_his_new=os.path.join(util_plot.get_result_path())
    path_his_old=path_his_old+'/Projects/'+testcase+'/'+his_name
    print "------------------------------------------------------------"
    print "The history file from older COAWST regression run for",testcase,"case is",path_his_old
    path_his_new=path_his_new+'/Projects/'+testcase+'/'+his_name
    print "------------------------------------------------------------"
    print "The history file from new COAWST regression run for",testcase,"case is",path_his_new
    print "------------------------------------------------------------"
      
    """ set the contour levels for zeta plots """
    colormin=-0.6
    colormax=0.0
    xmin=-0.8
    xmax=0.0
    ymin=-0.01
    ymax=0.01  
    """ call the function for zeta (water level) plots """
    util_plot.plot_zeta(pdf,path_his_old,path_his_new,his_name,testcase,xmin,xmax,\
                        ymin,ymax,colormin,colormax)

