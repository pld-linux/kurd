Summary:	KDE Universal Remote Desktop is remote desktop control client frontend
Summary(pl):	KDE Universal Remote Desktop - nak�adka dla klient�w zdalnych desktop�w
Name:		kurd
Version:	0.1
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Patch0:		%{name}-Makefile.patch
Patch1:		%{name}-desktop.patch
URL:		http://kurd.sourceforge.net/
BuildRequires:	kdelibs-devel
Requires:	rdesktop
Requires:	kdebase >= 3.0
Requires:	tightvnc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_htmldir	/usr/share/doc/kde/HTML

%description
KDE Universal Remote Desktop has the goal of becoming an extendable
remote desktop control client frontend.

%description -l pl
KDE Universal Remote Desktop ma sta� si� rozszerzalnym frontendem dla
klient�w zdalnych desktop�w.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/kurd.desktop
%{_pixmapsdir}/locolor/*/apps/kurd.png
