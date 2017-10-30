%define         kms_version kms6.6.0

Summary: Kurento SCTP user-land implementation
Name: kms-usrsctp
Version: 0.9.2.1
Release: 1%{?dist}
License: GPLv2+
Group: Applications/Communications
URL: https://github.com/Kurento/usrsctp
Source0: usrsctp-%{kms_version}.zip
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
#Requires: 
#BuildRequires: 

%description
SCTP is a message oriented, reliable transport protocol with direct
support for multihoming that runs on top of IP or UDP, and supports
both v4 and v6 versions

%package devel
Summary: Kurento SCTP user-land implementation
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig

%description devel
SCTP is a message oriented, reliable transport protocol with direct
support for multihoming that runs on top of IP or UDP, and supports
both v4 and v6 versions

%prep
%setup -q -n usrsctp-%{kms_version}

%build
./bootstrap
#./configure --build=x86_64-redhat-linux-gnu --host=x86_64-redhat-linux-gnu --program-prefix= --disable-dependency-tracking --prefix=/usr \
#    --exec-prefix=/usr --bindir=/usr/bin --sbindir=/usr/sbin --sysconfdir=/etc --datadir=/usr/share --includedir=/usr/include --libdir=/usr/lib64 \
#    --libexecdir=/usr/libexec --localstatedir=/var --sharedstatedir=/var/lib --mandir=/usr/share/man --infodir=/usr/share/info
FORTIFY_FLAGS=`echo "$CFLAGS" | sed '/^.*\(-D_FORTIFY_SOURCE=.\).*$/s//\1/'`
CFLAGS="$FORTIFY_FLAGS $CFLAGS"
%configure
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}


%clean
rm -rf %{buildroot}


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root,-)
%{_libdir}/*.so
#%{_libdir}/pkgconfig/*
%{_includedir}/*
%exclude %{_libdir}/*.la
%exclude %{_libdir}/*.a


%changelog
