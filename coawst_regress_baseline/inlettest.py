import util
import os
import sys 
import shutil 
import subprocess
import time 

def regress_inlet(code_path):
    case_name       ='Inlet_test'
    base_bashfile   ='coawst.bash'
    base_runfile    ='run_nemo'
    couple_flag     ='2way'
    ntilex          = 2
    ntiley          = 2
    ntilex_ref      = "2  2"            #This is for "Refined" mesh 
    ntiley_ref      = "2  2"            #This is for "Refined" mesh 
    nocn            = ntilex*ntiley
    nwav            = 4
    natm            = 0
    tot_nproc       = nocn+nwav+natm
    nodes           = 1                 # for NEMO, ppn = 8 
    executable      = 'coawstM'
    buildfile       = 'Build.txt'

    inlet_tests=os.listdir(os.path.join(code_path,'Projects/Inlet_test'))    
    ignored = ['.svn']
    inlet_tests= [x for x in inlet_tests if x not in ignored]

    print "----------------------------------------------"
    print " INLET TEST CASES INCLUDED:", inlet_tests

    for each_inlet_case in inlet_tests: 
        project_str='Projects/Inlet_test'+'/'+each_inlet_case
        project_subpath=os.path.join(code_path,project_str)
        
        os.chdir(code_path)

        bashfile  = base_bashfile + '_inlet_' + each_inlet_case
        shutil.copy2(base_bashfile,bashfile)

        runfile   = base_runfile + '_inlet_' + each_inlet_case
        shutil.copy2(base_runfile,runfile)
       
        """ Edit 'coawst.bash' for each case """
        util.edit_bashfile(bashfile,case_name,code_path,project_subpath)     

        os.system('./%(bashfile)s  >>Build.txt 2>&1' %locals() )
        print "------------------------------------------"
        print "Finished compiling Inlet test:", each_inlet_case
       
        case_subname = "Inlet_test_" + each_inlet_case

        if each_inlet_case == 'DiffGrid': 
            inputfile='coupling_inlet_test_diffgrid.in' 
	    oceaninfile='ocean_inlet_test.in'
            couplefile=inputfile 
            util.edit_jobscript(runfile,inputfile,case_subname,project_str,\
                                code_path,tot_nproc,nodes)    

            os.chdir(project_subpath)
            util.edit_couplefile(couplefile,natm,nwav,nocn,couple_flag)
            util.edit_oceaninfile(oceaninfile,ntilex,ntiley)

            os.chdir(code_path)
 
            print "------------------------------------------"
            print "Executing Inlet_test:", each_inlet_case 
            p=subprocess.Popen("qsub %(runfile)s" %locals(),shell=True,    \
                                stdout=subprocess.PIPE,stderr=subprocess.PIPE)
            stdout,stderr=p.communicate()
           
            #check every ten mins
            stdout_case=stdout 
            util.check_queue(stdout_case)
          
            logfile = 'log.out_' + case_subname

            #   Moving output files to each projects folder
            util.move_casefiles(project_subpath,case_subname,bashfile,runfile,\
                                buildfile,executable,stdout,logfile)

        elif each_inlet_case == 'Coupled': 
            inputfile='coupling_inlet_test.in' 
            oceaninfile='ocean_inlet_test.in'
            couplefile=inputfile 
            util.edit_jobscript(runfile,inputfile,case_subname,project_str,\
                                code_path,tot_nproc,nodes)    
          
            os.chdir(project_subpath)
            util.edit_couplefile(couplefile,natm,nwav,nocn,couple_flag)
            util.edit_oceaninfile(oceaninfile,ntilex,ntiley)

            os.chdir(code_path)

            print "------------------------------------------"
            print "Executing Inlet_test:", each_inlet_case 
            p=subprocess.Popen("qsub %(runfile)s" %locals(),shell=True,     \
                               stdout=subprocess.PIPE,stderr=subprocess.PIPE)
            stdout,stderr=p.communicate()

            #check every ten mins
            stdout_case=stdout 
            util.check_queue(stdout_case)

            logfile = 'log.out_' + case_subname

            #   Moving output files to each projects folder
            util.move_casefiles(project_subpath,case_subname,bashfile,runfile,\
                                buildfile,executable,stdout,logfile)

        elif each_inlet_case == 'Refined':
            inputfile='coupling_inlet_test_ref3.in' 
            oceaninfile='ocean_inlet_test_ref3.in'
            couplefile=inputfile 
            util.edit_jobscript(runfile,inputfile,case_subname,project_str,\
                                code_path,tot_nproc,nodes)    

            os.chdir(project_subpath)
            util.edit_couplefile(couplefile,natm,nwav,nocn,couple_flag)
# For refined case the ocean file function is changed in the same script
            util.edit_ref_oceaninfile(oceaninfile,ntilex_ref,ntiley_ref)

            os.chdir(code_path)

            print "------------------------------------------"
            print "Executing Inlet_test:", each_inlet_case 
            p=subprocess.Popen("qsub %(runfile)s" %locals(),shell=True,     \
                               stdout=subprocess.PIPE,stderr=subprocess.PIPE)
            stdout,stderr=p.communicate()

            #check every ten mins
            stdout_case=stdout 
            util.check_queue(stdout_case)

            logfile = 'log.out_' + case_subname

            #   Moving output files to each projects folder
            util.move_casefiles(project_subpath,case_subname,bashfile,runfile,\
                                buildfile,executable,stdout,logfile)

        elif each_inlet_case == 'Swanonly': 
            inputfile='swan_inlet_test.in' 
            util.edit_jobscript(runfile,inputfile,case_subname,project_str,\
                                code_path,tot_nproc,nodes)    

            print "------------------------------------------"
            print "Executing Inlet_test:", each_inlet_case 
            p=subprocess.Popen("qsub %(runfile)s" %locals(),shell=True,      \
                                stdout=subprocess.PIPE,stderr=subprocess.PIPE)
            stdout,stderr=p.communicate()

            #check every ten mins
            stdout_case=stdout 
            util.check_queue(stdout_case)

            logfile = 'log.out_' + case_subname

            #   Moving output files to each projects folder
            util.move_casefiles(project_subpath,case_subname,bashfile,runfile,\
                                buildfile,executable,stdout,logfile)
