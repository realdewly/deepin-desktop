%global repo go-gir-generator

Name:           deepin-gir-generator
Version:        1.2.0
Release:        1%{?dist}
Summary:        Generate static golang bindings for GObject
License:        GPLv3
URL:            https://github.com/linuxdeepin/go-gir-generator
Source0:        %{url}/archive/%{version}/%{repo}-%{version}.tar.gz
Patch0:         SettingsBackendLike.patch
# https://cr.deepin.io/#/c/go-gir-generator/+/41653/
Patch1:         %{name}_build-with-glib2.patch

# e.g. el6 has ppc64 arch without gcc-go, so EA tag is required
ExclusiveArch:  %{?go_arches:%{go_arches}}%{!?go_arches:%{ix86} x86_64 %{arm}}
# If go_compiler is not set to 1, there is no virtual provide. Use golang instead.
BuildRequires:  %{?go_compiler:compiler(go-compiler)}%{!?go_compiler:golang}
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gudev-1.0)
Provides:       golang(gir/gobject-2.0)
Provides:       golang(gir/gio-2.0)
Provides:       golang(gir/glib-2.0)
Provides:       golang(gir/gudev-1.0)

%description
Generate static golang bindings for GObject

%prep
%setup -q -n %{repo}-%{version}

GIO_VER=$(v=$(rpm -q --qf %{RPMTAG_VERSION} gobject-introspection); echo ${v//./})
if [ $GIO_VER -ge 1521 ]; then
# Our gobject-introspection is too new
# https://cr.deepin.io/#/c/16880/
%patch0 -p1
%patch1 -p1
fi

%build
export GOPATH="%{gopath}"
%make_build

%install
%make_install

%files
%doc README.md
%license LICENSE
%{_bindir}/gir-generator
%{gopath}/src/gir/

%changelog
* Thu Jan 31 2019 mosquito <sensor.wen@gmail.com> - 1.2.0-1
- Update to 1.2.0

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Nov 19 2018 mosquito <sensor.wen@gmail.com> - 1.1.0-2
- Provides gobject-2.0 gio-2.0 glib-2.0 gudev-1.0

* Thu Nov  1 2018 mosquito <sensor.wen@gmail.com> - 1.1.0-1
- Update to 1.1.0

* Fri Aug 17 2018 mosquito <sensor.wen@gmail.com> - 1.0.4-1
- Update to 1.0.4

* Mon Aug 06 2018 Zamir SUN <zsun@fedoraproject.org> - 1.0.3-1
- Update to 1.0.3

* Tue Jul 31 2018 Florian Weimer <fweimer@redhat.com> - 1.0.2-4
- Rebuild with fixed binutils

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Oct 14 2017 mosquito <sensor.wen@gmail.com> - 1.0.2-1
- Update to 1.0.2

* Thu Aug  3 2017 mosquito <sensor.wen@gmail.com> - 1.0.1-2
- Fix undefined type SettingsBackendLike

* Fri May 19 2017 mosquito <sensor.wen@gmail.com> - 1.0.1-1.git9ee7058
- Update to 1.0.1

* Tue Jan 17 2017 mosquito <sensor.wen@gmail.com> - 0.9.6-1.gitfe260d3
- Update to 0.9.6

* Wed Jan 04 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 0.9.6-3
- Renamed package to deepin-go-gir-generator

* Sun Dec 18 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 0.9.6-2
- Changed lib path

* Fri Oct 28 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 0.9.6-1
- Compilation rework

* Thu Sep 29 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 0.9.5-2
- Compilation rework

* Sun Sep 18 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 0.9.5-1
- Initial package build
