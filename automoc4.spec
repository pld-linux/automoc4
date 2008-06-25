
Summary:	automoc4
Summary(pl.UTF-8):	automoc4
Name:		automoc4
Version:	0.9.83
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	ftp://ftp.kde.org/pub/kde/unstable/4.0.83/support/%{name}-%{version}.tar.bz2
# Source0-md5:	7876af12da90bd357fc547c4f4828603
Patch0:		%{name}-lib64.patch
BuildRequires:	QtCore-devel
BuildRequires:	cmake
BuildRequires:	qt4-build
BuildRequires:	qt4-qmake
BuildRequires:	rpmbuild(macros) >= 1.293
Obsoletes:	kde4-automoc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
automoc4.

%description -l pl.UTF-8
automoc3.

%prep
%setup -q
%patch0 -p0

%build
install -d build
cd build
%cmake \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
%if "%{_lib}" != "lib"
	-DLIB_SUFFIX=64 \
%endif
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/automoc4
%dir %{_libdir}/automoc4
%{_libdir}/automoc4/Automoc4Config.cmake
%{_libdir}/automoc4/automoc4.files.in
