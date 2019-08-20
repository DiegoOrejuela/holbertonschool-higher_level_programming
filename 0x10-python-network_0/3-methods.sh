#!/bin/bash
#Write a Bash script that takes in a URL and displays all HTTP methods the server will accept
sudo curl -sD - $1 -o /dev/null | grep Allow | cut -d " " -f 2-
  
