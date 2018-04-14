## update anaconda
    conda update conda
    conda update anaconda

## update
    conda update <packageName>

## check environment
    conda info -e

## create new environment
    conda create -n <envName> python=2.7
    conda create -n <envName> numpy matplotlib python=2.7

## switch environment
    # 切换到新环境# linux/Mac下需要使用source activate env_name
    activate env_name
    #退出环境，也可以使用`activate root`切回root环境
    deactivate env_name
## remove environment
    conda remove --name <envName> package_name