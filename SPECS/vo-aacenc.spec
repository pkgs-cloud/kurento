Name:		vo-aacenc
Version:	0.1.2
Release:	3%{?dist}
Summary:	VisualOn AAC encoder library
License:	ASL 2.0
Group:		Applications/Multimedia
URL:		http://opencore-amr.sourceforge.net/
Source:		http://sourceforge.net/projects/opencore-amr/files/%{name}/%{name}-%{version}.tar.gz
Requires:	glibc

%description
This library contains an encoder implementation of the Advanced Audio
Coding (AAC) audio codec. The library is based on a codec implementation
by VisualOn as part of the Stagefright framework from the Google
Android project.

This package is in the 'tainted' section because the AAC encoding 
standard is covered by patents.

%package devel
Summary:        Development files for vo-aacenc
Group:          Applications/Multimedia
Requires:       %{name} = %{version}-%{release}

%description devel
This package contains libraries and header files for
developing applications that use vo-aacenc.

%prep
%setup -q

%build
%configure --disable-static --disable-silent-rules
make %{?_smp_mflags}


%install
rm -rf %buildroot
make install DESTDIR=%{buildroot}

find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files 
%{_libdir}/libvo-aacenc.so.0
%{_libdir}/libvo-aacenc.so.0.0.3

%files devel
%{_includedir}/%{name}
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc


%changelog

* Fri Jul 08 2016 David Vásquez <davidjeremias82 AT gmail DOT com> - 0.1.2-3
- Massive rebuild

* Thu Apr 28 2016 David Vásquez <davidjeremias82 AT gmail DOT com> - 0.1.2-2
- Rebuilt 

* Fri May 17 2012 David Vasquez <davidjeremias82 AT gmail DOT com> - 0.1.2-1
- Initial build

