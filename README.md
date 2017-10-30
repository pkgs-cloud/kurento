# Kurento Media Server and components

RPM packages for RHEL / CentOS 7

> Compiled from [https://github.com/kurento](https://github.com/kurento) for Red Hat Enterprise Linux systems  
> _Last updated on October 27, 2017_

### Installation

##### Install Kurento RPM packages with required dependencies

1. Install [**pkgs.cloud** release repository](https://github.com/pkgs-cloud/release)
2. `yum install kurento-release epel-release -y`
3. `yum install kms -y`

##### List all available packages

```bash
yum --disablerepo="*" --enablerepo="pkgs.cloud-kurento" list available
```

##### Additional (optional) Kurento filters

```bash
yum install kms-filters-chroma -y
yum install kms-filters-crowddetector -y
yum install kms-filters-platedetector -y
yum install kms-filters-pointerdetector -y
```

### Usage

##### Modify default settings

- `/etc/sysconfig/kms`
- `/etc/kurento`:

```
/etc/kurento
	├── kurento.conf.json
	└── modules
	    └── kurento
	        ├── BaseRtpEndpoint.conf.ini
	        ├── HttpEndpoint.conf.ini
	        ├── MediaElement.conf.ini
	        ├── SdpEndpoint.conf.json
	        ├── UriEndpoint.conf.ini
	        └── WebRtcEndpoint.conf.ini
```

##### Enable, start, restart Kurento service

1. `systemctl enable kms.service`
2. `systemctl start kms.service`
3. `systemctl restart kms.service`

##### Configure Firewall

If FirewallD is running open a range of UDP ports for RTP

```bash
firewall-cmd --zone=public --permanent --add-port=49152-65535/udp
systemctl reload firewalld
```

##### STUN / TURN

Modify `/etc/kurento/modules/kurento/WebRtcEndpoint.conf.ini`


##### Log files

Log files are stored under `/var/log/kurento`  
Log level can be set in `/etc/sysconfig/kms`

### Help with Kurento

- [Tutorials](http://doc-kurento.readthedocs.io/en/stable/tutorials.html)
- [Documentation](https://doc-kurento.readthedocs.io/en/stable/)
- [Google Groups](https://groups.google.com/forum/#!forum/kurento) 

### Help with RPM packages

- [Open an issue](https://github.com/pkgs-cloud/release/issues)

### List of Kurento RPM packages including dependencies

```
├── kurento-6.7.0-dev
│   ├── kms-6.6.3-1.el7.x86_64.rpm
│   ├── kms-cmake-utils-1.4.0-1.el7.x86_64.rpm
│   ├── kms-core-6.6.3-1.git8ec5a3a.el7.x86_64.rpm
│   ├── kms-core-devel-6.6.3-1.git8ec5a3a.el7.x86_64.rpm
│   ├── kms-elements-6.6.3-1.git0090f10.el7.x86_64.rpm
│   ├── kms-elements-devel-6.6.3-1.git0090f10.el7.x86_64.rpm
│   ├── kms-filters-6.6.3-1.git5eef962.el7.x86_64.rpm
│   ├── kms-filters-devel-6.6.3-1.git5eef962.el7.x86_64.rpm
│   ├── kms-gstreamer1-1.8.1.1-1.x86_64.rpm
│   ├── kms-gstreamer1-devel-1.8.1.1-1.x86_64.rpm
│   ├── kms-gstreamer1-libav-1.8.2.1-1.x86_64.rpm
│   ├── kms-gstreamer1-plugins-bad-1.8.1.1-1.x86_64.rpm
│   ├── kms-gstreamer1-plugins-bad-devel-1.8.1.1-1.x86_64.rpm
│   ├── kms-gstreamer1-plugins-base-1.8.1.1-1.x86_64.rpm
│   ├── kms-gstreamer1-plugins-base-devel-1.8.1.1-1.x86_64.rpm
│   ├── kms-gstreamer1-plugins-good-1.8.1.1-1.x86_64.rpm
│   ├── kms-gstreamer1-plugins-ugly-1.8.1.1-1.x86_64.rpm
│   ├── kms-jsonrpc-1.1.3-1.el7.x86_64.rpm
│   ├── kms-jsonrpc-devel-1.1.3-1.el7.x86_64.rpm
│   ├── kms-libnice-0.1.14.1-1.el7.x86_64.rpm
│   ├── kms-libnice-devel-0.1.14.1-1.el7.x86_64.rpm
│   ├── kms-openwebrtc-gst-plugins-0.10.0-1.el7.x86_64.rpm
│   ├── kms-openwebrtc-gst-plugins-devel-0.10.0-1.el7.x86_64.rpm
│   └── kurento-media-server-6.6.3-1.gitf7091a3.el7.x86_64.rpm
└── kurento-6.6.1
    ├── a52dec-0.7.4-19.el7.x86_64.rpm
    ├── a52dec-devel-0.7.4-19.el7.x86_64.rpm
    ├── boost-1.55.0-8.el7.x86_64.rpm
    ├── boost-atomic-1.55.0-8.el7.x86_64.rpm
    ├── boost-chrono-1.55.0-8.el7.x86_64.rpm
    ├── boost-context-1.55.0-8.el7.x86_64.rpm
    ├── boost-coroutine-1.55.0-8.el7.x86_64.rpm
    ├── boost-date-time-1.55.0-8.el7.x86_64.rpm
    ├── boost-devel-1.55.0-8.el7.x86_64.rpm
    ├── boost-filesystem-1.55.0-8.el7.x86_64.rpm
    ├── boost-graph-1.55.0-8.el7.x86_64.rpm
    ├── boost-graph-mpich-1.55.0-8.el7.x86_64.rpm
    ├── boost-graph-openmpi-1.55.0-8.el7.x86_64.rpm
    ├── boost-iostreams-1.55.0-8.el7.x86_64.rpm
    ├── boost-jam-1.55.0-8.el7.x86_64.rpm
    ├── boost-locale-1.55.0-8.el7.x86_64.rpm
    ├── boost-log-1.55.0-8.el7.x86_64.rpm
    ├── boost-math-1.55.0-8.el7.x86_64.rpm
    ├── boost-mpich-1.55.0-8.el7.x86_64.rpm
    ├── boost-mpich-devel-1.55.0-8.el7.x86_64.rpm
    ├── boost-mpich-python-1.55.0-8.el7.x86_64.rpm
    ├── boost-openmpi-1.55.0-8.el7.x86_64.rpm
    ├── boost-openmpi-devel-1.55.0-8.el7.x86_64.rpm
    ├── boost-openmpi-python-1.55.0-8.el7.x86_64.rpm
    ├── boost-program-options-1.55.0-8.el7.x86_64.rpm
    ├── boost-python-1.55.0-8.el7.x86_64.rpm
    ├── boost-random-1.55.0-8.el7.x86_64.rpm
    ├── boost-regex-1.55.0-8.el7.x86_64.rpm
    ├── boost-serialization-1.55.0-8.el7.x86_64.rpm
    ├── boost-signals-1.55.0-8.el7.x86_64.rpm
    ├── boost-static-1.55.0-8.el7.x86_64.rpm
    ├── boost-system-1.55.0-8.el7.x86_64.rpm
    ├── boost-test-1.55.0-8.el7.x86_64.rpm
    ├── boost-thread-1.55.0-8.el7.x86_64.rpm
    ├── boost-timer-1.55.0-8.el7.x86_64.rpm
    ├── boost-wave-1.55.0-8.el7.x86_64.rpm
    ├── faad2-2.7-6.el7.x86_64.rpm
    ├── faad2-devel-2.7-6.el7.x86_64.rpm
    ├── faad2-libs-2.7-6.el7.x86_64.rpm
    ├── fdk-aac-0.1.5-0.1.gita0bd8aa.el7.x86_64.rpm
    ├── fdk-aac-devel-0.1.5-0.1.gita0bd8aa.el7.x86_64.rpm
    ├── ffmpeg-3.1.4-1.el7.x86_64.rpm
    ├── ffmpeg-3.2.4-1.el7.x86_64.rpm
    ├── ffmpeg-devel-3.1.4-1.el7.x86_64.rpm
    ├── ffmpeg-devel-3.2.4-1.el7.x86_64.rpm
    ├── ffmpeg-libs-3.1.4-1.el7.x86_64.rpm
    ├── ffmpeg-libs-3.2.4-1.el7.x86_64.rpm
    ├── gpac-0.6.1-1.el7.x86_64.rpm
    ├── gpac-devel-0.6.1-1.el7.x86_64.rpm
    ├── gpac-devel-static-0.6.1-1.el7.x86_64.rpm
    ├── gpac-doc-0.6.1-1.el7.x86_64.rpm
    ├── gpac-libs-0.6.1-1.el7.x86_64.rpm
    ├── gstreamer1-1.8.1.1-1.x86_64.rpm
    ├── gstreamer1-devel-1.8.1.1-1.x86_64.rpm
    ├── gstreamer1-libav-1.8.2.1-1.x86_64.rpm
    ├── gstreamer1-plugins-bad-1.8.1.1-1.x86_64.rpm
    ├── gstreamer1-plugins-bad-devel-1.8.1.1-1.x86_64.rpm
    ├── gstreamer1-plugins-base-1.8.1.1-1.x86_64.rpm
    ├── gstreamer1-plugins-base-devel-1.8.1.1-1.x86_64.rpm
    ├── gstreamer1-plugins-good-1.8.1.1-1.x86_64.rpm
    ├── gstreamer1-plugins-ugly-1.8.1.1-1.x86_64.rpm
    ├── kms-6.6.1-1.el7.x86_64.rpm
    ├── kms-chroma-6.6.0-1.el7.x86_64.rpm
    ├── kms-chroma-devel-6.6.0-1.el7.x86_64.rpm
    ├── kms-cmake-utils-1.3.2-1.el7.x86_64.rpm
    ├── kms-core-6.6.1-1.el7.x86_64.rpm
    ├── kms-core-devel-6.6.1-1.el7.x86_64.rpm
    ├── kms-crowddetector-6.6.0-1.el7.x86_64.rpm
    ├── kms-crowddetector-devel-6.6.0-1.el7.x86_64.rpm
    ├── kms-elements-6.6.1-1.el7.x86_64.rpm
    ├── kms-elements-devel-6.6.1-1.el7.x86_64.rpm
    ├── kms-filters-6.6.1-1.el7.x86_64.rpm
    ├── kms-filters-devel-6.6.1-1.el7.x86_64.rpm
    ├── kms-jsoncpp-1.6.3-1.el7.x86_64.rpm
    ├── kms-jsoncpp-devel-1.6.3-1.el7.x86_64.rpm
    ├── kms-jsonrpc-1.1.2-1.el7.x86_64.rpm
    ├── kms-jsonrpc-devel-1.1.2-1.el7.x86_64.rpm
    ├── kms-libnice-0.1.13-1.el7.x86_64.rpm
    ├── kms-libnice-devel-0.1.13-1.el7.x86_64.rpm
    ├── kms-libs3-6.6.0-1.x86_64.rpm
    ├── kms-libs3-devel-6.6.0-1.x86_64.rpm
    ├── kms-openwebrtc-gst-plugins-0.10.0-1.el7.x86_64.rpm
    ├── kms-openwebrtc-gst-plugins-devel-0.10.0-1.el7.x86_64.rpm
    ├── kms-platedetector-6.6.0-1.el7.x86_64.rpm
    ├── kms-platedetector-devel-6.6.0-1.el7.x86_64.rpm
    ├── kms-pointerdetector-6.6.0-1.el7.x86_64.rpm
    ├── kms-pointerdetector-devel-6.6.0-1.el7.x86_64.rpm
    ├── kms-usrsctp-0.9.2.1-1.el7.x86_64.rpm
    ├── kms-usrsctp-devel-0.9.2.1-1.el7.x86_64.rpm
    ├── kurento-media-server-6.6.1-1.el7.x86_64.rpm
    ├── kurento-module-creator-4.0.7-1.el7.x86_64.rpm
    ├── lame-3.99.5-5.el7.x86_64.rpm
    ├── lame-devel-3.99.5-5.el7.x86_64.rpm
    ├── lame-libs-3.99.5-5.el7.x86_64.rpm
    ├── lame-mp3x-3.99.5-5.el7.x86_64.rpm
    ├── libavdevice-3.1.4-1.el7.x86_64.rpm
    ├── libavdevice-3.2.4-1.el7.x86_64.rpm
    ├── libde265-1.0.2-2.el7.x86_64.rpm
    ├── libde265-devel-1.0.2-2.el7.x86_64.rpm
    ├── libde265-examples-1.0.2-2.el7.x86_64.rpm
    ├── libevent-2.0.22-1.el7.x86_64.rpm
    ├── libevent-devel-2.0.22-1.el7.x86_64.rpm
    ├── libmad-0.15.1b-17.el7.x86_64.rpm
    ├── libmad-devel-0.15.1b-17.el7.x86_64.rpm
    ├── librtmp-2.4-7.20160224.gitfa8646d.el7.x86_64.rpm
    ├── librtmp-devel-2.4-7.20160224.gitfa8646d.el7.x86_64.rpm
    ├── libsoup-2.50.0-1.el7.x86_64.rpm
    ├── libsoup-devel-2.50.0-1.el7.x86_64.rpm
    ├── libsrtp-1.5.4-3.el7.x86_64.rpm
    ├── libsrtp-devel-1.5.4-3.el7.x86_64.rpm
    ├── mozilla-openh264-1.5.0-3.20160606git2610ab1.el7.x86_64.rpm
    ├── opencore-amr-0.1.3-4.el7.x86_64.rpm
    ├── opencore-amr-devel-0.1.3-4.el7.x86_64.rpm
    ├── opencv-2.4.7-6.el7.x86_64.rpm
    ├── opencv-core-2.4.7-6.el7.x86_64.rpm
    ├── opencv-devel-2.4.7-6.el7.x86_64.rpm
    ├── opencv-python-2.4.7-6.el7.x86_64.rpm
    ├── openh264-1.5.0-3.20160606git2610ab1.el7.x86_64.rpm
    ├── openh264-devel-1.5.0-3.20160606git2610ab1.el7.x86_64.rpm
    ├── openssl-1.0.2k-1.el7.x86_64.rpm
    ├── openssl-devel-1.0.2k-1.el7.x86_64.rpm
    ├── openssl-libs-1.0.2k-1.el7.x86_64.rpm
    ├── openssl-perl-1.0.2k-1.el7.x86_64.rpm
    ├── openssl-static-1.0.2k-1.el7.x86_64.rpm
    ├── opus-1.1.3-1.el7.x86_64.rpm
    ├── opus-devel-1.1.3-1.el7.x86_64.rpm
    ├── rtmpdump-2.4-7.20160224.gitfa8646d.el7.x86_64.rpm
    ├── sbc-1.3-5.el7.x86_64.rpm
    ├── sbc-devel-1.3-5.el7.x86_64.rpm
    ├── source-highlight-3.1.8-10.el7.x86_64.rpm
    ├── source-highlight-devel-3.1.8-10.el7.x86_64.rpm
    ├── system-python-3.6.1-0.2.rc1.el7.x86_64.rpm
    ├── system-python-libs-3.6.1-0.2.rc1.el7.x86_64.rpm
    ├── vo-aacenc-0.1.2-3.el7.x86_64.rpm
    ├── vo-aacenc-devel-0.1.2-3.el7.x86_64.rpm
    ├── vo-amrwbenc-0.1.3-2.el7.x86_64.rpm
    ├── vo-amrwbenc-devel-0.1.3-2.el7.x86_64.rpm
    ├── x264-0.148-7.20160614gita5e06b9.el7.x86_64.rpm
    ├── x264-devel-0.148-7.20160614gita5e06b9.el7.x86_64.rpm
    ├── x264-libs-0.148-7.20160614gita5e06b9.el7.x86_64.rpm
    ├── x265-1.9-1.el7.x86_64.rpm
    ├── x265-devel-1.9-1.el7.x86_64.rpm
    ├── x265-libs-1.9-1.el7.x86_64.rpm
    ├── xvidcore-1.3.4-2.el7.x86_64.rpm
    └── xvidcore-devel-1.3.4-2.el7.x86_64.rpm
```

---

##### DISCLAIMER

THIS SOFTWARE IS PROVIDED "AS IS" AND ANY EXPRESSED OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE REGENTS OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
