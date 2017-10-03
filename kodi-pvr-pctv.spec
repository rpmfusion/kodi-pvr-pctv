%global commit 85d6eae79876af8a6db2413e3884296520271768
%global short_commit %(c=%{commit}; echo ${c:0:7})
%global commit_date 20170324

%global kodi_addon pvr.pctv
%global kodi_version 17.0

Name:           kodi-%(tr "." "-" <<<%{kodi_addon})
Version:        1.4.7
Release:        1%{?dist}
Summary:        PVR Client to connect PCTV Systems Broadway to Kodi

Group:          Applications/Multimedia
License:        GPLv2+
URL:            https://github.com/kodi-pvr/%{kodi_addon}/
Source0:        https://github.com/kodi-pvr/%{kodi_addon}/archive/%{short_commit}/%{name}-%{short_commit}.tar.gz
# GPLv2 license file
Source1:        http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt
# Fix jsoncpp library detection
Patch0:         %{name}-1.4.7-jsoncpp.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  jsoncpp-devel
BuildRequires:  kodi-devel >= %{kodi_version}
BuildRequires:  kodi-platform-devel >= %{kodi_version}
BuildRequires:  platform-devel
Requires:       kodi >= %{kodi_version}
ExclusiveArch:  i686 x86_64

%description
PCTV Systems frontend. Supports streaming of live TV & recordings, EPG view,
timers.


%prep
%autosetup -n %{kodi_addon}-%{commit}

cp -p %{SOURCE1} .


%build
%cmake -DCMAKE_INSTALL_LIBDIR=%{_libdir}/kodi/ .
%make_build


%install
%make_install


%files
%doc README.md %{kodi_addon}/changelog.txt
%license gpl-2.0.txt
%{_libdir}/kodi/addons/%{kodi_addon}/
%{_datadir}/kodi/addons/%{kodi_addon}/


%changelog
* Fri Apr 28 2017 Mohamed El Morabity <melmorabity@fedorapeople.org> - 1.4.7-1
- Update to latest stable release for Kodi 17

* Sat Jul 23 2016 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.2.13-1
- Update to latest stable release for Kodi 16

* Mon Aug 24 2015 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.1.11-1
- Initial RPM release
