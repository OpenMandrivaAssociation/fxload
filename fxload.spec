%define _disable_lto 1

Summary:	EZ-USB utility program
Name:		fxload
Version:	2008_10_13
Release:	3
Group:		System/Kernel and hardware
License:	GPLv2
Url:		https://linux-hotplug.sourceforge.net/
Source0:	https://netcologne.dl.sourceforge.net/project/linux-hotplug/fxload/%{version}/%{name}-%{version}.tar.gz

%description
This package contains utilities for downloading firmware to EZ-USB devices.
EZ-USB devices use 8051-based microcontrollers that have been enhanced with
registers, buffers, and other device-side support for USB transactions.

It currently supports devices based on the Anchorchips EZ-USB, as well as the
Cypress EZ-USB FX (which is almost completely source compatible) and EZ-USB FX2
(which is not).  All of these support full speed (12 Mbit/sec) transfers.  The
FX2 also supports high speed (480 Mbit/s) transfers, introduced in USB 2.0.

This version of FXLOAD supports optional use of two-stage loading, where 
special device firmware is used to support writing into off-chip memory such
as RAM (when firmware neeeds more than about 8 KBytes of code and data) or,
for firmware development, I2C serial EEPROM.

%prep
%setup -q
%autopatch -p1

%build
%make

%install
%makeinstall
mv %{buildroot}/usr/%{_datadir}/* %{buildroot}/%{_datadir}
mkdir -p %{buildroot}/sbin
mv %{buildroot}%{_sbindir}/%{name} %{buildroot}/sbin/%{name}

%files
%doc COPYING README.txt
/sbin/fxload
%{_datadir}/usb
%{_mandir}/man8/*

