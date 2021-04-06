%global project_name FcitxQt5

Name:           fcitx-qt5
Version:        1.2.4
Release:        3%{?dist}
Summary:        Fcitx IM module for Qt5

# The entire source code is GPLv2+ except
# platforminputcontext/ which is BSD
License:        GPLv2+ and BSD
URL:            https://github.com/fcitx/fcitx-qt5
Source0:        http://download.fcitx-im.org/%{name}/%{name}-%{version}.tar.xz

BuildRequires:  cmake
BuildRequires:  fcitx-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  libxkbcommon-devel
BuildRequires:  extra-cmake-modules
BuildRequires:  gettext-devel
# The author requests that fcitx-qt5 should be rebuilt for each minor version
# of qt5. qt5-qtbase-private-devel is not actually required for build, but
# left for Qt maintainer to tract this case.
BuildRequires:  qt5-qtbase-private-devel
%{?_qt5:Requires: %{_qt5}%{?_isa} = %{_qt5_version}}
%filter_provides_in %{_qt5_plugindir}/platforminputcontexts/libfcitxplatforminputcontextplugin.so
%filter_provides_in %{_libdir}/fcitx/qt/libfcitx-quickphrase-editor5.so
%filter_setup

%description
This package provides Fcitx Qt5 input context.

%package devel
Summary:        Development files for fcitx-qt5
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake

%description devel
The %{name}-devel package contains libraries and header files necessary for
developing programs using fcitx-qt5 libraries.

%prep
%setup -q

%build
mkdir -pv build
pushd build
%cmake ..
popd
make %{?_smp_mflags} -C build

%install
make install/fast DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p" -C build
%find_lang %{name}

%ldconfig_scriptlets

%files -f %{name}.lang
%doc README
%license COPYING COPYING.BSD
%{_libdir}/fcitx/libexec/%{name}-gui-wrapper
%{_libdir}/lib%{project_name}*.so.*
%{_libdir}/fcitx/qt/
%{_qt5_plugindir}/platforminputcontexts/libfcitxplatforminputcontextplugin.so

%files devel
%{_includedir}/%{project_name}
%{_libdir}/lib%{project_name}*.so
%{_libdir}/cmake/*


%changelog
* Tue Apr 6 2021 uoser <uoser@uniontech.com> - 1.2.4-1
- Initial Package