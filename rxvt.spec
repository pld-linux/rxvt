Summary:	rxvt - terminal emulator in an X window
Summary(de):	rxvt - Terminal-Emulator in einem X-Fenster
Summary(es):	Emulador de terminal en X window - rxvt
Summary(fr):	rxvt - un emulateur de terminal pour X window
Summary(pl):	Emulator terminala pod X11
Summary(pt_BR):	Emulador de terminal no X window - rxvt
Summary(ru):	rxvt - �������� ��������� VT102 ��� X Window System
Summary(tr):	X11 i�in bir u�birim yaz�l�m�
Summary(uk):	rxvt - �������� ���ͦ���� VT102 ��� X Window System
Summary(zh_CN):	rxvt - ͼ�δ����µ�ģ���ն�
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
Rxvt ist ein VT100-Terminal-Emulator f�r X. Es ist als der Nachfolger
von xterm(1) f�r Benutzer gedacht, die auf die exotischeren Funktionen
von xterm verzichten k�nnen. Insbesondere implementiert rxvt keine
Tektronix 4014-Emulation, keine Sitzungsprotokolle und keine
Konfigurierbarkeit im Toolkit-Stil. Als Folge davon belegt es
wesentlich weniger Auslagerungsplatz als xterm, was einen
signifikanten Vorteil f�r Computer bedeutet, die viele X-Sitzungen
bedienen.

%description -l es
Rxvt es un emulador de terminal VT100 para X. Tiene el objetivo de ser
un substituto de xterm(1) para usuarios que no necesiten de las
caracter�sticas m�s esot�ricas de xterm. Espec�ficamente rxvt no
implementa la emulaci�n Tektronix 4014, registro de sesi�n y
configurabilidad en el estilo toolkit. Como resultado, rxvt usa mucho
menos swap del que xterm - una ventaja significativa en una m�quina
sirviendo varias sesiones X.

%description -l fr
rxvt est un �mulateur de terminal VT100 pour X. Il est con�u pour
remplacer xterm(1) pour les utilisateurs qui n'ont pas besoin des
possibilit�s �sot�riques d'xterm. Notamment, rxvt n'implante pas
l'�mulation Tektronix 4014, le session logging et la configuration de
style toolkit. En revanche, rxvt utilise beaucoup moins d'espace de
swap qu'xterm - un avantage certain sur une machine avec de nombreuses
sessions X.

%description -l pl
Rxvt jest emulatorem terminala VT100 dla X Window. Jest on
interesuj�cym zamiennikiem dla programu xterm(1) dla u�ytkownik�w,
kt�rzy nie potrzebuj� bardziej wyszukanych mo�liwo�ci xterma jak
emulacja terminala Tektronix 4014, logowanie sesji czy pewne
mo�liwo�ci konfiguracyjnye na poziomie X toolkit. Rezygnacja z tych
mo�liwo�ci zaowocowa�a tym, �e rxvt potrzebuje o wiele mniej pami�ci
do uruchomienia.

%description -l pt_BR
Rxvt � um emulador de terminal VT100 para X. Ele tem o objetivo de ser
um substituto de xterm(1) para usu�rios que n�o necessitam das
caracter�sticas mais esot�ricas de xterm. Especificamente rxvt n�o
implementa a emula��o Tektronix 4014, registro de sess�o e
configurabilidade no estilo toolkit. Como resultado, rxvt usa muito
menos swap do que xterm - uma vantagem significativa em uma m�quina
servindo v�rias sess�es X.

%description -l ru
rxvt - �������� ��������� VT100 ��� X window. �� �������������� ���
������ ��� xterm(1) ��� �������������, ������� �� ��������� ���
����������� xterm. rxvt, � ���������, �� ��������� �������� Tektronix
4014, ���������������� ������ � ����������������� � ����� �������. �
���������� rxvt ���������� ������� ������ ����-������ ��� xterm -
������������ ������������ ��� �����, �������������� ����� X-������.

%description -l tr
rxvt, X11 i�in vt100 terminalini destekleyen bir yaz�l�md�r. As�l
geli�tirilme amac� xterm'in baz� detayl� �zelliklerine gerek duymayan
ki�iler i�in daha az kaynak harcayan bir alternatif yaratmakt�.
Textronik 4014 �yk�n�m� gibi xterm'e ait egzotik �zellikleri
gerektirmeyen ve bir�ok pencerenin a��ld��� ortamlarda son derece
avantajl� olabilir.

%description -l uk
rxvt - �������� ���ͦ���� VT100 ��� X window. ��� ��� ����������� ��
��ͦ�� ��� xterm(1) ��� ���������ަ�, ���� �� ���Ҧ�Φ �Ӧ ��������Ԧ
xterm. rxvt, �������, �� ���̦�դ �����æ� Tektronix 4014,
�������������� ��Ӧ� �� ���Ʀ������Φ��� � ���̦ Xtoolkit. ��
��������� rxvt ������դ �������� ����� ���'�Ԧ Φ� xterm - ������
�������� ��� �����, �� ���������� ������ X-��Ӧ�.

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
