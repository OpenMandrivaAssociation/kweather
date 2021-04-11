#define snapshot 20200825
#define commit bdeb34190dc11f855bafb300e5879f04ff7432d5

Name:		kweather
Version:	0.4
%if 0%{?snapshot}
Release:	0.%{snapshot}.1
Source0:	https://invent.kde.org/plasma-mobile/kweather/-/archive/master/kweather-%{snapshot}.tar.bz2
%else
Release:	1
Source0:	https://invent.kde.org/plasma-mobile/kweather/-/archive/%{version}/kweather-%{version}.tar.bz2
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
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5Kirigami2)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5Notifications)
BuildRequires:	cmake(KF5DBusAddons)
BuildRequires:	cmake(KF5Plasma)
BuildRequires:	cmake(KF5QuickCharts)
BuildRequires:	cmake(OpenSSL)
BuildRequires:	pkgconfig(openssl)

%description
Weather applet for Plasma Mobile

%prep
%if 0%{?snapshot}
%autosetup -p1 -n %{name}-master-%{commit}
%else
%autosetup -p1
%endif
%cmake_kde5 -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%files
%{_bindir}/kweather
%{_datadir}/applications/org.kde.kweather.desktop
%{_datadir}/dbus-1/services/org.kde.kweather.service
%{_datadir}/icons/*/scalable/apps/kweather.svg
%{_datadir}/metainfo/org.kde.kweather.appdata.xml
