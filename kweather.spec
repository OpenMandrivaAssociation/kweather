%define snapshot 20200825
%define commit bdeb34190dc11f855bafb300e5879f04ff7432d5

Name:		kweather
Version:	0.2.1
Release:	0.%{snapshot}.1
Summary:	Weather applet for Plasma Mobile
Source0:	https://invent.kde.org/plasma-mobile/kweather/-/archive/master/kweather-%{snapshot}.tar.bz2
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
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5Kirigami2)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5Notifications)
BuildRequires:	cmake(KF5DBusAddons)
BuildRequires:	cmake(KF5Plasma)
BuildRequires:	cmake(OpenSSL)
BuildRequires:	pkgconfig(openssl)

%description
Weather applet for Plasma Mobile

%prep
%autosetup -p1 -n %{name}-master-%{commit}
%cmake_kde5 -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%files
%{_bindir}/kweather
%{_datadir}/applications/org.kde.kweather.desktop
%{_datadir}/icons/hicolor/scalable/apps/kweather.svg
%{_datadir}/metainfo/org.kde.kweather.appdata.xml
%{_libdir}/qt5/plugins/plasma/applets/plasma_applet_kweather_1x4.so
%{_datadir}/dbus-1/services/org.kde.kweather.service
%{_datadir}/kservices5/plasma-applet-org.kde.plasma.kweather_1x4.desktop
%{_datadir}/metainfo/org.kde.plasma.kweather_1x4.appdata.xml
%{_datadir}/plasma/plasmoids/org.kde.plasma.kweather_1x4
