##
## File:        Makefile.am 
## Package:     Babel makefiles
## Revision:    $Revision: 7368 $
## Modified:    $Date: 2011-11-22 15:23:42 -0800 (Tue, 22 Nov 2011) $
## Description: automake makefile to build the sidl runtime library
##
## Copyright (c) 2000-2002, The Regents of the University of Calfornia.
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


INCLUDEDIR  = $(srcdir)/../sidl
INCLUDEDIR2 = .
LIBSIDL    = $(top_builddir)/sidl/libsidl.la

dist_data_DATA = sidlx.sidl
include_HEADERS = $(STUBHDRS) $(IORHDRS) sidlx_common.h

lib_LTLIBRARIES = libsidlx.la 
libsidlx_la_SOURCES = $(IMPLSRCS) $(IMPLHDRS) sidlx_common.c sidlx_common.h \
	$(STUBSRCS) $(STUBHDRS) $(IORSRCS) $(IORHDRS) \
	$(SKELSRCS) $(SKELHDRS) 
libsidlx_la_LDFLAGS = -no-undefined -release $(VERSION) $(LIBSIDL)

AM_CPPFLAGS = -I$(INCLUDEDIR) -I$(INCLUDEDIR2)

EXTRA_DIST = babel.make libsidlx.scl.in

all-local:libsidlx.scl

libsidlx.scl:
	sed -e 's,@@DIR@@,'`pwd`',g' < $(srcdir)/libsidlx.scl.in > libsidlx.scl

if BABEL_RUNTIME_ONLY
CLEANFILES = babel-stamp babel-temp libsidlx.scl \
	babel.make.package babel.make.depends

babel-stamp:
	touch babel-stamp

else
CLEANFILES = babel-stamp babel-temp libsidlx.scl \
	$(STUBSRCS) $(STUBHDRS) $(IORSRCS) $(IORHDRS) $(SKELSRCS) $(SKELHDRS) \
	babel.make.package babel.make.depends

$(STUBSRCS) $(STUBHDRS) $(IORSRCS) $(IORHDRS) $(SKELSRCS) $(SKELHDRS) $(IMPLSRCS) $(IMPLHDRS) : babel-stamp
## cf. http://www.gnu.org/software/automake/manual/automake.html#Multiple-Outputs
## Recover from the removal of $@
	@if test -f $@; then :; else \
	  trap 'rm -rf babel.lock babel-stamp' 1 2 13 15; \
## mkdir is a portable test-and-set
	  if mkdir babel.lock 2>/dev/null; then \
## This code is being executed by the first process.
	    rm -f babel-stamp; \
	    $(MAKE) $(AM_MAKEFLAGS) babel-stamp; \
	    result=$$?; rm -rf babel.lock; exit $$result; \
	  else \
## This code is being executed by the follower processes.
## Wait until the first process is done.
	    while test -d babel.lock; do sleep 1; done; \
## Succeed if and only if the first process succeeded.
	    test -f babel-stamp; \
	  fi; \
	fi

babel-stamp: $(srcdir)/sidlx.sidl
	@rm -f babel-temp
	@touch babel-temp
	$(SHELL) ../../bin/babel --vpath="$(srcdir)" --server=C \
	  -! $(srcdir)/../sidl/sidl.sidl \
	$(srcdir)/sidlx.sidl
	@mv -f babel-temp $@
endif

clean-local:
	test "X$(srcdir)" = "X." || rm -f $(IMPLSRCS) $(IMPLHDRS)


include babel.make

# Make sure Makefile.in is newer than babel.make
dist-hook:
	touch -c $(distdir)/Makefile.in

install-data-local:
	sed -e 's,@@DIR@@,$(DESTDIR)$(libdir),g' < $(srcdir)/libsidlx.scl.in \
		> libsidlx_inst.scl
	$(INSTALL_DATA) libsidlx_inst.scl $(DESTDIR)$(libdir)/libsidlx.scl
	rm -f libsidlx_inst.scl

uninstall-local:
	$(RM) $(DESTDIR)$(libdir)/libsidlx.scl
