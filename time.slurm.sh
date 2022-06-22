#! /bin/bash
#
#SBATCH --job-name=OpenMP-demo
#SBATCH --ntasks=1 --cpus-per-task=1
#SBATCH --time=10:00

# Build the environment
source $VSC_SCRATCH/IIp/bin/iip-env.sh

python time.py