Summary:	Decibel Audio Player is a GTK+ audio player
Summary(hu.UTF-8):	Decibel Audio Player egy GTK+ audió lejátszó
Name:		decibel-audio-player
Version:	1.06
Release:	0.1
License:	GPL v2
Group:		X11/Applications/Sound
Source0:	http://decibel.silent-blade.org/uploads/Main/%{name}-%{version}.tar.gz
# Source0-md5:	60e63607a260a909052f4ba2723df65d
URL:		http://decibel.silent-blade.org/
BuildRequires:	gettext-tools
BuildRequires:	rpm-pythonprov
Requires:	python-dbus
Requires:	python-gstreamer
Requires:	python-mutagen
Requires:	python-pygtk-glade
Requires:	python-pygtk-gtk
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Decibel Audio Player is a GTK+ audio player. It aims also at being a
real audio player and, as such, it does not include features that are
not meant to be part of an audio player. These features (e.g.,
tagging, burning) generally have a really better support in
specialized software. If you're looking for an audio player than can
also make coffee, then you should stay away from Decibel and give a
try to other players (e.g., Amarok, Exaile).

%description -l hu.UTF-8
Decibel Audio Player egy GTK+ audió lejásztó. Egy valódi zenelejátszó
akar lenni, és ezért nincsenek olyan szolgáltatásai, amelyek nem
részei egy zenelejátszónak. Ezekre a szolgáltatásokra (cimkézés,
cd-írás) vannak erre a célra készített programok. Ha egy olyan
zenelejátszót keresel, amely még a kávéd is megfőzi, tartsd magad
távol a Decibeltől, és próbálj inkább más lejátszókat (pl. Amarok,
Exaile).

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	prefix=%{_prefix} \
	DESTDIR=$RPM_BUILD_ROOT

%{find_lang} %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc doc/ChangeLog
%attr(755,root,root) %{_bindir}/*
%lang(en_GB) %{_datadir}/locale/en_GB/LC_MESSAGES/decibel-audio-player.mo
%{_datadir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png
%{_mandir}/man1/*.1*
