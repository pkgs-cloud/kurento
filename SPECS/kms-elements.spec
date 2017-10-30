%define git git0090f10

Summary: Elements for Kurento Media Server
Name: kms-elements
Version: 6.6.3
Release: 1.%{git}%{?dist}
License: Apache 2.0
Group: Applications/Communications
URL: https://github.com/Kurento/kms-elements
Source0: %{name}-%{version}-%{git}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: kms-core kms-openwebrtc-gst-plugins
BuildRequires: kms-core-devel kms-jsonrpc-devel kms-libnice-devel
BuildRequires: kurento-module-creator
BuildRequires: kms-gstreamer1-devel >= 1.8.1, kms-gstreamer1-plugins-base-devel
BuildRequires: openwebrtc-gst-plugins-devel
BuildRequires: boost >= 1.55
BuildRequires: boost-system boost-filesystem boost-program-options boost-test boost-thread boost-log boost-regex
BuildRequires: libsigc++20-devel
BuildRequires: glibmm24-devel
BuildRequires: libevent-devel >= 2.0
BuildRequires: libsrtp-devel >= 1.5.4
BuildRequires: opus-devel >= 1.1.0
BuildRequires: libuuid-devel >= 2.23
BuildRequires: libsoup-devel >= 2.40
BuildRequires: openssl-devel >= 1.0.2h
BuildRequires: gobject-introspection-devel
BuildRequires: valgrind

%description
The kms-elements project contains elements needed for the Kurento Media Server

%package devel
Summary: Elements for Kurento Media Server
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig

%description devel
The kms-elements project contains elements needed for the Kurento Media Server

%prep
%setup -q -n %{name}-master


%build
mkdir -p build
cd build
cmake -DCMAKE_INSTALL_PREFIX:PATH=/usr -DCMAKE_BUILD_TYPE=Release ..
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
cd build
make install DESTDIR=%{buildroot}
mv %{buildroot}/usr/etc %{buildroot}
mv %{buildroot}/usr/share/cmake-* %{buildroot}/usr/share/cmake


%clean
rm -rf %{buildroot}


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%defattr(-,root,root,-)
#%doc AUTHORS COPYING ChangeLog NEWS README TODO
%config(noreplace) %{_sysconfdir}/kurento/modules/kurento
%{_libdir}/*.so.*
%{_libdir}/gstreamer-*/*.so
%{_libdir}/kurento/modules/*.so
%{_datadir}/kurento/modules/*

%files devel
%defattr(-,root,root,-)
%{_libdir}/pkgconfig/*
%{_includedir}/*
%{_datadir}/cmake/*
%exclude %{_libdir}/*.la
%exclude %{_libdir}/*.a
%{_libdir}/*.so


%changelog
