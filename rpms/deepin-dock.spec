%global project dde-dock
%global repo %{project}

%global commit bf79f1cca5edefd14bc823c8dbdb7a4a334b3671
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           deepin-dock
Version:        4.3.3
Release:        1.git%{shortcommit}%{?dist}
Summary:        Deepin desktop-environment - Dock module
License:        GPLv3
URL:            https://github.com/linuxdeepin/dde-dock
Source0:        %{url}/archive/%{commit}/%{repo}-%{shortcommit}.tar.gz

BuildRequires:  deepin-tool-kit-devel
BuildRequires:  deepin-qt-dbus-factory-devel
BuildRequires:  gsettings-qt-devel
BuildRequires:  gtk2-devel
BuildRequires:  libXtst-devel
BuildRequires:  qt5-linguist
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtx11extras-devel
BuildRequires:  qt5-qtsvg-devel
BuildRequires:  xcb-util-wm-devel
BuildRequires:  xcb-util-image-devel
#Requires:       deepin-daemon
#Requires:       deepin-menu
#Requires:       deepin-qt-dbus-factory
#Requires:       deepin-qt5integration

Provides:       %{repo}%{?_isa} = %{version}-%{release}
Obsoletes:      %{repo}%{?_isa} < %{version}-%{release}

%description
Deepin desktop-environment - Dock module.

%package devel
Summary:        Development package for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Header files and libraries for %{name}.

%prep
%setup -q -n %{repo}-%{commit}
sed -i 's|lrelease|lrelease-qt5|g' translate_generation.sh
sed -i '/target.path/s|lib|%{_lib}|' plugins/*/*.pro
sed -i 's|lib|%{_lib}|' frame/controller/dockpluginloader.cpp

%build
%qmake_qt5 PREFIX=%{_prefix}
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%license LICENSE
%{_bindir}/%{repo}
%{_libdir}/%{repo}/
%{_datadir}/%{repo}/
%{_datadir}/dbus-1/services/*.service

%files devel
%{_includedir}/%{repo}/

%changelog
* Fri Jul 14 2017 mosquito <sensor.wen@gmail.com> - 4.3.3-1.gitbf79f1c
- Update to 4.3.3
* Fri May 19 2017 mosquito <sensor.wen@gmail.com> - 4.2.1-1.git42610ae
- Update to 4.2.1
* Tue Mar  7 2017 mosquito <sensor.wen@gmail.com> - 4.1.4-1.gitd772fe2
- Update to 4.1.4
* Sun Feb 26 2017 mosquito <sensor.wen@gmail.com> - 4.1.3-1.git26f189d
- Update to 4.1.3
* Tue Jan 17 2017 mosquito <sensor.wen@gmail.com> - 4.0.8-1.gita882590
- Update to 4.0.8
* Mon Jan 16 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 4.0.7-1
- Update to version 4.0.7 and renamed to deepin-dock
* Mon Dec 19 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 4.0.6-1
- Update to version 4.0.6
* Sun Dec 04 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 4.0.5-2
- Rebuild with newer deepin-tool-kit
* Sun Oct 02 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 4.0.5-1
- Initial package build
