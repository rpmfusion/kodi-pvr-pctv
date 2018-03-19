%global commit 5b47d9fe5a33a72c6372e9ab4d7d49644f5a5971
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate 20180205

%global kodi_addon pvr.pctv
%global kodi_version 18.0

Name:           kodi-%(tr "." "-" <<<%{kodi_addon})
Version:        2.3.1
Release:        1%{?dist}
Summary:        PCTV PVR for Kodi

License:        GPLv2+
URL:            https://github.com/kodi-pvr/%{kodi_addon}/
Source0:        https://github.com/kodi-pvr/%{kodi_addon}/archive/%{shortcommit}/%{kodi_addon}-%{shortcommit}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  kodi-devel >= %{kodi_version}
BuildRequires:  kodi-platform-devel >= %{kodi_version}
BuildRequires:  pkgconfig(jsoncpp)
BuildRequires:  platform-devel
Requires:       kodi >= %{kodi_version}
ExclusiveArch:  i686 x86_64

%description
%{summary}.


%prep
%autosetup -n %{kodi_addon}-%{commit}


%build
# https://gitlab.kitware.com/cmake/cmake/issues/17555#note_355574
export PKG_CONFIG_ALLOW_SYSTEM_CFLAGS=1
%cmake .
%make_build


%install
%make_install


%files
%doc README.md %{kodi_addon}/changelog.txt
%{_libdir}/kodi/addons/%{kodi_addon}/
%{_datadir}/kodi/addons/%{kodi_addon}/


%changelog
* Fri Mar 16 2018 Mohamed El Morabity <melmorabity@fedoraproject.org> - 2.3.1-1
- Update to latest stable release for Kodi 18

* Thu Mar 01 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 1.4.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Oct 03 2017 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.4.8-1
- Update to 1.4.8

* Fri Apr 28 2017 Mohamed El Morabity <melmorabity@fedorapeople.org> - 1.4.7-1
- Update to latest stable release for Kodi 17

* Sat Jul 23 2016 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.2.13-1
- Update to latest stable release for Kodi 16

* Mon Aug 24 2015 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.1.11-1
- Initial RPM release
