Summary:     rxvt - terminal emulator in an X window
Summary(de): rxvt - Terminal-Emulator in einem X-Fenster
Summary(fr): rxvt - un emulateur de terminal pour X window
Summary(pl): Emulator terminala pod X11
Summary(tr): X11 için bir uçbirim yazýlýmý
Name:        rxvt
Serial:      2
Version:     2.4.7
Release:     1
Copyright:   GPL
Group:       X11/Utilities
Source:      ftp://ftp.math.fu-berlin.de/pub/rxvt/devel/%{name}-%{version}.tar.bz2
Source1:     rxvt.wmconfig
Patch0:      rxvt-config.patch
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Rxvt is a VT100 terminal emulator for X. It is intended as a replacement
for xterm(1) for users who do not require the more esoteric features of
xterm. Specifically rxvt does not implement the Tektronix 4014 emulation,
session logging and toolkit style configurability. As a result, rxvt uses
much less swap space than xterm - a significant advantage on a machine
serving many X sessions.

%description -l de
Rxvt ist ein VT100-Terminal-Emulator für X. Es ist als der Nachfolger 
von xterm(1) für Benutzer gedacht, die auf die exotischeren Funktionen 
von xterm verzichten können. Insbesondere implementiert rxvt keine 
Tektronix 4014-Emulation, keine Sitzungsprotokolle und keine 
Konfigurierbarkeit im Toolkit-Stil. Als Folge davon belegt es 
wesentlich weniger Auslagerungsplatz als xterm, was einen signifikanten 
Vorteil für Computer bedeutet, die viele X-Sitzungen bedienen. 

%description -l fr
rxvt est un émulateur de terminal VT100 pour X. Il est conçu pour remplacer
xterm(1) pour les utilisateurs qui n'ont pas besoin des possibilités
ésotériques d'xterm. Notamment, rxvt n'implante pas l'émulation Tektronix
4014, le session logging et la configuration de style toolkit. En revanche,
rxvt utilise beaucoup moins d'espace de swap qu'xterm - un avantage certain
sur une machine avec de nombreuses sessions X. 

%description -l pl
Rxvt jest emulatorem terminala VT100 pod X Window. jest on interesuj±cym
zamiennikiem dla programu xterm(1) dla u¿ytkowników, którzy nie potrzebuj±
bardziej wyszukanyc hmo¿liwo¶ci xterma jak emulacja terminala Tektronix 4014
logowanie sesji pewnych mo¿liwo¶ci konfiguraxyjnych na poziomie X toolkit.
Rezygnacja w z powy¿szycha zaowocowa³a tym, ¿e rxvt potrzebuje o wiele mniej
pamiêci do uruchomienia.

%description -l tr
rxvt, X11 için vt100 terminalini destekleyen bir yazýlýmdýr. Asýl geliþtirilme
amacý xterm'in bazý detaylý özelliklerine gerek duymayan kiþiler için daha az
kaynak harcayan bir alternatif yaratmaktý. Textronik 4014 öykünümü gibi
xterm'e ait egzotik özellikleri gerektirmeyen ve birçok pencerenin açýldýðý
ortamlarda son derece avantajlý olabilir.

%prep
%setup -q
%patch -p1 -b .config

%build
CFLAGS="$RPM_OPT_FLAGS" \
./configure %{_target} \
	--prefix=/usr/X11R6 \
	--enable-utmp \
	--enable-wtmp \
	--enable-xpm-background 
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{etc/X11/wmconfig,usr/X11R6/lib/X11/app-defaults}

make prefix=$RPM_BUILD_ROOT/usr/X11R6 install
install %{SOURCE1} $RPM_BUILD_ROOT/etc/X11/wmconfig/rxvt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc
%config(missingok) /etc/X11/wmconfig/rxvt
%attr(755,root,root) /usr/X11R6/bin/*
/usr/X11R6/man/man1/*

%changelog
* Sun Sep 27 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [2.4.7-2]
- added -q %setup parameter,
- changed Buildroot to /tmp/%%{name}-%%{version}-root,
- added using %%{name} and %%{version} in Source,
  subpackage,
- rxvt is now builded from bziped tar source,
- added pl translation,
- spec rewrited for allow building from non-root account.

* Tue Sep 08 1998 Cristian Gafton <gafton@redhat.com>
- version 2.4.7
- old version used to be called 2.20, so now we are Serial: 1

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Fri Nov 07 1997 Michael K. Johnson <johnsonm@redhat.com>
- no paths in wmconfig files.

* Thu Oct 23 1997 Michael K. Johnson <johnsonm@redhat.com>
- added wmconfig

* Mon Jul 21 1997 Erik Troan <ewt@redhat.com>
- built against glibc

* Mon Mar 31 1997 Michael K. Johnson <johnsonm@redhat.com>
- make rxvt use standard XGetDefault instead of built-in one.
