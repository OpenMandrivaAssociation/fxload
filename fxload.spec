%define name	fxload
%define version	2002_04_11
%define release %mkrel 9

Summary:	EZ-USB utility program
Name:		%name
Version:	%version
Release:	%release
Group:		System/Kernel and hardware
License:	GPL
URL:		http://linux-hotplug.sourceforge.net/
Source:		%{name}-%{version}.tar.bz2
Patch0:		fxload-2002_04_11-types.patch.bz2
# http://qa.mandriva.com/show_bug.cgi?id=36214
Patch1:		fxload-2002_04_11-usb_header.patch
BuildRoot: 	%{_tmppath}/%{name}-buildroot

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
%patch0 -p1 -b .types
%patch1 -p1 -b .usb_header

%build
%make

%install
rm -fr %{buildroot}
%makeinstall
mv %{buildroot}/usr/%{_datadir}/* %{buildroot}/%{_datadir}
mkdir -p %{buildroot}/sbin
mv %{buildroot}%{_sbindir}/%{name} %{buildroot}/sbin/%{name}

%clean
rm -fr %buildroot

%files
%defattr(-,root,root)
%doc COPYING README.txt
/sbin/fxload
%{_datadir}/usb
%{_mandir}/man8/*

