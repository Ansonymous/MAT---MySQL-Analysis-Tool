#!/bin/sh
sudo cp analyze.sh /usr/bin/analyze.sh
echo 'Copied analyze.sh to /usr/bin/analyze.sh'
sudo cp sum.sh /usr/bin/sum.sh
echo 'Copied sum.sh to /usr/bin/sum.sh'
sudo cp man /usr/bin/man
echo 'Copied man to /usr/bin/man'
sudo cp mat /usr/bin/mat
echo 'Copied mat to /usr/bin/mat'
sudo mkdir /usr/bin/MAT
echo 'Created MAT directory at /usr/bin/MAT'
sudo apt-get install mysql-utilities
echo 'MAT is installed'
