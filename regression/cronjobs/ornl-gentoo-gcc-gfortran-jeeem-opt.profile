#!/bin/sh
# 
# Profile: ornl-gentoo-gcc-gfortran-jeeem-opt.profile
#

# setup the general Linux flags

export MAIL_SERVER=smtp.ornl.gov
export SH=bash
export PACKAGE=babel
export SNAPSHOT_NUMBER=`date '+%Y%m%d'`
export PATH=/usr/local/bin:/bin:/usr/bin:/usr/local/lib:/opt/bin:/sbin:/usr/sbin:/home/kohl/.gentoo/java-config-2/current-user-vm/bin
export LD_LIBRARY_PATH=/usr/local/lib
export JNI_INCLUDES='/home/kohl/.gentoo/java-config-2/current-user-vm/include'

host=`hostname`

export SVN=svn
export SVNROOT=svn+ssh://kohl@www.cca-forum.org/svn/babel/trunk
export URL=http://www.cca-forum.org/download/babel
export MAKE=make
export MAKE_FLAGS="-j2 -l 2.1"
export MAIL=mail
export PERL=perl
export ACLOCAL=aclocal
export AUTOMAKE=automake
export AUTOCONF=autoconf
export CONFIG_FLAGS="--enable-auto-disable --with-F90-vendor=GNU"
export CD=cd
export MKDIR=mkdir
export MV=mv
export CHMOD=chmod
export CHGRP=chgrp
export TESTGID=babel
export FIND=find

# export PACKAGING_BUILDDIR=${HOME}/babel_scratch
export PACKAGING_BUILDDIR=${HOME}/CCA/CCA2/babel_testing/babel_scratch
mkdir -p ${PACKAGING_BUILDDIR}

# set the GCC version
export GCCVERSION=`gcc --version | head -n 1 | awk ' { print $3}'`

export CC=gcc
export CFLAGS='-O -Wall -Wtrigraphs'
export CXX=g++
export CXXFLAGS='-O -Wall'

export F77=/usr/bin/gfortran
export FFLAGS=-O

export FC=/usr/bin/gfortran

export PROFILE_NAME="ornl-gentoo-gcc${GCCVERSION}-gfortran-jeeem-opt"

