#!bin/bash

nohup python classifier_daemon.py -CLASSIFIER &
nohup python context_engine_daemon.py -CONTEXT_ENGINE &
nohup python daemon.py -BOT &
