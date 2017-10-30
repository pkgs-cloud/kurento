%define module crowddetector

Summary: Kurento Crowd detector filter element
Name: kms-%{module}
Version: 6.6.0
Release: 1%{?dist}
License: GPLv2+
Group: Applications/Communications
URL: https://github.com/Kurento/%{name}
Source0: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: kms-filters
Provides: kms-filters-%{module}
BuildRequires: kms-cmake-utils
BuildRequires: kms-core-devel
BuildRequires: kms-elements-devel
BuildRequires: libsoup-devel
BuildRequires: opencv-devel

%description
Crowd detector filter element for Kurento Media Server

%package devel
Summary: Development package for %{name}
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig

%description devel
Development package for %{name}

%prep
%setup -q


%build
mkdir -p build
cd build
cmake -DCMAKE_INSTALL_PREFIX:PATH=/usr -DBUILD_SHARED_LIBS=ON -DCMAKE_BUILD_TYPE=Release -G "Unix Makefiles" ..
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
cd build
make install DESTDIR=%{buildroot}
mv %{buildroot}/usr/share/cmake-* %{buildroot}/usr/share/cmake

%clean
rm -rf %{buildroot}


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_libdir}/*.so.*
%{_libdir}/gstreamer-1.5/lib%{module}.so
%{_libdir}/kurento/modules/libkms%{module}module.so
%{_datadir}/kurento/*

%files devel
%defattr(-,root,root,-)
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_includedir}/*
%{_datadir}/cmake/*
%exclude %{_libdir}/*.la
%exclude %{_libdir}/*.a


%changelog
