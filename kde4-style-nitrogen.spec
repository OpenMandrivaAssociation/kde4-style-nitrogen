%define name	kde4-style-nitrogen
%define version	3.2.0
%define release	%mkrel 1
%define Summary	Window decoration

Summary:	%Summary
Name:		%name
Version:	%version
Release:	%release
Source0:	http://www.kde-look.org/CONTENT/content-files/99551-kde4-windeco-nitrogen-%{version}-Source.tar.gz
License:	GPLv2
Group:		Graphical desktop/KDE
URL:		http://www.kde-look.org/content/show.php/Nitrogen?content=99551
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	kdebase4-workspace-devel
Requires:	kdebase4-runtime
Conflicts:	kdebase4-runtime => 1:4.3.70

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