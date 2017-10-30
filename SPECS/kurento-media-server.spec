%define git gitf7091a3

Summary: Kurento Media Server
Name: kurento-media-server
Version: 6.6.3
Release: 1.%{git}%{?dist}
License: Apache 2.0
Group: Applications/Communications
URL: https://github.com/Kurento/kurento-media-server
Source0: kurento-media-server-%{version}-%{git}.tar.gz
Source1: kms.service
Source2: kms.sysconfig
#Patch0: loadConfig.cpp.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: kms-core kms-elements kms-libnice kms-jsonrpc kms-usrsctp
Requires: boost >= 1.55
Requires: boost-system boost-filesystem boost-program-options boost-test boost-thread boost-log boost-regex
Requires: libsrtp >= 1.5.4
Requires: opus >= 1.1.0
Requires: openssl-libs >= 1.0.2
BuildRequires: kms-jsonrpc-devel
# Boost 1.55
BuildRequires: boost >= 1.55
BuildRequires: boost-system boost-filesystem boost-program-options boost-test boost-thread boost-log boost-regex
BuildRequires: libsigc++20-devel
BuildRequires: glibmm24-devel
BuildRequires: libevent-devel >= 2.0
BuildRequires: libsrtp-devel >= 1.5.4
BuildRequires: opus-devel >= 1.1.0

%description
Kurento Media Server is the Kurento's core element.
It is responsible for media transmission, processing, loading and recording.
It is implemented in low level technologies based on GStreamer to optimize
the resource consumption. It provides the following features:
- Networked streaming protocols, including HTTP, RTP and WebRTC
- Group communications (MCUs and SFUs functionality) supporting both media mixing
  and media routing/dispatching
- Generic support for computational vision and augmented reality filters
- Media storage supporting writing operations for WebM and MP4 and playing
  in all formats supported by GStreamer
- Automatic media transcodification between any of the codecs supported
  by GStreamer including VP8, H.264, H.263, AMR, OPUS, Speex, G.711, etc.

%prep
%setup -q -n %{name}-master
#%patch0


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

install -p -D -m 0644 %{SOURCE1} \
    %{buildroot}%{_unitdir}/kms.service

install -p -D -m 0644 %{SOURCE2} \
    %{buildroot}%{_sysconfdir}/sysconfig/kms

install -p -d -m 0700 %{buildroot}%{_localstatedir}/kurento
install -p -d -m 0700 %{buildroot}%{_localstatedir}/log/kurento

%clean
rm -rf %{buildroot}


%post
%systemd_post kms.service

%preun
%systemd_preun kms.service

%postun
%systemd_postun kms.service

%files
%defattr(-,root,root,-)
#doc ChangeLog.md README.md LICENSE
%doc README.md LICENSE
%config(noreplace) %{_sysconfdir}/kurento
%config(noreplace) %{_sysconfdir}/sysconfig/kms
%{_bindir}/*
%{_datadir}/kurento/*
%{_localstatedir}/*
%{_unitdir}/kms.service

%changelog
