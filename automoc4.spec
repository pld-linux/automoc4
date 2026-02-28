
%define		qtver	4.4.1

Summary:	Automoc4 - automatically adding Qt moc files rules for CMake
Summary(pl.UTF-8):	Automoc4 - automatyczne dodawanie reguł dla plików Qt moc do CMake
Name:		automoc4
Version:	0.9.88
Release:	4
License:	BSD
Group:		Development/Tools
Source0:	ftp://ftp.kde.org/pub/kde/stable/automoc4/%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	91bf517cb940109180ecd07bc90c69ec
URL:		http://techbase.kde.org/Development/Tools/Automoc4
BuildRequires:	QtCore-devel >= %{qtver}
BuildRequires:	cmake >= 2.6.1-2
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.293
Obsoletes:	kde4-automoc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
automoc4 is a tool to add rules for generating Qt moc files
automatically to projects that use CMake as the buildsystem.

%description -l pl.UTF-8
automoc4 to narzędzie dodające automatycznie reguły do tworzenia
plików Qt moc do projektów wykorzystujących CMake jako swojego
systemu budowania.

%prep
%setup -q

%build
install -d build
cd build
%cmake .. \
	-DCMAKE_BUILD_TYPE=%{!?debug:Release}%{?debug:Debug} \
	-DCMAKE_CXX_FLAGS_RELEASE="-DNDEBUG" \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	-DCMAKE_VERBOSE_MAKEFILE=ON \
	-DQT_QMAKE_EXECUTABLE=/usr/bin/qmake-qt4

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
%{_libdir}/automoc4/Automoc4*.cmake
%{_libdir}/automoc4/automoc4.files.in
