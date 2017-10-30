%global shortname srtp

Name:		libsrtp
Version:	1.5.4
Release:	3%{?dist}
Summary:	An implementation of the Secure Real-time Transport Protocol (SRTP)
Group:		System Environment/Libraries
License:	BSD
URL:		https://github.com/cisco/libsrtp
Source0:	https://github.com/cisco/libsrtp/archive/v%{version}.tar.gz
# Universal config.h
Source2:	config.h
# Fix shared lib so ldconfig doesn't complain
Patch0:		libsrtp-1.5.4-shared-fix.patch
Patch1:		libsrtp-srtp_aes_encrypt.patch
Patch2:		libsrtp-sha1-name-fix.patch
Patch3:		libsrtp-fix-name-collision-on-MIPS.patch

%description
This package provides an implementation of the Secure Real-time
Transport Protocol (SRTP), the Universal Security Transform (UST), and
a supporting cryptographic kernel.

%package devel
Summary:	Development files for %{name}
Group:		Development/Libraries
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	pkgconfig

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1 -b .sharedfix
%patch1 -p1 -b .srtp_aes_encrypt
%patch2 -p1 -b .sha1-name-fix
%patch3 -p1 -b .mips-name-fix

%if 0%{?rhel} > 0
%ifarch ppc64
sed -i 's/-z noexecstack//' Makefile.in
%endif
%endif

%build
export CFLAGS="%{optflags} -fPIC"
%configure
make %{?_smp_mflags} shared_library

%install
make install DESTDIR=%{buildroot}
find %{buildroot} -name '*.la' -exec rm -f {} ';'

# Handle multilib issues with config.h
mv %{buildroot}%{_includedir}/%{shortname}/config.h %{buildroot}%{_includedir}/%{shortname}/config-%{__isa_bits}.h
cp -a %{SOURCE2} %{buildroot}%{_includedir}/%{shortname}/config.h

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license LICENSE
%doc CHANGES README TODO VERSION doc/*.txt doc/*.pdf
%{_libdir}/*.so.*

%files devel
%{_includedir}/%{shortname}/
%{_libdir}/pkgconfig/libsrtp.pc
%{_libdir}/*.so

%changelog
* Wed Mar  2 2016 Tom Callaway <spot@fedoraproject.org> - 1.5.4-3
- use upstream provided .pc file (bz1313590)

* Fri Feb 12 2016 Tom Callaway <spot@fedoraproject.org> - 1.5.4-2
- fix shared lib generation to silence ldconfig

* Thu Feb 11 2016 Tom Callaway <spot@fedoraproject.org> - 1.5.4-1
- update to 1.5.4
- fix MIPS name collision (bz1305950 ) Thanks to Michal Toman

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Nov 14 2014 Tom Callaway <spot@fedoraproject.org> - 1.5.0-2
- fix library linking typo

* Fri Nov 14 2014 Tom Callaway <spot@fedoraproject.org>
- api changes between 1.4.4 and 1.5.0, bump sover to 1.0.0
- fix linking issue to make proper libsrtp.so.1

* Fri Oct 31 2014 Leif Madsen <leif@leifmadsen.com> - 1.5.0-1
- Update for 1.5.0 release.

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.4-13.20101004cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.4-12.20101004cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 15 2014 Dennis Gilmore <dennis@ausil.us> - 1.4.4-11.20101004cvs
- update the config.h header aarch64 is a 64 bit arch though there is no multilib

* Mon Feb 10 2014 Tom Callaway <spot@fedoraproject.org> - 1.4.4-10.20101004cvs
- rename internal functions to avoid conflicts (bz 956340)

* Mon Dec 30 2013 Tom Callaway <spot@fedoraproject.org> - 1.4.4-9.20101004cvs
- apply fix for CVE-2013-2139 from https://github.com/cisco/libsrtp/pull/27

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.4-8.20101004cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.4-7.20101004cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Sep 25 2012 Karsten Hopp <karsten@redhat.com> 1.4.4-6.20101004cvs
- use __PPC64__, not __ppc64__ which is undefined on PPC64 arch

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.4-5.20101004cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 21 2012 Tom Callaway <spot@fedoraproject.org> - 1.4.4-4.20101004cvs
- handle config.h multilib (bz787537)

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.4-3.20101004cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.4-2.20101004cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jan 25 2011 Jeffrey C. Ollie <jeff@ocjtech.us>
- Don't use '-z noexecstack' option for linker on PPC64 (EL6)

* Mon Oct  4 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 1.4.4-1.20101004cvs
- initial package
