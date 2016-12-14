#!/bin/bash

m=$1
n=$2

target=${3:-"/home/ajdin/Repositories/dva336/project/data/generated_"$1"_"$2".txt"}

python2 generator.py $1 $2 > $target && tail $target

