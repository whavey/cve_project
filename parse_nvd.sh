#!/bin/bash

function process_nvd {
  echo "Processing nvd json"
  echo "-------------------"

  ./nvd_preprocess.py

  sed -i "s/\"/rep_/g" split_files/*
  sed -i "s/'/\"/g" split_files/*
  sed -i "s/rep_/'/g" split_files/*

  for i in `ls ./split_files`;do
    echo "" >> ./split_files/$i
  done
}

function setup_elastic {
  echo "Setting up database"
  echo "-------------------"

  sysctl -w vm.max_map_count=262144
  docker-compose up -d

  echo
  echo "Checking logstash status..."
  docker-compose logs -f logstash | grep pipeline
}

function argv {
    for a in ${BASH_ARGV[*]} ; do
      echo -n "$a "
    done
    echo
}

$1
