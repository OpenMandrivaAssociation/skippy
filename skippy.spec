Name:		skippy
Version: 0.5.0
Release:	%mkrel 7
License:	GPL
Group:		Graphical desktop/Other	
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Summary:	A full screen pager for X11
Source0:    http://thegraveyard.org/files/%{name}-%{version}.tar.bz2
Url:		http://thegraveyard.org/skippy.php
BuildRequires: imlib2-devel
BuildRequires: libx11-devel
BuildRequires: libxft-devel
BuildRequires: libxinerama-devel
BuildRequires: libxmu-devel

%description
A full screen pager for X11, not entirely unlike expocity and Apple's
Expose. It arranges snapshots of all windows on the current desktop,
allowing you to easily switch between applications. It doesn't require
a specific window manager, but requires NetWM compliance to work 
( working with gnome, fluxbox, Metacity, KWin, IceWM, and others )
%prep
%setup -q 

%build
%setup_compile_flags
%make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%_bindir/
cp %{name} $RPM_BUILD_ROOT/%_bindir/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc CHANGELOG skippyrc-default COPYING
%_bindir/*



%changelog
* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 0.5.0-7mdv2011.0
+ Revision: 614895
- the mass rebuild of 2010.1 packages

* Mon Feb 22 2010 Funda Wang <fwang@mandriva.org> 0.5.0-6mdv2010.1
+ Revision: 509813
- fix BR

  + Michael Scherer <misc@mandriva.org>
    - remove uneeded patch
    - fix Patch

* Sat Aug 02 2008 Thierry Vignaud <tv@mandriva.org> 0.5.0-6mdv2009.0
+ Revision: 260769
- rebuild

* Tue Jul 29 2008 Thierry Vignaud <tv@mandriva.org> 0.5.0-5mdv2009.0
+ Revision: 252542
- rebuild
- fix no-buildroot-tag
- fix spacing at top of description

* Thu Dec 20 2007 Thierry Vignaud <tv@mandriva.org> 0.5.0-3mdv2008.1
+ Revision: 135900
- BR X11-devel
- BR xmu-devel xft-devel
- kill re-definition of %%buildroot on Pixel's request
- use %%mkrel
- import skippy


* Fri Aug 05 2005 Michael Scherer <misc@mandriva.org> 0.5.0-3mdk
- Rebuild


* Sun Jun 27 2004 Michael Scherer <misc@mandrake.org> 0.5.0-2mdk 
- fix build ( patch 0 )

* Thu May 20 2004 Michael Scherer <misc@mandrake.org> 0.5.0-1mdk
- New release 0.5.0

* Wed May 19 2004 Michael Scherer <misc@mandrake.org> 0.4.1-1mdk
- initial release 
