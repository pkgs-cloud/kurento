%global kms_version kms6.6.0

%define majorminor  1.5
%define gstreamer   kms-gstreamer1

%define gst_minver  1.8.1

Name: 		%{gstreamer}-plugins-ugly
Version: 	1.8.1.1
Release: 	1
Summary: 	GStreamer streaming media framework "ugly" plug-ins

Group: 		Applications/Multimedia
License: 	LGPL
URL:		http://gstreamer.freedesktop.org/
Vendor:         GStreamer Backpackers Team <package@gstreamer.freedesktop.org>
#Source:         http://gstreamer.freedesktop.org/src/gst-plugins-ugly/gst-plugins-ugly-%{version}.tar.xz
Source:         gst-plugins-ugly-%{kms_version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires: 	%{gstreamer} >= %{gst_minver}
BuildRequires: 	%{gstreamer}-devel >= %{gst_minver}
BuildRequires:  gcc-c++
BuildRequires: opencore-amr-devel

#BuildRequires:  libsidplay-devel >= 1.36.0
#BuildRequires:  a52dec-devel >= 0.7.3
#BuildRequires:  libdvdread-devel >= 0.9.0
BuildRequires:  lame-devel >= 3.99
BuildRequires:  libmad-devel >= 0.15.0
#BuildRequires:  mpeg2dec-devel >= 0.4.0
#BuildRequires:  libmpg123-devel >= 1.13
BuildRequires: libcdio-devel

#Provides:       gstreamer-sid = %{version}-%{release}
#Provides:      gstreamer-lame = %{version}-%{release}
#Provides:       gstreamer-mad = %{version}-%{release}
#Provides:       gstreamer-a52dec = %{version}-%{release}
#Provides:       gstreamer-dvdread = %{version}-%{release}
#Provides:       gstreamer-mpeg2dec = %{version}-%{release}

Requires: x264-libs >= 0.148
Requires: lame-libs >= 3.99

Conflicts:	gstreamer1-plugins-ugly

%description
GStreamer is a streaming media framework, based on graphs of elements which
operate on media data.

This package contains well-written plug-ins that can't be shipped in
gstreamer-plugins-good because:
- the license is not LGPL
- the license of the library is not LGPL
- there are possible licensing issues with the code.

# %package devel
# Summary:        Development files for GStreamer Ugly Plugins
# Group:          Development/Libraries
#
# Requires:       %{name} = %{version}-%{release}
#
# %description devel
# GStreamer is a streaming media framework, based on graphs of elements which
# operate on media data.
#
# This package contains well-written plug-ins that can't be shipped in
# gstreamer-plugins-good because:
# - the license is not LGPL
# - the license of the library is not LGPL
# - there are possible licensing issues with the code.
# 
# This package contains development files and documentation.

%prep
%setup -q -n gst-plugins-ugly-%{kms_version}
#%setup -q -n gst-plugins-ugly

%build
./autogen.sh
%configure \
  --enable-debug
#  --enable-gtk-doc 

make %{?_smp_mflags}
                                                                                
%install
rm -rf $RPM_BUILD_ROOT

# Install doc temporarily in order to be included later by rpm
%makeinstall

# Clean out files that should not be part of the rpm.
rm -f $RPM_BUILD_ROOT%{_libdir}/gstreamer-%{majorminor}/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/gstreamer-%{majorminor}/*.a
rm -f $RPM_BUILD_ROOT%{_libdir}/*.a
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%find_lang gst-plugins-ugly-%{majorminor}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f gst-plugins-ugly-%{majorminor}.lang
%defattr(-, root, root, -)
#%doc AUTHORS COPYING README REQUIREMENTS gst-plugins-ugly.doap
%{_libdir}/gstreamer-%{majorminor}/libgstasf.so
%{_libdir}/gstreamer-%{majorminor}/libgstdvdlpcmdec.so
%{_libdir}/gstreamer-%{majorminor}/libgstxingmux.so
%{_libdir}/gstreamer-%{majorminor}/libgstrmdemux.so
%{_libdir}/gstreamer-%{majorminor}/libgstdvdsub.so

# plugins with dependencies
#%{_libdir}/gstreamer-%{majorminor}/libgstsid.so
%{_libdir}/gstreamer-%{majorminor}/libgstlame.so
%{_libdir}/gstreamer-%{majorminor}/libgstmad.so
%{_libdir}/gstreamer-%{majorminor}/libgsta52dec.so
#%{_libdir}/gstreamer-%{majorminor}/libgstdvdread.so
#%{_libdir}/gstreamer-%{majorminor}/libgstmpeg2dec.so
#%{_libdir}/gstreamer-%{majorminor}/libgstmpg123.so
#%{_libdir}/gstreamer-%{majorminor}/libgsttwolame.so
#%doc %{_datadir}/gtk-doc/html/gst-plugins-ugly-plugins-%{majorminor}/*
%{_datadir}/gstreamer-%{majorminor}/presets/GstX264Enc.prs
%{_libdir}/gstreamer-%{majorminor}/libgstx264.so
%{_libdir}/gstreamer-%{majorminor}/libgstamrnb.so
%{_libdir}/gstreamer-%{majorminor}/libgstamrwbdec.so
%{_datadir}/gstreamer-%{majorminor}/presets/GstAmrnbEnc.prs
%{_libdir}/gstreamer-%{majorminor}/libgstcdio.so


%changelog
* Fri Jun 5 2009 Jan Schmidt <thaytan at mad dot scientist dot com>
- Move x264enc plugin from -bad

* Fri Dec 15 2006 Thomas Vander Stichele <thomas at apestaart dot org>
- further cleanup
- add .doap file

* Fri Sep 02 2005 Thomas Vander Stichele <thomas at apestaart dot org>
- clean out for split into ugly
