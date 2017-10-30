Summary: Kurento JsonRPC protocol implementation
Name: kms-jsonrpc
Version: 1.1.3
Release: 1%{?dist}
License: GPLv2+
Group: Applications/Communications
URL: https://github.com/Kurento/kms-jsonrpc
Source0: kms-jsonrpc-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: kms-jsoncpp
BuildRequires: kms-cmake-utils
BuildRequires: kms-jsoncpp-devel
BuildRequires: boost >= 1.55
BuildRequires: boost-test

%description
Kurento JsonRPC protocol implementation

%package devel
Summary: Kurento JsonRPC protocol implementation
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig

%description devel
Kurento JsonRPC protocol implementation

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

%files devel
%defattr(-,root,root,-)
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_includedir}/*
%{_datadir}/*
%exclude %{_libdir}/*.la
%exclude %{_libdir}/*.a


%changelog
