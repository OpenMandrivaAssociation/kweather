%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
#define git 20210825
#define commit dccfaa0fea063c5a79b1f8d41261e5532e5387dc

Name:		kweather
Version:	24.12.0
Release:	%{?git:0.%{git}.}2
%if 0%{?git:1}
Source0:        https://invent.kde.org/plasma-mobile/%{name}/-/archive/master/%{name}-master.tar.bz2
%else
Source0:        https://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
%endif
Summary:	Weather applet for Plasma Mobile
License:	GPLv3
Group:		Applications/Productivity
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Quick)
BuildRequires:	cmake(Qt5Test)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5Svg)
BuildRequires:	cmake(Qt5QuickControls2)
BuildRequires:	cmake(Qt5Charts)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5Kirigami2)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5Notifications)
BuildRequires:	cmake(KF5DBusAddons)
BuildRequires:	cmake(KF5Plasma)
BuildRequires:	cmake(KF5QuickCharts)
BuildRequires:	cmake(KF5KWeatherCore)
BuildRequires:	cmake(KF5KirigamiAddons)
BuildRequires:	cmake(OpenSSL)
BuildRequires:	pkgconfig(openssl)

%description
Weather applet for Plasma Mobile

%prep
%if 0%{?git}
%autosetup -p1 -n %{name}-master-%{commit}
%else
%autosetup -p1
%endif
%cmake_kde5 -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build
%find_lang %{name}

%files -f %{name}.lang
%{_bindir}/kweather
%{_datadir}/applications/org.kde.kweather.desktop
%{_datadir}/dbus-1/services/org.kde.kweather.service
%{_datadir}/icons/*/scalable/apps/org.kde.kweather.svg
%{_datadir}/metainfo/org.kde.kweather.appdata.xml
%{_libdir}/qt5/plugins/plasma/applets/plasma_applet_kweather_1x4.so
%{_datadir}/metainfo/org.kde.plasma.kweather_1x4.appdata.xml
%{_datadir}/plasma/plasmoids/org.kde.plasma.kweather_1x4
