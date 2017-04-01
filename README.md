# Kurento Media Server and components

RPM packages for RHEL / CentOS 7

> Compiled from [https://github.com/kurento](https://github.com/kurento) for Red Hat Enterprise Linux systems

### Installation

##### Install Kurento RPM packages with required dependencies

1. Install [**pkgs.cloud** release repository](https://github.com/pkgs-cloud/release)
2. `yum install kurento-release -y`
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
	├── kurento.conf.json	└── modules	    └── kurento	        ├── BaseRtpEndpoint.conf.ini	        ├── HttpEndpoint.conf.ini	        ├── MediaElement.conf.ini	        ├── SdpEndpoint.conf.json	        ├── UriEndpoint.conf.ini	        └── WebRtcEndpoint.conf.ini
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

##### STUN / TURNModify `/etc/kurento/modules/kurento/WebRtcEndpoint.conf.ini`


##### Log files

Log files are stored under `/var/log/kurento`  
Log level can be set in `/etc/sysconfig/kms`

### Help with Kurento

- [Tutorials](http://doc-kurento.readthedocs.io/en/stable/tutorials.html)
- [Documentation](https://doc-kurento.readthedocs.io/en/stable/)
- [Google Groups](https://groups.google.com/forum/#!forum/kurento) 

### Help with RPM packages

- [Open an issue](https://github.com/pkgs-cloud/release/issues)

---

##### DISCLAIMER

THIS SOFTWARE IS PROVIDED "AS IS" AND ANY EXPRESSED OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE REGENTS OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.