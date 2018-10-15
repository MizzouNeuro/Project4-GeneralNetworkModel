#!/bin/bash

#SBATCH -p Lewis,hpc5
#SBATCH -N 1

#SBATCH -n 10
#SBATCH --qos=normal
#SBATCH --job-name=BLA
#SBATCH --output=bla%j.out

#SBATCH --time 0-00:30

module load intel/intel-2016-update2
module load nrn/nrn-mpi-7.4
module load openmpi/openmpi-2.0.0

module list
echo "Starting simulation at $(date)"


mpirun nrniv -mpi main.hoc


echo "Simulation complete at $(date)"
