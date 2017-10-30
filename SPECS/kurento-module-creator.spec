Summary: Kurento Module Creator
Name: kurento-module-creator
Version: 4.0.7
Release: 1%{?dist}
License: Apache 2.0
Group: Development/Tools
URL: https://github.com/Kurento/kurento-module-creator
Source0: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: cmake >= 2.8
#Requires: java
BuildRequires: maven >= 3.0

%description
The kurento-module-creator project contains a processor that will
generate code for RPC between the Kurento Media Server and remote libraries

%prep
%setup -q

%build
mvn package

%install
install -p -d -m 0755 %{buildroot}%{_bindir}
install -p -D -m 0644 -t %{buildroot}%{_bindir} target/kurento-module-creator-jar-with-dependencies.jar
install -p -D -m 0755 -t %{buildroot}%{_bindir} scripts/kurento-module-creator

install -p -d -m 0755 %{buildroot}%{_datadir}/cmake/Modules
install -p -D -m 0644 -t %{buildroot}%{_datadir}/cmake/Modules target/classes/FindKurentoModuleCreator.cmake

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%{_bindir}/*
%{_datadir}/*

%changelog
