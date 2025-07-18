#
# Conditional build:
%bcond_with	tests		# test suite

%define		kdeappsver	25.04.3
%define		kframever	5.94.0
%define		qtver		5.15.2
%define		kaname		itinerary
Summary:	Itinerary and boarding pass management application
Summary(pl.UTF-8):	Aplikacja do zarządzania trasami i kartami pokładowymi
Name:		ka6-%{kaname}
Version:	25.04.3
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	2ff786ec58771c86867fc016e905c30c
URL:		https://apps.kde.org/itinerary/
BuildRequires:	Qt6DBus-devel >= 5.15.2
BuildRequires:	Qt6Gui-devel >= 5.15.2
BuildRequires:	Qt6Location-devel
BuildRequires:	Qt6Network-devel >= 5.15.2
BuildRequires:	Qt6Positioning-devel >= 5.15.2
BuildRequires:	Qt6Qml-devel >= 5.15.2
BuildRequires:	Qt6Quick-devel
BuildRequires:	Qt6Test-devel
BuildRequires:	Qt6Widgets-devel >= 5.15.2
BuildRequires:	cmake >= 3.20
BuildRequires:	fontconfig-devel
BuildRequires:	freetype-devel
BuildRequires:	gettext-devel
BuildRequires:	ka6-kitinerary-devel >= %{kdeappsver}
BuildRequires:	ka6-kmime-devel >= %{kdeappsver}
BuildRequires:	ka6-kosmindoormap-devel >= %{kdeappsver}
BuildRequires:	ka6-kpkpass-devel >= %{kdeappsver}
BuildRequires:	ka6-kpublictransport-devel >= %{kdeappsver}
BuildRequires:	kf6-extra-cmake-modules >= 5.88
BuildRequires:	kf6-karchive-devel >= 5.91.0
BuildRequires:	kf6-kauth-devel >= 5.93.0
BuildRequires:	kf6-kcalendarcore-devel >= 5.91.0
BuildRequires:	kf6-kcodecs-devel >= 5.93.0
BuildRequires:	kf6-kcompletion-devel >= 5.93.0
BuildRequires:	kf6-kconfig-devel >= 5.93.0
BuildRequires:	kf6-kconfigwidgets-devel >= 5.93.0
BuildRequires:	kf6-kcontacts-devel >= 5.91.0
BuildRequires:	kf6-kcoreaddons-devel >= 5.93.0
BuildRequires:	kf6-kcrash-devel >= 5.88
BuildRequires:	kf6-kdbusaddons-devel >= 5.88
BuildRequires:	kf6-kholidays-devel >= 5.88
BuildRequires:	kf6-ki18n-devel >= 5.93.0
BuildRequires:	kf6-kio-devel >= 5.88
BuildRequires:	kf6-kirigami-addons-devel >= 1.6.0
BuildRequires:	kf6-kitemviews-devel >= 5.93.0
BuildRequires:	kf6-kjobwidgets-devel >= 5.93.0
BuildRequires:	kf6-knotifications-devel >= 5.88
BuildRequires:	kf6-kservice-devel >= 5.93.0
BuildRequires:	kf6-kunitconversion-devel >= 5.88
BuildRequires:	kf6-kwidgetsaddons-devel >= 5.93.0
BuildRequires:	kf6-kxmlgui-devel >= 5.93.0
BuildRequires:	kf6-networkmanager-qt-devel >= 5.88
BuildRequires:	kf6-qqc2-desktop-style-devel >= 5.88
BuildRequires:	libQuotient-qt6-devel >= 0.9.0
BuildRequires:	ninja
BuildRequires:	pkgconfig
BuildRequires:	qt6-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	shared-mime-info >= 1.0
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires(post,postun):	desktop-file-utils
BuildRequires:	zlib-devel
Obsoletes:	ka5-itinerary < 24
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Itinerary and boarding pass management application.

%description -l pl.UTF-8
Aplikacja do zarządzania trasami i kartami pokładowymi.

%prep
%setup -q -n %{kaname}-%{version}

%build
%cmake \
	-B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_DOCBUNDLEDIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON

%ninja_build -C build

%if %{with tests}
ctest --test-dir build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%find_lang %{kaname} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database_post

%postun
%update_desktop_database_postun

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_bindir}/itinerary
%attr(755,root,root) %{_libdir}/libSolidExtras.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/kfilemetadata/kfilemetadata_itineraryextractor.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/thumbcreator/itinerarythumbnail.so
%dir %{_libdir}/qt6/qml/org/kde/solidextras
%attr(755,root,root) %{_libdir}/qt6/qml/org/kde/solidextras/libsolidextrasqmlplugin.so
%{_libdir}/qt6/qml/org/kde/solidextras/qmldir
%{_desktopdir}/org.kde.itinerary.desktop
%{_iconsdir}/hicolor/scalable/apps/org.kde.itinerary.svg
%{_datadir}/knotifications6/itinerary.notifyrc
%{_datadir}/metainfo/org.kde.itinerary.appdata.xml
%{_datadir}/qlogging-categories6/org_kde_itinerary.categories
