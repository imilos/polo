%define vermaj 18
%define vermin 6-beta
%define debug_package %{nil}

Name:           polo
Version:        %{vermaj}
Release:        6_beta%{?dist}
Summary:        Advanced file manager for Linux written in Vala.

License:        LGPLv3+
URL:            https://github.com/imilos/%{name}
Source0:        https://github.com/teejee2008/%{name}/archive/v%{vermaj}.%{vermin}.tar.gz
#Source0:        https://imi.pmf.kg.ac.rs/~milos/polo-%{vermaj}.%{vermin}.tar.gz
Patch0:         vala40.patch

BuildRequires:  vala, vte291-devel, libgee-devel, json-glib-devel, libxml2-devel, chrpath, gettext
Requires:       libgee, vte291, json-glib, libxml2, libmediainfo, rsync, pv, p7zip, p7zip-plugins, tar, gzip, bzip2, xz, fish, qemu-kvm, qemu-img, gvfs, rclone, libsoup

%description
Advanced file manager for Linux written in Vala. Supports multiple panes (single, dual, quad)
with multiple tabs in each pane. Supports archive creation, extraction and browsing. Support 
for cloud storage; running and managing KVM images, modifying PDF documents and image files, 
booting ISO files in KVM, and writing ISO files to USB drives.

%prep
%autosetup -n %{name}-%{vermaj}.%{vermin} -p1

%build
make

%install
%make_install
chrpath --delete %{buildroot}%{_bindir}/polo-gtk
rm %{buildroot}%{_bindir}/polo-uninstall

%files
##%{_bindir}/gtk3-version-polo
%{_bindir}/polo-gtk
%{_bindir}/polo-disk
%{_bindir}/polo-gtk3-helper
%{_datarootdir}/applications/polo-gtk.desktop
%{_datarootdir}/appdata/polo-gtk.appdata.xml
%{_datarootdir}/locale/**/LC_MESSAGES/polo.mo
%{_datarootdir}/pixmaps/polo.png
%{_datarootdir}/polo/*

%changelog
* Thu Jun 28 2018 <imilos@gmail.com> 18-6beta
- Update to 18.6 beta
* Tue Jan 30 2018 <grturner@5x5code.com> 18-1beta
- Initial packaging

