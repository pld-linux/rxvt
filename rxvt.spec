Summary:	rxvt - terminal emulator in an X window
Summary(de):	rxvt - Terminal-Emulator in einem X-Fenster
Summary(es):	Emulador de terminal en X window - rxvt
Summary(fr):	rxvt - un emulateur de terminal pour X window
Summary(pl):	Emulator terminala pod X11
Summary(pt_BR):	Emulador de terminal no X window - rxvt
Summary(ru):	rxvt - эмулятор терминала VT102 для X Window System
Summary(tr):	X11 iГin bir uГbirim yazЩlЩmЩ
Summary(uk):	rxvt - емулятор терм╕налу VT102 для X Window System
Summary(zh_CN):	rxvt - м╪пн╢╟©зоб╣ддёдБжу╤к
Name:		rxvt
Version:	2.7.10
Release:	1
Epoch:		1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/rxvt/%{name}-%{version}.tar.bz2
# Source0-md5:	00dd774ee6e4e06d5a060266d7bb92f5
Source1:	%{name}.desktop
Patch0:		%{name}-utmp98.patch
Patch1:		%{name}-utmp98-2.patch
Patch2:		%{name}-xim.patch
Patch3:		%{name}-utmpx.patch
URL:		http://www.rxvt.org/
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	utempter-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Rxvt is a VT100 terminal emulator for X. It is intended as a
replacement for xterm(1) for users who do not require the more
esoteric features of xterm. Specifically rxvt does not implement the
Tektronix 4014 emulation, session logging and toolkit style
configurability. As a result, rxvt uses much less swap space than
xterm - a significant advantage on a machine serving many X sessions.

%description -l de
Rxvt ist ein VT100-Terminal-Emulator fЭr X. Es ist als der Nachfolger
von xterm(1) fЭr Benutzer gedacht, die auf die exotischeren Funktionen
von xterm verzichten kЖnnen. Insbesondere implementiert rxvt keine
Tektronix 4014-Emulation, keine Sitzungsprotokolle und keine
Konfigurierbarkeit im Toolkit-Stil. Als Folge davon belegt es
wesentlich weniger Auslagerungsplatz als xterm, was einen
signifikanten Vorteil fЭr Computer bedeutet, die viele X-Sitzungen
bedienen.

%description -l es
Rxvt es un emulador de terminal VT100 para X. Tiene el objetivo de ser
un substituto de xterm(1) para usuarios que no necesiten de las
caracterМsticas mАs esotИricas de xterm. EspecМficamente rxvt no
implementa la emulaciСn Tektronix 4014, registro de sesiСn y
configurabilidad en el estilo toolkit. Como resultado, rxvt usa mucho
menos swap del que xterm - una ventaja significativa en una mАquina
sirviendo varias sesiones X.

%description -l fr
rxvt est un Иmulateur de terminal VT100 pour X. Il est conГu pour
remplacer xterm(1) pour les utilisateurs qui n'ont pas besoin des
possibilitИs ИsotИriques d'xterm. Notamment, rxvt n'implante pas
l'Иmulation Tektronix 4014, le session logging et la configuration de
style toolkit. En revanche, rxvt utilise beaucoup moins d'espace de
swap qu'xterm - un avantage certain sur une machine avec de nombreuses
sessions X.

%description -l pl
Rxvt jest emulatorem terminala VT100 dla X Window. Jest on
interesuj╠cym zamiennikiem dla programu xterm(1) dla u©ytkownikСw,
ktСrzy nie potrzebuj╠ bardziej wyszukanych mo©liwo╤ci xterma jak
emulacja terminala Tektronix 4014, logowanie sesji czy pewne
mo©liwo╤ci konfiguracyjnye na poziomie X toolkit. Rezygnacja z tych
mo©liwo╤ci zaowocowaЁa tym, ©e rxvt potrzebuje o wiele mniej pamiЙci
do uruchomienia.

%description -l pt_BR
Rxvt И um emulador de terminal VT100 para X. Ele tem o objetivo de ser
um substituto de xterm(1) para usuАrios que nЦo necessitam das
caracterМsticas mais esotИricas de xterm. Especificamente rxvt nЦo
implementa a emulaГЦo Tektronix 4014, registro de sessЦo e
configurabilidade no estilo toolkit. Como resultado, rxvt usa muito
menos swap do que xterm - uma vantagem significativa em uma mАquina
servindo vАrias sessУes X.

%description -l ru
rxvt - эмулятор терминала VT100 для X window. Он разрабатывался как
замена для xterm(1) для пользователей, которым не требуется все
возможности xterm. rxvt, в частности, не реализует эмуляцию Tektronix
4014, протоколирование сессий и конфигурируемость в стиле тулкита. В
результате rxvt использует намного меньше своп-памяти чем xterm -
значительное преимущество для машин, обрабатывающих много X-сессий.

%description -l tr
rxvt, X11 iГin vt100 terminalini destekleyen bir yazЩlЩmdЩr. AsЩl
geliЧtirilme amacЩ xterm'in bazЩ detaylЩ Жzelliklerine gerek duymayan
kiЧiler iГin daha az kaynak harcayan bir alternatif yaratmaktЩ.
Textronik 4014 ЖykЭnЭmЭ gibi xterm'e ait egzotik Жzellikleri
gerektirmeyen ve birГok pencerenin aГЩldЩПЩ ortamlarda son derece
avantajlЩ olabilir.

%description -l uk
rxvt - емулятор терм╕налу VT100 для X window. В╕н був розроблений як
зам╕на для xterm(1) для користувач╕в, яким не потр╕бн╕ вс╕ можливост╕
xterm. rxvt, зокрема, не реал╕зу╓ емуляц╕ю Tektronix 4014,
протоколювання сес╕й та конф╕гурован╕сть в стил╕ Xtoolkit. Як
результат rxvt потребу╓ набагато менше пам'ят╕ н╕ж xterm - значна
перевага для машин, що обробляють багато X-сес╕й.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
mv -f autoconf/{configure.in,xpm.m4} .
CFLAGS="%{rpmcflags} -DLINUX_KEYS"
%{__libtoolize}
%{__aclocal} -I .
%{__autoheader}
%{__autoconf}
%{__automake} || :
%configure \
	--enable-shared \
	--disable-static \
	--enable-everything \
	--enable-xgetdefault \
	--enable-mousewheel \
	--disable-menubar \
	--enable-next-xcroll \
	--enable-ttygid \
	--with-term=rxvt \
	--enable-half-shadow \
	--enable-smart-resize \
	--enable-256-color 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_applnkdir}/Terminals \
	$RPM_BUILD_ROOT%{_libdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Terminals

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc doc/menu/* ChangeLog
%{_applnkdir}/Terminals/rxvt.desktop
%attr(755,root,root) %{_bindir}/rxvt
%attr(755,root,root) %{_bindir}/rclock
%attr(755,root,root) %{_libdir}/librxvt.so.*.*.*
%{_mandir}/man1/*
