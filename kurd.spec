Summary:	KDE Universal Remote Desktop is remote desktop control client frontend
Summary(pl):	KDE Universal Remote Desktop - nak³adka dla klientów zdalnych desktopów
Name:		kurd
Version:	0.1
Release:	3
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://dl.sourceforge.net/kurd/%{name}-%{version}.tar.gz
# Source0-md5:	726808fc5dcc9372fdb12c3b495839c4
Patch0:		%{name}-Makefile.patch
Patch1:		%{name}-desktop.patch
URL:		http://kurd.sourceforge.net/
BuildRequires:	automake
BuildRequires:	kdelibs-devel
BuildRequires:	rpmbuild(macros) >= 1.129
Requires:	rdesktop
Requires:	kdebase-core >= 3.0
Requires:	vnc-client
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
cp -f /usr/share/automake/config.sub admin
kde_htmldir="%{_kdedocdir}"; export kde_htmldir
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv -f $RPM_BUILD_ROOT%{_iconsdir}/{lo,hi}color

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/kurd.desktop
%{_iconsdir}/hicolor/*/apps/kurd.png
