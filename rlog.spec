%define name 		rlog
%define version		1.3.7
%define release		3
%define major		1
%define libname		%mklibname %{name} %{major}
%define libnamedev	%mklibname %{name} %{major} -d 

Summary: 	Runtime Logging for C++
Name: 		%{name}
Version: 	%{version}
Release:        %mkrel %{release}
License:	LGPL
Group:		Development/C++
Source:         %{name}-%{version}.tar.bz2
URL:		http://freshmeat.net/projects/rlog/
BuildRoot: 	%{_tmppath}/%{name}-%{version}

%description
RLog provides a flexible message logging facility for C++ programs and
libraries. It is designed to be fast enough to use in production code.

%package -n 	%{libname}
Summary:	Libraries for rlog
Group:		Development/C++
Provides:	lib%{name} = %{version}-%{release}

%description -n	%{libname}
Libraries for rlog.

%package -n	%{libnamedev}
Summary:	Header files and development libraries for librlog1
Group:		Development/C++
Requires:	lib%{name} = %{version}-%{release} 
Provides:	%{name}-devel = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}

%description -n	%{libnamedev}
Header files and development libraries for librlog1.

%prep
rm -rf $RPM_BUILD_ROOT

%setup -q

%build
CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS" \
./configure --prefix=%{_prefix} --libdir=%{_libdir}
make -j 2

%install
make DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/librlog.la
%{_libdir}/librlog.so
%{_libdir}/librlog.so.1
%{_libdir}/librlog.so.1.3.4

%files -n %{libnamedev}
%defattr(-,root,root)
%{_includedir}/%{name}/*.h
%{_libdir}/pkgconfig/librlog.pc
%{_datadir}/doc/%{name}/*

