Name:           redis-plus-plus
Version:        1.3.5
Release:        1
Summary:        Redis plus plus
Group:          net
License:        GPL
URL:            http://github.com/Upnext-DragonFly
Vendor:         Upnext
Source:         packagesource.tar.gz
Prefix:         %{_prefix}
Packager:       Dragonfly
BuildRoot:      %{_tmppath}/%{name}-%{version}
BuildRequires:  hiredis-devel, redis-devel
Requires:       hiredis, redis, redis-server, redis-tools

%description
Redis plus plus

%global debug_package %{nil}

%prep
%setup -c .

%build
CFLAGS="$RPM_OPT_FLAGS" cmake -DCMAKE_INSTALL_PREFIX:PATH=/ .
make INSTALL_LIB=lib64 sysconfdir=/etc -j$(nproc)

%install
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT INSTALL_LIB=lib64 install

%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_libdir}/*
%{_includedir}/*
/share/cmake/*

%changelog
* Fri Oct 21 2022 Dragonfly <dragonfly@upnext.com> - 1.3.5-1
- Fix dependencies
* Tue Oct 04 2022 Dragonfly <dragonfly@upnext.com> - 1.3.5-0
- First package

