#!/bin/bash

kill -15 $(ps aux | grep CLASSIFIER | awk '{ print $2 }' | head -n 1)
kill -15 $(ps aux | grep CONTEXT_ENGINE | awk '{ print $2 }' | head -n 1)
kill -15 $(ps aux | grep BOT | awk '{ print $2 }' | head -n 1)
