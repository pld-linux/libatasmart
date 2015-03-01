Summary:	ATA S.M.A.R.T. Disk Health Monitoring Library
Summary(pl.UTF-8):	Biblioteka do monitorowania stanu dysku ATA S.M.A.R.T.
Name:		libatasmart
Version:	0.19
Release:	2
License:	LGPL v2+
Group:		Libraries
Source0:	http://0pointer.de/public/%{name}-%{version}.tar.xz
# Source0-md5:	53afe2b155c36f658e121fe6def33e77
BuildRequires:	autoconf >= 2.68
BuildRequires:	automake >= 1:1.11
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:2.2
BuildRequires:	pkgconfig
BuildRequires:	tar >= 1:1.22
BuildRequires:	udev-devel >= 143
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A small and lightweight parser library for ATA S.M.A.R.T. hard disk
health monitoring.

%description -l pl.UTF-8
Mała i lekka biblioteka analizująca stan dysków twardych ATA z
systemem S.M.A.R.T.

%package devel
Summary:	Header files for libatasmart library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libatasmart
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	udev-devel >= 143

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

%package -n vala-atasmart
Summary:	libatasmart API for Vala language
Summary(pl.UTF-8):	API libatasmart dla języka Vala
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description -n vala-atasmart
libatasmart API for Vala language.

%description -n vala-atasmart -l pl.UTF-8
API libatasmart dla języka Vala.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	--enable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libatasmart.la

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
%attr(755,root,root) %ghost %{_libdir}/libatasmart.so.4

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libatasmart.so
%{_includedir}/atasmart.h
%{_pkgconfigdir}/libatasmart.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libatasmart.a

%files -n vala-atasmart
%defattr(644,root,root,755)
%{_datadir}/vala/vapi/atasmart.vapi
