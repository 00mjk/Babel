##
## File:        Makefile.am
## Package:     Babel regression checks
## Revision:    $Revision: 5359 $
## Modified:    $Date: 2007-09-26 13:53:06 -0600 (Wed, 26 Sep 2007) $
## Description: automake makefile for C++ regression tests
##
## Copyright (c) 2000-2001, The Regents of the University of Calfornia.
## Produced at the Lawrence Livermore National Laboratory.
## Written by the Components Team <components@llnl.gov>
## UCRL-CODE-2002-054
## All rights reserved.
## 
## This file is part of Babel. For more information, see
## http://www.llnl.gov/CASC/components/. Please read the COPYRIGHT file
## for Our Notice and the LICENSE file for the GNU Lesser General Public
## License.
## 
## This program is free software; you can redistribute it and/or modify it
## under the terms of the GNU Lesser General Public License (as published by
## the Free Software Foundation) version 2.1 dated February 1999.
## 
## This program is distributed in the hope that it will be useful, but
## WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
## conditions of the GNU Lesser General Public License for more details.
## 
## You should have received a copy of the GNU Lesser General Public License
## along with this program; if not, write to the Free Software Foundation,
## Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA

SIDLFILE = $(srcdir)/../struct.sidl
TESTFILE = structtest.F03

include $(srcdir)/../../include/runF03.make
include $(srcdir)/babel.make
include $(srcdir)/synch_babel.make

s_Combined.lo : s_Simple.lo s_Hard.lo s_Rarrays.lo
