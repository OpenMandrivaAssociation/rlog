%define name 		rlog
%define version		1.4
%define release		4
%define major		5
%define libname		%mklibname %{name} %{major}
%define libnamedev	%mklibname %{name} %{major} -d 

Summary: 	Runtime Logging for C++
Name: 		%{name}
Version: 	%{version}
Release:        %mkrel %{release}
License:	LGPLv2+
Group:		Development/C++
Source0:        http://rlog.googlecode.com/files/%{name}-%{version}.tar.gz
URL:		http://www.arg0.net/rlog

%description
RLog provides a flexible message logging facility for C++ programs and
libraries. It is designed to be fast enough to use in production code.

%package -n 	%{libname}
Summary:	Libraries for rlog
Group:		Development/C++
Provides:	lib%{name} = %{version}-%{release}
Obsoletes:	%mklibname %{name} 1

%description -n	%{libname}
Libraries for rlog.

%package -n	%{libnamedev}
Summary:	Header files and development libraries for librlog1
Group:		Development/C++
Requires:	lib%{name} = %{version}-%{release} 
Provides:	%{name}-devel = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}
Obsoletes:	%mklibname %{name} 1 -d

%description -n	%{libnamedev}
Header files and development libraries for librlog1.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/librlog.so.*

%files -n %{libnamedev}
%{_includedir}/%{name}
%{_libdir}/librlog.so
%{_libdir}/pkgconfig/librlog.pc
%{_datadir}/doc/%{name}
