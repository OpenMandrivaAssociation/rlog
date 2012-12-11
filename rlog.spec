%define name 		rlog
%define version		1.4
%define release		3
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
CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS" \
./configure --prefix=%{_prefix} --libdir=%{_libdir}
make -j 2

%install
make DESTDIR=%{buildroot} install

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/librlog.so.*

%files -n %{libnamedev}
%defattr(-,root,root)
%{_includedir}/%{name}
%{_libdir}/librlog.so
%{_libdir}/pkgconfig/librlog.pc
%{_datadir}/doc/%{name}



%changelog
* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 1.4-3mdv2011.0
+ Revision: 614709
- the mass rebuild of 2010.1 packages

* Sun Nov 29 2009 Jérôme Brenier <incubusss@mandriva.org> 1.4-2mdv2010.1
+ Revision: 471582
- obsolete old libs (major 1)

* Tue Nov 24 2009 Jérôme Brenier <incubusss@mandriva.org> 1.4-1mdv2010.1
+ Revision: 469713
- new version 1.4
- new major 5
- fix license tag / URL / Source
- fix files section
- $RPM_BUILD_ROOT -> %%{buildroot}

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 1.3.7-2mdv2008.1
+ Revision: 140746
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - import rlog


* Wed Jun 28 2006 Lev Givon <lev@mandriva.org> 1.3.7-2mdk
- Use mkrel, put docs in devel package

* Mon Jan 09 2006 Moreno Manzini <moreno.mg@gmail.com> 1.3.7-1mdk
- 1.3.7
- Fixed some specs bug

* Sun Jul 24 2005 Madman <madman@extenzilla.it> 1.3.6-3mdk
- Fixed issues in specfile.
* Mon Jun 27 2005 Madman <madman@extenzilla.it> 1.3.6-2mdk
- Fixed issues in specfile.
* Thu Jun 23 2005 Madman <madman@extenzilla.it> 1.3.6-1mdk
- First release for Mandriva 2006 Cooker.
