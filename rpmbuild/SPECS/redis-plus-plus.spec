Name:           redis-plus-plus
Version:        0.1
Release:        0
Summary:        Application Launcher for Dragonfly applications
Group:          net
License:        GPL
URL:            http://github.com/Upnext-DragonFly
Vendor:         Upnext
Source:         packagesource.tar.gz
Prefix:         %{_prefix}
Packager:       Dragonfly
BuildRoot:      %{_tmppath}/%{name}-%{version}
# BuildRequires:
# Requires:

Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd

%description
Dragonfly application launcher

%global debug_package %{nil}

%prep
%setup -c .

%post
%systemd_post %{name}.service

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

%changelog
* Tue Oct 04 2022 Dragonfly <dragonfly@upnext.com> - 1.1-0
- First package

