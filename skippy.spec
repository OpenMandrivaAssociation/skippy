Name:		skippy
Version: 0.5.0
Release:	3mdk
License:	GPL
Group:		Graphical desktop/Other	
Summary:	A full screen pager for X11
Source0:    http://thegraveyard.org/files/%{name}-%{version}.tar.bz2
Patch0:     skippy.Makefile.patch.bz2
Url:		http://thegraveyard.org/skippy.php
BuildRequires: imlib2-devel 
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description

A full screen pager for X11, not entirely unlike expocity and Apple's
Expose. It arranges snapshots of all windows on the current desktop,
allowing you to easily switch between applications. It doesn't require
a specific window manager, but requires NetWM compliance to work 
( working with gnome, fluxbox, Metacity, KWin, IceWM, and others )
%prep
%setup -q 
%patch -p 0

%build
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

