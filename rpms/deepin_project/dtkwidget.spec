Name:           dtkwidget
Version:        2.0.0
Release:        2%{?dist}
Summary:        Deepin tool kit widget modules
License:        GPLv3
URL:            https://github.com/linuxdeepin/dtkwidget
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  qt5-linguist
BuildRequires:  qt5-qtbase-static
BuildRequires:  pkgconfig(dtkcore)
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(gsettings-qt)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(libstartup-notification-1.0)
BuildRequires:  pkgconfig(xcb-util)
BuildRequires:  pkgconfig(xrender)
Provides:       deepin-tool-kit%{_isa} = %{version}-%{release}
Obsoletes:      deepin-tool-kit%{_isa} < %{version}-%{release}

%description
DtkWidget is Deepin graphical user interface for deepin desktop development.

%package devel
Summary:        Development package for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Header files and libraries for %{name}.

%prep
%setup -q
sed -i 's|lrelease|lrelease-qt5|g' tool/translate_generation.sh

%build
%qmake_qt5 PREFIX=%{_prefix} LIB_INSTALL_DIR=%{_libdir}
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc README.md
%license LICENSE
%{_libdir}/lib*.so.*
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/translations
%{_datadir}/%{name}/translations/*.qm

%files devel
%{_includedir}/libdtk-*/
%{_libdir}/pkgconfig/*.pc
%{_libdir}/lib*.so

%changelog
* Thu Aug 24 2017 mosquito <sensor.wen@gmail.com> - 2.0.0-2
- Dont depend a specific version of Qt

* Sun Aug 20 2017 mosquito <sensor.wen@gmail.com> - 2.0.0-1
- Update to 2.0.0

* Sat Jul 29 2017 mosquito <sensor.wen@gmail.com> - 0.3.3-1
- Initial package build
