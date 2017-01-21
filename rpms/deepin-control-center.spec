%global project dde-control-center
%global repo %{project}

%global _commit 8b1a736714f3b46404b7037d0d149deb1c045996
%global _shortcommit %(c=%{_commit}; echo ${c:0:7})

Name:           deepin-control-center
Version:        4.0.2
Release:        2.git%{_shortcommit}%{?dist}
Summary:        New control center for linux deepin

License:        GPLv3
URL:            https://github.com/linuxdeepin/dde-control-center
Source0:        %{url}/archive/%{_commit}/%{repo}-%{_shortcommit}.tar.gz
# https://www.archlinux.org/packages/community/x86_64/deepin-control-center/
Patch0:         %{name}_4.0.2_disable-update.patch

BuildRequires:  deepin-tool-kit-devel
BuildRequires:  deepin-dock-devel
BuildRequires:  deepin-qt-dbus-factory-devel
BuildRequires:  GeoIP-devel
BuildRequires:  gtk2-devel
BuildRequires:  qt5-linguist
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtsvg-devel
BuildRequires:  qt5-qtmultimedia-devel
BuildRequires:  qt5-qtx11extras-devel
BuildRequires:  desktop-file-utils
Requires:       deepin-account-faces
Requires:       deepin-api
Requires:       deepin-daemon
Requires:       GeoIP-GeoLite-data
Requires:       GeoIP-GeoLite-data-extra
Requires:       startdde
Requires:       gtk-murrine-engine
Provides:       %{repo}%{?_isa} = %{version}-%{release}

%description
New control center for linux deepin

%prep
%setup -q -n %{repo}-%{_commit}
%patch0 -p1 -b .disable-update
sed -i 's|lrelease|lrelease-qt5|g' translate_generation.sh

%ifarch x86_64
sed -i -E '/target.path|utils.path/s|lib|lib64|' plugins/*/*.pro
sed -i 's|lib|lib64|' \
    frame/pluginscontroller.cpp \
    plugins/notify/notifydata.cpp \
    modules/update/updatemodule.cpp
%endif

%build
%qmake_qt5 PREFIX=%{_prefix} \
    QMAKE_CFLAGS_ISYSTEM= \
    WITH_MODULE_GRUB=NO \
    WITH_MODULE_REMOTE_ASSIST=NO \
    WITH_MODULE_SYSINFO_UPDATE=NO \
    DISABLE_SYS_UPDATE=YES
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}

%files
%{_bindir}/%{repo}
%{_libdir}/%{repo}/plugins/
%{_datadir}/applications/%{repo}.desktop
%{_datadir}/dbus-1/services/*.service
%{_datadir}/%{repo}/

%changelog
* Sat Jan 21 2017 mosquito <sensor.wen@gmail.com> - 4.0.2-2.git8b1a736
- Fix can not start
* Thu Jan 19 2017 mosquito <sensor.wen@gmail.com> - 4.0.2-1.git8b1a736
- Update to 4.0.2
* Tue Jan 17 2017 mosquito <sensor.wen@gmail.com> - 4.0.1-1.gitd1c1c9a
- Update to 4.0.1
* Tue Dec 27 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 3.0.24-2
- Bump to newer release because of copr signature
* Fri Dec 09 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 3.0.24-1
- Upgrade to 3.0.24
* Sun Oct 09 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 3.0.21-1
- Initial package build
