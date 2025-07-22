%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
#define git 20240218
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")

Name:		kweather
Version:	25.04.3
Release:	%{?git:0.%{git}.}1
%if 0%{?git:1}
Source0:        https://invent.kde.org/plasma-mobile/kweather/-/archive/%{gitbranch}/kweather-%{gitbranchd}.tar.bz2
%else
Source0:        https://download.kde.org/%{stable}/release-service/%{version}/src/kweather-%{version}.tar.xz
%endif
Summary:	Weather applet for Plasma Mobile
License:	GPLv3
Group:		Applications/Productivity
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Quick)
BuildRequires:	cmake(Qt6Test)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Svg)
BuildRequires:	cmake(Qt6QuickControls2)
BuildRequires:	cmake(Qt6Charts)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6Kirigami2)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6Notifications)
BuildRequires:	cmake(KF6DBusAddons)
BuildRequires:	cmake(KF6QuickCharts)
BuildRequires:	cmake(KF6KirigamiAddons)
BuildRequires:	cmake(KF6Crash)
BuildRequires:	cmake(KWeatherCore)
BuildRequires:	cmake(OpenSSL)
BuildRequires:	cmake(Plasma) > 5.90.0
BuildRequires:	pkgconfig(openssl)
BuildRequires:	%mklibname -d Plasma

%rename plasma6-kweather

BuildSystem:	cmake
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON

%description
Weather applet for Plasma Mobile

%files -f %{name}.lang
%{_bindir}/kweather
%{_datadir}/applications/org.kde.kweather.desktop
%{_datadir}/dbus-1/services/org.kde.kweather.service
%{_datadir}/icons/*/scalable/apps/org.kde.kweather.svg
%{_datadir}/metainfo/org.kde.kweather.appdata.xml
%{_libdir}/qt6/plugins/plasma/applets/plasma_applet_kweather_1x4.so
%{_datadir}/metainfo/org.kde.plasma.kweather_1x4.appdata.xml
%{_datadir}/plasma/plasmoids/org.kde.plasma.kweather_1x4
