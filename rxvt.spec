Summary:	rxvt - terminal emulator in an X window
Summary(de.UTF-8):	rxvt - Terminal-Emulator in einem X-Fenster
Summary(es.UTF-8):	Emulador de terminal en X window - rxvt
Summary(fr.UTF-8):	rxvt - un emulateur de terminal pour X window
Summary(pl.UTF-8):	Emulator terminala dla X Window
Summary(pt_BR.UTF-8):	Emulador de terminal no X window - rxvt
Summary(ru.UTF-8):	rxvt - эмулятор терминала VT102 для X Window System
Summary(tr.UTF-8):	X11 için bir uçbirim yazılımı
Summary(uk.UTF-8):	rxvt - емулятор терміналу VT102 для X Window System
Summary(zh_CN.UTF-8):	rxvt - 图形窗口下的模拟终端
Name:		rxvt
Version:	2.7.10
Release:	5
Epoch:		1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/rxvt/%{name}-%{version}.tar.gz
# Source0-md5:	302c5c455e64047b02d1ef19ff749141
Source1:	%{name}.desktop
Patch0:		%{name}-utmp98.patch
Patch1:		%{name}-utmp98-2.patch
Patch2:		%{name}-xim.patch
Patch3:		%{name}-utmpx.patch
Patch4:		%{name}-as-needed.patch
URL:		http://www.rxvt.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	libxcb-devel
BuildRequires:	utempter-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXau-devel
BuildRequires:	xorg-lib-libXdmcp-devel
BuildRequires:	xorg-lib-libXpm-devel
Requires:	terminfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Rxvt is a VT100 terminal emulator for X. It is intended as a
replacement for xterm(1) for users who do not require the more
esoteric features of xterm. Specifically rxvt does not implement the
Tektronix 4014 emulation, session logging and toolkit style
configurability. As a result, rxvt uses much less swap space than
xterm - a significant advantage on a machine serving many X sessions.

%description -l de.UTF-8
Rxvt ist ein VT100-Terminal-Emulator für X. Es ist als der Nachfolger
von xterm(1) für Benutzer gedacht, die auf die exotischeren Funktionen
von xterm verzichten können. Insbesondere implementiert rxvt keine
Tektronix 4014-Emulation, keine Sitzungsprotokolle und keine
Konfigurierbarkeit im Toolkit-Stil. Als Folge davon belegt es
wesentlich weniger Auslagerungsplatz als xterm, was einen
signifikanten Vorteil für Computer bedeutet, die viele X-Sitzungen
bedienen.

%description -l es.UTF-8
Rxvt es un emulador de terminal VT100 para X. Tiene el objetivo de ser
un substituto de xterm(1) para usuarios que no necesiten de las
características más esotéricas de xterm. Específicamente rxvt no
implementa la emulación Tektronix 4014, registro de sesión y
configurabilidad en el estilo toolkit. Como resultado, rxvt usa mucho
menos swap del que xterm - una ventaja significativa en una máquina
sirviendo varias sesiones X.

%description -l fr.UTF-8
rxvt est un émulateur de terminal VT100 pour X. Il est conçu pour
remplacer xterm(1) pour les utilisateurs qui n'ont pas besoin des
possibilités ésotériques d'xterm. Notamment, rxvt n'implante pas
l'émulation Tektronix 4014, le session logging et la configuration de
style toolkit. En revanche, rxvt utilise beaucoup moins d'espace de
swap qu'xterm - un avantage certain sur une machine avec de nombreuses
sessions X.

%description -l pl.UTF-8
Rxvt jest emulatorem terminala VT100 dla X Window. Jest on
interesującym zamiennikiem dla programu xterm(1) dla użytkowników,
którzy nie potrzebują bardziej wyszukanych możliwości xterma jak
emulacja terminala Tektronix 4014, logowanie sesji czy pewne
możliwości konfiguracyjne na poziomie X toolkit. Rezygnacja z tych
możliwości zaowocowała tym, że rxvt potrzebuje o wiele mniej pamięci
do uruchomienia.

%description -l pt_BR.UTF-8
Rxvt é um emulador de terminal VT100 para X. Ele tem o objetivo de ser
um substituto de xterm(1) para usuários que não necessitam das
características mais esotéricas de xterm. Especificamente rxvt não
implementa a emulação Tektronix 4014, registro de sessão e
configurabilidade no estilo toolkit. Como resultado, rxvt usa muito
menos swap do que xterm - uma vantagem significativa em uma máquina
servindo várias sessões X.

%description -l ru.UTF-8
rxvt - эмулятор терминала VT100 для X window. Он разрабатывался как
замена для xterm(1) для пользователей, которым не требуется все
возможности xterm. rxvt, в частности, не реализует эмуляцию Tektronix
4014, протоколирование сессий и конфигурируемость в стиле тулкита. В
результате rxvt использует намного меньше своп-памяти чем xterm -
значительное преимущество для машин, обрабатывающих много X-сессий.

%description -l tr.UTF-8
rxvt, X11 için vt100 terminalini destekleyen bir yazılımdır. Asıl
geliştirilme amacı xterm'in bazı detaylı özelliklerine gerek duymayan
kişiler için daha az kaynak harcayan bir alternatif yaratmaktı.
Textronik 4014 öykünümü gibi xterm'e ait egzotik özellikleri
gerektirmeyen ve birçok pencerenin açıldığı ortamlarda son derece
avantajlı olabilir.

%description -l uk.UTF-8
rxvt - емулятор терміналу VT100 для X window. Він був розроблений як
заміна для xterm(1) для користувачів, яким не потрібні всі можливості
xterm. rxvt, зокрема, не реалізує емуляцію Tektronix 4014,
протоколювання сесій та конфігурованість в стилі Xtoolkit. Як
результат rxvt потребує набагато менше пам'яті ніж xterm - значна
перевага для машин, що обробляють багато X-сесій.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
mv -f autoconf/{configure.in,xpm.m4} .
#CFLAGS="%{rpmcflags} -DLINUX_KEYS"
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
	--enable-next-scroll \
	--enable-ttygid \
	--with-term=rxvt \
	--enable-half-shadow \
	--enable-smart-resize \
	--enable-256-color
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc doc/menu/* doc/*.html ChangeLog
%attr(755,root,root) %{_bindir}/rxvt
%attr(755,root,root) %{_bindir}/rclock
%attr(755,root,root) %{_libdir}/librxvt.so.*.*.*
%{_desktopdir}/rxvt.desktop
%{_mandir}/man1/*
