Summary:	rxvt - terminal emulator in an X window
Summary(de):	rxvt - Terminal-Emulator in einem X-Fenster
Summary(fr):	rxvt - un emulateur de terminal pour X window
Summary(pl):	Emulator terminala pod X11
Summary(tr):	X11 için bir uçbirim yazýlýmý
Name:		rxvt
Version:	2.7.3
Release:	5
Serial:		5
License:	GPL
Group:		X11/Utilities
Group(pl):	X11/Narzêdzia
Source0:	ftp://ftp.rxvt.org/pub/rxvt/devel/%{name}-%{version}.tar.gz
Source1:	rxvt.desktop
Patch0:		rxvt-utempter.patch
Patch1:		rxvt-utmp-configure.patch
BuildRequires:	XFree86-devel
BuildRequires:	utempter-devel
BuildRequires:	yodl
BuildRequires:	xpm-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Rxvt is a VT100 terminal emulator for X. It is intended as a
replacement for xterm(1) for users who do not require the more
esoteric features of xterm. Specifically rxvt does not implement the
Tektronix 4014 emulation, session logging and toolkit style
configurability. As a result, rxvt uses much less swap space than
xterm - a significant advantage on a machine serving many X sessions.

%description -l de
Rxvt ist ein VT100-Terminal-Emulator für X. Es ist als der Nachfolger
von xterm(1) für Benutzer gedacht, die auf die exotischeren Funktionen
von xterm verzichten können. Insbesondere implementiert rxvt keine
Tektronix 4014-Emulation, keine Sitzungsprotokolle und keine
Konfigurierbarkeit im Toolkit-Stil. Als Folge davon belegt es
wesentlich weniger Auslagerungsplatz als xterm, was einen
signifikanten Vorteil für Computer bedeutet, die viele X-Sitzungen
bedienen.

%description -l fr
rxvt est un émulateur de terminal VT100 pour X. Il est conçu pour
remplacer xterm(1) pour les utilisateurs qui n'ont pas besoin des
possibilités ésotériques d'xterm. Notamment, rxvt n'implante pas
l'émulation Tektronix 4014, le session logging et la configuration de
style toolkit. En revanche, rxvt utilise beaucoup moins d'espace de
swap qu'xterm - un avantage certain sur une machine avec de nombreuses
sessions X.

%description -l pl
Rxvt jest emulatorem terminala VT100 dla X Window. Jest on
interesuj±cym zamiennikiem dla programu xterm(1) dla u¿ytkowników,
którzy nie potrzebuj± bardziej wyszukanych mo¿liwo¶ci xterma jak
emulacja terminala Tektronix 4014, logowanie sesji czy pewne
mo¿liwo¶ci konfiguracyjnye na poziomie X toolkit. Rezygnacja z tych
mo¿liwo¶ci zaowocowa³a tym, ¿e rxvt potrzebuje o wiele mniej pamiêci
do uruchomienia.

%description -l tr
rxvt, X11 için vt100 terminalini destekleyen bir yazýlýmdýr. Asýl
geliþtirilme amacý xterm'in bazý detaylý özelliklerine gerek duymayan
kiþiler için daha az kaynak harcayan bir alternatif yaratmaktý.
Textronik 4014 öykünümü gibi xterm'e ait egzotik özellikleri
gerektirmeyen ve birçok pencerenin açýldýðý ortamlarda son derece
avantajlý olabilir.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
LDFLAGS="-s -lutempter" ; export LDFLAGS
%configure \
	--enable-everything \
	--enable-xgetdefault \
	--disable-menubar \
	--enable-next-xcroll \
	--enable-ttygid \
	--with-term=xterm-color
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_applnkdir}/Utilities

%{__make} DESTDIR=$RPM_BUILD_ROOT install

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Utilities

gzip -9nf doc/menu/* $RPM_BUILD_ROOT%{_mandir}/man1/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/menu/*
%{_applnkdir}/Utilities/rxvt.desktop
%attr(755,root,root) %{_bindir}/rxvt
%attr(755,root,root) %{_bindir}/rclock
%{_mandir}/man1/*
