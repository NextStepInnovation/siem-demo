# SIEM Technologies Demo

We will be speaking about a few SIEM technologies and demonstrating their basic operation. It should be possible to use the configurations and scripts in this repo to try out these technologies yourself. 

## Prerequisites 

### Windows

- Windows 10 or equivalent (up-to-date build)
    - For x64 systems: Version 1903 or higher, with Build 18362 or higher.
    - For ARM64 systems: Version 2004 or higher, with Build 19041 or higher.
    - Builds lower than 18362 do not support WSL 2. Use the [Windows Update
      Assistant](https://www.microsoft.com/software-download/windows10) to
      update your version of Windows.

- [Windows System for Linux (WSL) 2](https://docs.microsoft.com/en-us/windows/wsl/install-win10#manual-installation-steps): This will provide a backend for Docker for Windows that will work even for Windows 10 Home (otherwise, you will have to have Window 10 Pro or better)
- [Docker Desktop for Windows](https://docs.docker.com/docker-for-windows/install/)

### macOS

- [XCode command line tools](https://medium.com/flawless-app-stories/install-command-line-tools-on-macos-catalina-anansewaa-com-6f8c63120fd8)
- [Docker Desktop for Mac](https://docs.docker.com/docker-for-mac/install/)

## Background on SIEM

Security Information and Event Management (SIEM) software gives enterprise security professionals both insight into and a track record of the activities within their IT environment. 

SIEM technology has been in existence for more than a decade, initially evolving from the log management discipline. It combined security event management (SEM) – which analyzes log and event data in real time to provide threat monitoring, event correlation and incident response – with security information management (SIM) which collects, analyzes and reports on log data.           

### How SIEM works

SIEM software collects and aggregates log data generated throughout the organization’s technology infrastructure, from host systems and applications to network and security devices such as firewalls and antivirus filters.

The software then identifies and categorizes incidents and events, as well as analyzes them. The software delivers on two main objectives, which are to

- provide reports on security-related incidents and events, such as successful
  and failed logins, malware activity and other possible malicious activities
  and
- send alerts if analysis shows that an activity runs against predetermined
  rulesets and thus indicates a potential security issue.

In short, the core purpose of SIEM is to provide an accurate, real-time assessment of _what is **true**_ about the security posture of your organization and directly aid in mitigating or eliminating threats to that security.

## Demo

We will be demonstrating two technologies, Splunk and Graylog. These were chosen because they have either a free-to-use (Splunk) or open-source (Graylog) version available. Their choice should not be taken as an endorsement but rather as a means to demonstrate the common aspects of SIEM technologies.

- [Splunk](splunk)
- [Graylog](graylog)




## Sources

1. [What is SIEM software? How it works and how to choose the right tool](https://www.csoonline.com/article/2124604/what-is-siem-software-how-it-works-and-how-to-choose-the-right-tool.html)
