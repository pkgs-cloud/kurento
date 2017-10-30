%define git git8ec5a3a

Summary: Core library of Kurento Media Server
Name: kms-core
Version: 6.6.3
Release: 1.%{git}%{?dist}
License: GPLv2+
Group: Applications/Communications
URL: https://github.com/Kurento/kms-core
Source0: %{name}-%{version}-%{git}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: kms-jsonrpc kms-jsoncpp
BuildRequires: kms-jsonrpc-devel kms-jsoncpp-devel kms-cmake-utils kurento-module-creator
BuildRequires: kms-gstreamer1-devel >= 1.8.1, kms-gstreamer1-plugins-base-devel
BuildRequires: kms-openwebrtc-gst-plugins-devel
BuildRequires: kms-cmake-utils
BuildRequires: boost >= 1.55
BuildRequires: boost-system boost-filesystem boost-program-options boost-test boost-thread boost-log boost-regex
BuildRequires: libsigc++20-devel
BuildRequires: glibmm24-devel
BuildRequires: libuuid-devel >= 2.23
BuildRequires: libvpx-devel >= 1.3.0

%description
The kms-core project contains core elements needed for the Kurento Media Server

%package devel
Summary: Development files for %{name}
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig

%description devel
Development files for %{name}

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
mv %{buildroot}%{_datadir}/cmake-* %{buildroot}%{_datadir}/cmake

%clean
rm -rf %{buildroot}


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%defattr(-,root,root,-)
%{_sysconfdir}/kurento/modules/kurento
%{_libdir}/*.so.*
%{_libdir}/gstreamer-*/*.so
%{_libdir}/kurento/modules/*.so

%{_datadir}/kurento/modules/*

%files devel
%defattr(-,root,root,-)
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_includedir}/*
%{_datadir}/cmake/*
%exclude %{_libdir}/*.la
%exclude %{_libdir}/*.a


%changelog
