Summary:	rxvt - terminal emulator in an X window
Summary(de):	rxvt - Terminal-Emulator in einem X-Fenster
Summary(fr):	rxvt - un emulateur de terminal pour X window
Summary(pl):	Emulator terminala pod X11
Summary(tr):	X11 i�in bir u�birim yaz�l�m�
Name:		rxvt
Version:	2.6.0
Release:	1 
Copyright:	GPL
Group:		X11/Utilities
Group(pl):	X11/Narz�dzia
Source0:	ftp://ftp.math.fu-berlin.de/pub/rxvt/devel/%{name}-%{version}.tar.bz2
Source1:	rxvt.wmconfig
Patch:		rxvt-utempter.patch
BuildRequires:	utempter-devel
BuildRequires:	yodl
BuildRequires:  xpm-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define _prefix /usr/X11R6
%define _mandir /usr/X11R6/man

%description
Rxvt is a VT100 terminal emulator for X. It is intended as a replacement
for xterm(1) for users who do not require the more esoteric features of
xterm. Specifically rxvt does not implement the Tektronix 4014 emulation,
session logging and toolkit style configurability. As a result, rxvt uses
much less swap space than xterm - a significant advantage on a machine
serving many X sessions.

%description -l de
Rxvt ist ein VT100-Terminal-Emulator f�r X. Es ist als der Nachfolger 
von xterm(1) f�r Benutzer gedacht, die auf die exotischeren Funktionen 
von xterm verzichten k�nnen. Insbesondere implementiert rxvt keine 
Tektronix 4014-Emulation, keine Sitzungsprotokolle und keine 
Konfigurierbarkeit im Toolkit-Stil. Als Folge davon belegt es 
wesentlich weniger Auslagerungsplatz als xterm, was einen signifikanten 
Vorteil f�r Computer bedeutet, die viele X-Sitzungen bedienen. 

%description -l fr
rxvt est un �mulateur de terminal VT100 pour X. Il est con�u pour remplacer
xterm(1) pour les utilisateurs qui n'ont pas besoin des possibilit�s
�sot�riques d'xterm. Notamment, rxvt n'implante pas l'�mulation Tektronix
4014, le session logging et la configuration de style toolkit. En revanche,
rxvt utilise beaucoup moins d'espace de swap qu'xterm - un avantage certain
sur une machine avec de nombreuses sessions X. 

%description -l pl
Rxvt jest emulatorem terminala VT100 dla X Window. Jest on interesuj�cym
zamiennikiem dla programu xterm(1) dla u�ytkownik�w, kt�rzy nie potrzebuj�
bardziej wyszukanych mo�liwo�ci xterma jak emulacja terminala Tektronix 4014,
logowanie sesji czy pewne mo�liwo�ci konfiguracyjnye na poziomie X toolkit.
Rezygnacja z tych mo�liwo�ci zaowocowa�a tym, �e rxvt potrzebuje o wiele mniej
pami�ci do uruchomienia.

%description -l tr
rxvt, X11 i�in vt100 terminalini destekleyen bir yaz�l�md�r. As�l geli�tirilme
amac� xterm'in baz� detayl� �zelliklerine gerek duymayan ki�iler i�in daha az
kaynak harcayan bir alternatif yaratmakt�. Textronik 4014 �yk�n�m� gibi
xterm'e ait egzotik �zellikleri gerektirmeyen ve bir�ok pencerenin a��ld���
ortamlarda son derece avantajl� olabilir.

%prep
%setup -q
%patch -p1

%build
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-lutempter" \
./configure %{_target_platform} \
	--prefix=%{_prefix} \
	--mandir=%{_mandir} \
	--enable-utmp \
	--enable-xpm-background \
	--enable-transparency \
	--enable-xgetdefault \
	--disable-menubar \
	--disable-backspace-key \
	--with-term=xterm-color
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{etc/X11/wmconfig,usr/X11R6/lib/X11/app-defaults}

make install prefix=$RPM_BUILD_ROOT%{_prefix} \
	mandir=$RPM_BUILD_ROOT%{_mandir}/man1

install %{SOURCE1} $RPM_BUILD_ROOT/etc/X11/wmconfig/rxvt

gzip -9nf doc/* $RPM_BUILD_ROOT%{_mandir}/man1/* || :

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/*
%config(missingok) /etc/X11/wmconfig/rxvt
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
