Summary:	ATA S.M.A.R.T. Disk Health Monitoring Library
Name:		libatasmart
Version:	0.13
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	http://0pointer.de/public/%{name}-%{version}.tar.gz
# Source0-md5:	1dbefaaf98c01305ca82df514a0b2258
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake >= 1:1.9
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	udev-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A small and lightweight parser library for ATA S.M.A.R.T. hard disk
health monitoring.

%package devel
Summary:	Header files for libatasmart library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libatasmart
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libatasmart library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libatasmart.

%package static
Summary:	Static libatasmart library
Summary(pl.UTF-8):	Statyczna biblioteka libatasmart
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libatasmart library.

%description static -l pl.UTF-8
Statyczna biblioteka libatasmart.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_sbindir}/skdump
%attr(755,root,root) %{_sbindir}/sktest
%attr(755,root,root) %{_libdir}/libatasmart.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libatasmart.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libatasmart.so
%{_libdir}/libatasmart.la
%{_includedir}/atasmart.h
%{_pkgconfigdir}/libatasmart.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libatasmart.a
