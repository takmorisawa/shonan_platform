#!/bin/sh

scp -r -i /Users/tkyk/.ssh/MyKeyPair.pem build ec2-user@18.216.105.170:/home/ec2-user/repo/shonan_platform/my-app
