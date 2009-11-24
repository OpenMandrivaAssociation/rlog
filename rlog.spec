%define name 		rlog
%define version		1.4
%define release		1
%define major		5
%define libname		%mklibname %{name} %{major}
%define libnamedev	%mklibname %{name} %{major} -d 

Summary: 	Runtime Logging for C++
Name: 		%{name}
Version: 	%{version}
Release:        %mkrel %{release}
License:	LGPLv2+
Group:		Development/C++
Source:         http://rlog.googlecode.com/files/%{name}-%{version}.tar.gz
URL:		http://www.arg0.net/rlog
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
rm -rf %{buildroot}

%setup -q

%build
CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS" \
./configure --prefix=%{_prefix} --libdir=%{_libdir}
make -j 2

%install
make DESTDIR=%{buildroot} install

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/librlog.la
%{_libdir}/librlog.so.*

%files -n %{libnamedev}
%defattr(-,root,root)
%{_includedir}/%{name}
%{_libdir}/librlog.so
%{_libdir}/pkgconfig/librlog.pc
%{_datadir}/doc/%{name}

