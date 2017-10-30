%define git git5eef962

Summary: Filter elements for Kurento Media Server
Name: kms-filters
Version: 6.6.3
Release: 1.%{git}%{?dist}
License: Apache 2.0
Group: Applications/Communications
URL: https://github.com/Kurento/kms-filters
Source0: %{name}-%{version}-%{git}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: kms-core kms-elements
BuildRequires: kms-core-devel kms-elements-devel
BuildRequires: opencv-devel
BuildRequires: libsoup-devel >= 2.40

%description
The kms-filters project contains filter elements for the Kurento Media Server

%package devel
Summary: Filter elements for Kurento Media Server
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig

%description devel
The kms-filters project contains filter elements for the Kurento Media Server

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
mv %{buildroot}%{_datadir}/cmake-* %{buildroot}%{_datadir}/cmake

%clean
rm -rf %{buildroot}


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%defattr(-,root,root,-)
%{_libdir}/*.so.*
%{_libdir}/gstreamer-*/*.so
%{_libdir}/kurento/modules/*.so
%{_datadir}/kurento/modules/*

%files devel
%defattr(-,root,root,-)
%{_libdir}/pkgconfig/*
%{_libdir}/*.so
%{_includedir}/*
%{_datadir}/cmake/*
%exclude %{_libdir}/*.la
%exclude %{_libdir}/*.a


%changelog
