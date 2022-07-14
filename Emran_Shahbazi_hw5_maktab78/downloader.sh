#!/bin/bash

read url
wget $url
printf "$url" >> log.txt
