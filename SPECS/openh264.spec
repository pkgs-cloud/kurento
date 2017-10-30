# globals for openh264-1.5.0-20160606-2610ab1.tar.xz
%global gitdate 20160606
%global gitversion 2610ab1
%global snapshot %{gitdate}-%{gitversion}
%global gver .%{gitdate}git%{gitversion}

Name:         	openh264
Summary:      	Open Source H.264 Codec
URL:          	http://www.openh264.org/
Group:        	System/Libraries
License:      	BSD
Version:      	1.5.0
Release:        3%{?gver}%{dist}
Source0:	%{name}-%{version}-%{snapshot}.tar.xz
Source1: 	%{name}-snapshot.sh
Source2:	https://github.com/mozilla/gmp-api/archive/master.zip
Patch:		fix_path.patch
BuildRequires: 	nasm git unzip

%description
OpenH264 is a codec library which supports H.264 encoding and decoding.
It is suitable for use in real time applications such as WebRTC.

%package devel
Summary: Development files for %{name}
Requires: %{name} = %{version}

%description devel
Header files and libraries for the package %{name}.

%package     -n mozilla-openh264
Summary:        H.264 codec support for Mozilla browsers
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       mozilla-filesystem%{?_isa}

%description -n mozilla-openh264
The mozilla-openh264 package contains a H.264 codec plugin for Mozilla
browsers.

%prep
%setup -n openh264

%ifarch x86_64
%patch -p0
%else
sed -i 's/PREFIX=\/usr\/local/PREFIX=\/usr/g' Makefile
%endif

#------------------------|
# Api for mozilla plugin
# Extract gmp-api archive
unzip %{S:2}
mv gmp-api-master gmp-api
#------------------------|

%build

# Update the makefile with our build options
sed -i -e 's|^CFLAGS_OPT=.*$|CFLAGS_OPT=%{optflags}|' Makefile
sed -i -e 's|^PREFIX=.*$|PREFIX=%{_prefix}|' Makefile
sed -i -e 's|^LIBDIR_NAME=.*$|LIBDIR_NAME=%{_lib}|' Makefile
sed -i -e 's|^SHAREDLIB_DIR=.*$|SHAREDLIB_DIR=%{_libdir}|' Makefile
sed -i -e '/^CFLAGS_OPT=/i LDFLAGS=%{__global_ldflags}' Makefile

%ifarch x86_64 
arch=x86_64
%else
arch=i386
%endif
make %{?_smp_mflags} ARCH=$arch

# build mozilla plugin
make plugin %{?_smp_mflags}

%install
%make_install 
%ifarch x86_64
sed -i 's|${prefix}/lib|${prefix}/lib64|g' %{buildroot}/%{_libdir}/pkgconfig/openh264.pc
%endif

#--------------------------------------------|
#Install mozilla plugin
install -dm 755 $RPM_BUILD_ROOT%{_libdir}/mozilla/plugins/gmp-gmpopenh264/system-installed
cp -a h264enc libgmpopenh264.so gmpopenh264.info $RPM_BUILD_ROOT%{_libdir}/mozilla/plugins/gmp-gmpopenh264/system-installed/

# cofiguration for mozilla plugin
install -dm 755 $RPM_BUILD_ROOT%{_libdir}/firefox/defaults/pref
cat > $RPM_BUILD_ROOT%{_libdir}/firefox/defaults/pref/gmpopenh264.js << EOF
pref("media.gmp-gmpopenh264.autoupdate", false);
pref("media.gmp-gmpopenh264.version", "system-installed");
EOF

install -dm 755 $RPM_BUILD_ROOT%{_sysconfdir}/profile.d
cat > $RPM_BUILD_ROOT%{_sysconfdir}/profile.d/gmpopenh264.sh << EOF
MOZ_GMP_PATH="%{_libdir}/mozilla/plugins/gmp-gmpopenh264/system-installed"
export MOZ_GMP_PATH
EOF
#end install mozilla plugin
#--------------------------------------------|

# Tools for openh264
install -dm 755 $RPM_BUILD_ROOT%{_bindir}
cp -a h264enc h264dec $RPM_BUILD_ROOT%{_bindir}/

# Remove static libraries
rm $RPM_BUILD_ROOT%{_libdir}/*.a

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc README.md LICENSE CONTRIBUTORS
%{_bindir}/h264enc
%{_bindir}/h264dec
%{_libdir}/lib%{name}.so.*

%files devel
%{_includedir}/wels
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/*.pc

%files -n mozilla-openh264
%{_sysconfdir}/profile.d/gmpopenh264.sh
%dir %{_libdir}/firefox
%dir %{_libdir}/firefox/defaults
%dir %{_libdir}/firefox/defaults/pref
%{_libdir}/firefox/defaults/pref/gmpopenh264.js
%{_libdir}/mozilla/plugins/gmp-gmpopenh264/

%changelog

* Fri Jul 08 2016 David Vásquez <davidjeremias82 AT gmail DOT com> - 1.5.0-3-20160606-2610ab1
- Massive rebuild

* Tue Apr 19 2016 David Vásquez <davidjeremias82 AT gmail DOT com> 1.5.0-2-20160606-2610ab1
- Enabled mozilla-openh264

* Tue Apr 19 2016 David Vásquez <davidjeremias82 AT gmail DOT com> 1.5.0-2-20160419-2610ab1
- Initial build rpm
