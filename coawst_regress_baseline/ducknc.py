import util
import os
import sys 
import shutil 
import subprocess 

def regress_ducknc(code_path):
    case_name       ='Ducknc'
    base_bashfile   ='coawst.bash' 
    base_runfile    ='run_nemo'
    oceaninfile     ='ocean_%s.in' % (case_name.lower())
    project_str     ='Projects'+'/'+case_name
    project_path    =os.path.join(code_path,project_str)
    case_subpath    =project_path # this is different for case within a subfolder
    couple_flag     ='1way'
    ntilex          = 4
    ntiley          = 2
    tot_nproc       = ntilex*ntiley
    nodes           = 1                 # for NEMO ppn=8
    execute         = 'coawstM'
    logfile         = 'log.out_' + case_name
    buildfile       = 'Build.txt'

    os.chdir(code_path)
    """ Make local copies for each case """
    bashfile  = base_bashfile + "_" + case_name 
    shutil.copy2(base_bashfile,bashfile)
      
    runfile   = base_runfile + "_" + case_name
    shutil.copy2(base_runfile,runfile)
 
    util.edit_bashfile(bashfile,case_name,code_path,project_path)

    print "------------------------------------------"
    print "Compiling:", case_name,"case"
    os.system('./%(bashfile)s >>Build.txt 2>&1' %locals() )

    util.edit_jobscript(runfile,oceaninfile,case_name,project_str,code_path,\
                        tot_nproc,nodes)

    os.chdir(project_path)
    util.edit_oceaninfile(oceaninfile,ntilex,ntiley)

    os.chdir(code_path)
    print "------------------------------------------"
    print "Executing test :", case_name
    p=subprocess.Popen("qsub %(runfile)s" %locals(),shell=True,stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE) 
    stdout,stderr=p.communicate()
 
#check every ten mins
    stdout_case=stdout
    util.check_queue(stdout_case)

#   Moving output files to each projects folder
    util.move_casefiles(project_path,case_name,bashfile,runfile,buildfile, \
                        execute,stdout,logfile)
