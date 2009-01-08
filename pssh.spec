Summary: Parallel SSH tools
Name: pssh
Version: 1.2.2
Release: 1
Group: system
Source: pssh-1.2.2.tar.gz 
License: GPL
Requires: openssh
Requires: python2
Packager: Brent Chun <bnc@theether.org>

%description
This package provides various parallel tools based on ssh and scp.

%prep 
%setup

%build
./configure
make

%install
install -D -m 755 bin/pssh /usr/local/bin/pssh
install -D -m 755 bin/pscp /usr/local/bin/pscp
install -D -m 755 bin/pnuke /usr/local/bin/pnuke
install -D -m 755 bin/prsync /usr/local/bin/prsync
install -D -m 755 bin/pslurp /usr/local/bin/pslurp
install -D -m 644 lib/python/psshutil.py \
                  /usr/local/lib/python/psshutil.py
install -D -m 644 lib/python/basethread.py \
                  /usr/local/lib/python/basethread.py

%clean

%files
%defattr(-,root,root)
/usr/local/bin/pssh
/usr/local/bin/pscp
/usr/local/bin/pnuke
/usr/local/bin/prsync
/usr/local/bin/pslurp
/usr/local/lib/python/psshutil.py
/usr/local/lib/python/basethread.py