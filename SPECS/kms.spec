%define gst_ver 1.8.1

Summary: Meta-package to pull in all Kurento Media Server dependencies
Name: kms
Version: 6.6.3
Release: 1%{?dist}
License: GPLv2+
Group: Applications/Communications
URL: https://github.com/Kurento

Requires: kurento-media-server == %{version}
Requires: kms-core == %{version}
Requires: kms-elements == %{version}
Requires: kms-filters == %{version}
Requires: kms-jsonrpc
Requires: kms-jsoncpp
Requires: kms-libnice
Requires: kms-usrsctp
Requires: kms-gstreamer1 >= %{gst_ver}
Requires: kms-gstreamer1-plugins-good >= %{gst_ver}
Requires: kms-gstreamer1-plugins-bad >= %{gst_ver}
Requires: kms-gstreamer1-plugins-ugly >= %{gst_ver}
Requires: kms-gstreamer1-libav >= %{gst_ver}
Requires: kms-openwebrtc-gst-plugins
Requires: openssl >= 1.0.2k
Requires: opus >= 1.1.3

Requires: mediainfo

%description
A dummy package which installs all dependencies for the Kurento Media Server

%files
# No files

%changelog
