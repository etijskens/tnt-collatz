# file env.sh
# You must source this file: `> source env.sh`

# start from clean environment
module purge
module load $VSC_INSTITUTE_CLUSTER/supported # (this may not work on all VSC clusters,
                                             # but it does on the Uantwerpen clusters)
# load modules needed for Python
module load Python     # also numpy, scipy, sympy, pandas, matplotlib, mpi4py, 
                       # C/C++ and Fortran compilers …
module load numba
module load buildtools # Cmake (needed by micc2)
module load git
module load gh         # (needed by micc2)
module list            # list all loaded modules

# allow to install python packages locally using `pip install --user`
export PYTHONUSERBASE=/scratch/antwerpen/201/vsc20170/.local
mkdir -p ${PYTHONUSERBASE}
export PATH="$PATH:${PYTHONUSERBASE}/bin"
