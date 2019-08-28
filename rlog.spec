%define major 5
%define libname %mklibname %{name} %{major}
%define libnamedev %mklibname %{name} %{major} -d

Summary:	Runtime Logging for C++
Name:		rlog
Version:	1.4
Release:	6
License:	LGPLv2+
Group:		Development/C++
Source0:	http://rlog.googlecode.com/files/%{name}-%{version}.tar.gz
URL:		http://www.arg0.net/rlog

%description
RLog provides a flexible message logging facility for C++ programs and
libraries. It is designed to be fast enough to use in production code.

%package -n %{libname}
Summary:	Libraries for rlog
Group:		Development/C++
Provides:	lib%{name} = %{EVRD}
Obsoletes:	%{mklibname %{name} 1} < 1.4-6

%description -n %{libname}
Libraries for rlog.

%package -n %{libnamedev}
Summary:	Header files and development libraries for librlog1
Group:		Development/C++
Requires:	lib%{name} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}
Provides:	lib%{name}-devel = %{EVRD}
Obsoletes:	%{mklibname %{name} 1 -d} < 1.4-6

%description -n %{libnamedev}
Header files and development libraries for librlog1.

%prep
%autosetup -p1

%build
%configure
%make_build

%install
%make_install

%files -n %{libname}
%{_libdir}/librlog.so.%{major}*

%files -n %{libnamedev}
%{_includedir}/%{name}
%{_libdir}/librlog.so
%{_libdir}/pkgconfig/librlog.pc
%{_datadir}/doc/%{name}
