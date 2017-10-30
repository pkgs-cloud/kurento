%define         kms_version kms6.6.2

Name:           kms-libnice
Version:        0.1.14.1
Release:        1%{?dist}
Summary:        Kurento GLib ICE implementation

Group:          System Environment/Libraries
License:        LGPLv2 and MPLv1.1
URL:            https://github.com/Kurento/libnice
Source0:        libnice-%{kms_version}.tar.gz

BuildRequires:	glib2-devel >= 2.44
BuildRequires:  kms-gstreamer1-devel
BuildRequires:	kms-gstreamer1-plugins-base-devel
BuildRequires:  kms-gstreamer1-devel >= 0.11.91
BuildRequires:	kms-gstreamer1-plugins-base-devel >= 0.11.91
BuildRequires:	gupnp-igd-devel >= 0.1.2
BuildRequires:  gtk-doc

%description
%{name} is an implementation of the IETF's draft Interactive Connectivity
Establishment standard (ICE). ICE is useful for applications that want to
establish peer-to-peer UDP data streams. It automates the process of traversing
NATs and provides security against some attacks. Existing standards that use
ICE include the Session Initiation Protocol (SIP) and Jingle, XMPP extension
for audio/video calls.


%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}
Requires:	glib2-devel >= 2.44
Requires:	pkgconfig


%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q -n libnice-master


%check
#make check


%build
./autogen.sh
%configure --disable-static
#sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
#sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'


%post -p /sbin/ldconfig


%postun -p /sbin/ldconfig


%files
#%doc NEWS README COPYING COPYING.LGPL COPYING.MPL
%{_bindir}/*
%{_libdir}/gstreamer-1.5/*.so
%{_libdir}/*.so.*


%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/nice.pc
%{_libdir}/girepository-1.0/*
%{_datadir}/gir-1.0/*

%changelog
