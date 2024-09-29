# Installation Conda WSL and library

**Reference**
- Official : https://docs.anaconda.com/anaconda/install/linux/

**Execution step**

1. Use wget
2. Activate on your directory`source /home/tridsanu/anaconda3/bin/activate`

# Creating Virtual ENV

**Execution step**

1. Create ENV : `conda create --name quant python=3.8` (from previous)
2. Activate : `conda activate quant`
3. Tell all ENV : `conda info --envs`
4. Installed Lib :
   -  Spyder : `conda install -c anaconda spyder`
       -   For using need to run `spyder --new-instance`
   -  Pandas : `conda install anaconda::pandas`
5. Deactivate : `conda deactivate`