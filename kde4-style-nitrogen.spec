%define name	kde4-style-nitrogen
%define version	3.3.3
%define release	3
%define Summary	Window decoration

Summary:	%Summary
Name:		%name
Version:	%version
Release:	%release
Source0:	http://www.kde-look.org/CONTENT/content-files/99551-kde4-windeco-nitrogen-%{version}-Source.tar.gz
License:	GPLv2
Group:		Graphical desktop/KDE
URL:		https://www.kde-look.org/content/show.php/Nitrogen?content=99551
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	kdebase4-workspace-devel
Requires:	kdebase4-runtime

%description
The Nitrogen window decoration is a fork of the oxygen/ozone
decoration that allows notably to

- resize window borders,
- change buttons size,
- hide the horizontal separator.
- select different title bar blending and frame border size depending
on the window title or name, in order to have better integration of
GTK based windows in the decoration style.
- add a size-grip handle in the bottom-right corner of windows. This
is particularly useful when the no-border option is selected.

%files -f kwin_nitrogen.lang
%defattr(-,root,root)
%doc README INSTALL COPYING
%_kde_libdir/kde4/kwin3_nitrogen.so
%_kde_libdir/kde4/kwin_nitrogen_config.so
%_kde_appsdir/kwin/nitrogenclient.desktop

#--------------------------------------------------------------------

%prep
%setup -q -n kde4-windeco-nitrogen-%{version}-Source

%build
%cmake_kde4
%make

%install
%__rm -rf %{buildroot}
%makeinstall_std -C build

%find_lang kwin_nitrogen

%clean
%__rm -rf %{buildroot}



%changelog
* Mon Dec 06 2010 Oden Eriksson <oeriksson@mandriva.com> 3.3.3-2mdv2011.0
+ Revision: 612550
- the mass rebuild of 2010.1 packages

* Sat Mar 13 2010 John Balcaen <mikala@mandriva.org> 3.3.3-1mdv2010.1
+ Revision: 518760
- Update to 3.3.3

* Sun Jan 31 2010 Funda Wang <fwang@mandriva.org> 3.3.2-1mdv2010.1
+ Revision: 498682
- update to new version 3.3.2

* Sat Dec 05 2009 John Balcaen <mikala@mandriva.org> 3.3.1-1mdv2010.1
+ Revision: 473650
- Update to 3.3.1

* Sat Nov 14 2009 John Balcaen <mikala@mandriva.org> 3.3.0-2mdv2010.1
+ Revision: 466043
- Rebuild

* Thu Nov 05 2009 Ahmad Samir <ahmadsamir@mandriva.org> 3.3.0-1mdv2010.1
+ Revision: 460519
- Update to 3.3.0

* Mon Sep 28 2009 John Balcaen <mikala@mandriva.org> 3.2.3-1mdv2010.0
+ Revision: 450494
- Update to 3.2.3

* Mon Sep 28 2009 John Balcaen <mikala@mandriva.org> 3.2.2-1mdv2010.0
+ Revision: 450413
- Update to 3.2.2

* Sun Sep 27 2009 John Balcaen <mikala@mandriva.org> 3.2.1-1mdv2010.0
+ Revision: 449676
- Update to 3.2.1

* Sat Sep 26 2009 John Balcaen <mikala@mandriva.org> 3.2.0-1mdv2010.0
+ Revision: 449392
- Update to 3.2.0

* Mon Sep 21 2009 John Balcaen <mikala@mandriva.org> 3.1.4-2mdv2010.0
+ Revision: 446062
- Add Conflicts: nitrogen will be the future oxygen theme on kde 4.4.x

* Sun Sep 20 2009 John Balcaen <mikala@mandriva.org> 3.1.4-1mdv2010.0
+ Revision: 446022
- import kde4-style-nitrogen

