# TODO: BRs
Summary:	KDE Universal Remote Desktop is remote desktop control client frontend
Summary(pl):	KDE Universal Remote Desktop - nak³adka dla klientów zdalnych desktopów
Name:		kurd
Version:	0.1
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Patch0:		%{name}-Makefile.patch
Patch1:		%{name}-desktop.patch
URL:		http://kurd.sourceforge.net/
Requires:	rdesktop
Requires:	kdebase >= 3.0
Requires:	tightvnc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KDE Universal Remote Desktop has the goal of becoming an extendable
remote desktop control client frontend.

%description -l pl
KDE Universal Remote Desktop ma staæ siê rozszerzalnym frontendem dla
klientów zdalnych desktopów.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
kde_icondir="%{_pixmapsdir}"; export kde_icondir
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/kurd.desktop
%{_pixmapsdir}/locolor/*/apps/kurd.png
