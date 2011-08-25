# deprecated/unmaintained according to xorg people
Summary:	X.org video driver for National Semiconductors GEODE processors
Summary(pl.UTF-8):	Sterownik obrazu X.org dla układów National Semiconductors GEODE
Name:		xorg-driver-video-nsc
Version:	2.8.3
Release:	5.1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-video-nsc-%{version}.tar.bz2
# Source0-md5:	f3ffacdc9f19e00b66bdff71b6df9b4e
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	rpmbuild(macros) >= 1.389
BuildRequires:	xorg-proto-fontsproto-devel
BuildRequires:	xorg-proto-randrproto-devel
BuildRequires:	xorg-proto-renderproto-devel
BuildRequires:	xorg-proto-videoproto-devel
BuildRequires:	xorg-proto-xextproto-devel
BuildRequires:	xorg-proto-xf86dgaproto-devel
BuildRequires:	xorg-util-util-macros >= 0.99.2
BuildRequires:	xorg-xserver-server-devel >= 1.0.99.901
%{?requires_xorg_xserver_videodrv}
Requires:	xorg-xserver-server >= 1.0.99.901
Provides:	xorg-driver-video
Obsoletes:	X11-driver-nsc < 1:7.0.0
Obsoletes:	XFree86-driver-nsc < 1:7.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X.org video driver for National Semiconductors GEODE processors. It
uses the DURANGO kit provided by National Semiconductors. The driver
supports GXLV (5530 companion chip), SC1200, SC1400 and GX2 (5535
companion chip).

%description -l pl.UTF-8
Sterownik obrazu X.org dla układów National Semiconductors GEODE.
Korzysta z zestawu programistycznego DURANGO udostępnionego przez
National Semiconductors. Obsługuje układy GXLV (układ towarzyszący
5530), SC1200, SC1400 i GX2 (układ towarzyszący 5535).

%prep
%setup -q -n xf86-video-nsc-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/xorg/modules/*/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog
%attr(755,root,root) %{_libdir}/xorg/modules/drivers/nsc_drv.so
%{_mandir}/man4/nsc.4*
