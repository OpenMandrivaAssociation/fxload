%define name	fxload
%define version	2002_04_11
%define release %mkrel 15

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



%changelog
* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 2002_04_11-13mdv2011.0
+ Revision: 664399
- mass rebuild

* Thu Dec 02 2010 Oden Eriksson <oeriksson@mandriva.com> 2002_04_11-12mdv2011.0
+ Revision: 605221
- rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 2002_04_11-11mdv2010.1
+ Revision: 522681
- rebuilt for 2010.1

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 2002_04_11-10mdv2010.0
+ Revision: 424511
- rebuild

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 2002_04_11-9mdv2009.1
+ Revision: 351157
- rebuild

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 2002_04_11-8mdv2009.0
+ Revision: 221015
- rebuild

* Sun Mar 09 2008 Adam Williamson <awilliamson@mandriva.org> 2002_04_11-7mdv2008.1
+ Revision: 182740
- move binary to /sbin (this seems to be the standard)

* Wed Jan 09 2008 Herton Ronaldo Krzesinski <herton@mandriva.com.br> 2002_04_11-6mdv2008.1
+ Revision: 147248
- Added patch fxload-2002_04_11-usb_header.patch, to address bug #36214.

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - fix kernel require
    - BR kernel-server-devel-latest for asm/usb.h
    - kill re-definition of %%buildroot on Pixel's request
    - import fxload


* Tue Mar 21 2006 Austin Acton <austin@mandriva.org> 2002_04_11-5mdk
- mkrel

* Sun Mar 19 2006 Pedro Lopez-Cabanillas <plcl@users.sourceforge.net> 2002_04_11-4mdk
- Remove requirement of ezusbmidi. This program may be used to load
  other firmware files, and it can be used with udev instead of hotplug.

* Fri Sep  2 2005 Olivier Blin <oblin@mandriva.com> 2002_04_11-3mdk
- require ezusbmidi instead of hotplug, because the hotplug script
  is provided in ezusbmidi
- Patch0: fix build by including <asm/types.h>

* Mon Mar 01 2004 Olivier Thauvin <thauvin@aerov.jussieu.fr> 2002_04_11-2mdk
- Own dir

* Tue Apr 22 2002 Austin Acton <aacton@yorku.ca> 2002_04_11-1mdk
- initial package
